import numpy as np
from numpy import linalg as LA
from mpi4py import MPI

FRES = np.finfo(np.float64).resolution * 10.0

def partition(size_global, proc_size, proc_rank):
    '''Partition the range [0, size_global) into `proc_size` parts and return the size and start index of the part corresponding to `proc_rank`.'''
    q, r = divmod(size_global, proc_size)
    size = q + (proc_rank < r)
    
    start = q * proc_rank + min(r, proc_rank)
    return size, start

def tri_kmesh(comm, nk1d):
    '''Generate a triangular (flattened) mesh of k-points in the 1st quadrant of the Brillouin zone.'''
    proc_rank = comm.Get_rank()
    proc_size = comm.Get_size()
    nk_global = (nk1d * (nk1d + 1)) // 2
    nk, kstart = partition(nk_global, proc_size, proc_rank)
    #print(proc_rank, ":", nk, kstart)
    kmesh = np.empty((2, nk))
    for i in range(nk):
        i_global = kstart + i
        n = np.floor(np.sqrt(2.0 * i_global + 0.25) - 0.5 + FRES)
        m = i_global - n * (n + 1) / 2.0
        #print(proc_rank, ":", i, n, m)
        kmesh[0,i] = n * np.pi / nk1d
        kmesh[1,i] = m * np.pi / nk1d
    return kmesh

def n1d_tri_mesh(comm, kmesh):
    nk_global = comm.allreduce(kmesh.shape[-1], op=MPI.SUM)
    return np.floor(np.sqrt(2.0 * nk_global))

def gather(comm, array, mpi_dtype = MPI.DOUBLE, root = 0):
    '''Gathered array is flattened; Further reshape can be done by users.'''
    proc_rank = comm.Get_rank()
    # Returns a list on the `root`, `None` on other processors
    recv_count = comm.gather(array.size, root=root)
    if proc_rank == root:
        # Gathered array is flattened; Further reshape can be done by users
        recv_data = np.empty(np.sum(recv_count), dtype=array.dtype)
        recv_count = np.array(recv_count, dtype=np.int32)
        recv_displ = np.cumsum(recv_count) - recv_count
    else:
        recv_displ = None
        recv_data = None
    comm.Gatherv(array, (recv_data, recv_count, recv_displ, mpi_dtype), root=root)
    return recv_data

def all_gather(comm, array, mpi_dtype = MPI.DOUBLE):
    '''Gathered array is flattened; Further reshape can be done by users.'''
    recv_count = np.array(comm.allgather(array.size), dtype=np.int32)
    recv_data = np.empty(np.sum(recv_count), dtype=array.dtype)
    recv_displ = np.cumsum(recv_count) - recv_count
    comm.Allgatherv(array, (recv_data, recv_count, recv_displ, mpi_dtype))
    return recv_data

class BareElectron:
    def __init__(self, mu, t, kmesh, comm):
        '''This class also implements the pairing symmetry.'''
        self._chem_pot = mu
        self._hop = t
        self._comm = comm
        self.kmesh = kmesh # This will also initialize the band and pair symmetry

    # Read-only attributes
    @property
    def comm(self):
        return self._comm
    
    @property
    def tri_nk1d(self):
        '''Meaningful only if the k-mesh is triangular.'''
        return self._nk1d
    
    @property
    def k_diag_mask(self):
        return self._k_diag_mask

    @property
    def band(self):
        return self._band
    
    @property
    def band_shift_pi(self):
        return self._band2
    
    @property
    def pair_symm(self):
        return self._pair_symm
    
    @property
    def pair_symm_shift_pi(self):
        return self._pair_symm2
    
    # Read-write attributes
    @property
    def chem_pot(self):
        return self._chem_pot
    @chem_pot.setter
    def chem_pot(self, mu):
        self._chem_pot = mu
        self._band = BareElectron.Band(self._kmesh, self._chem_pot, self._hop)
        self._band2 = BareElectron.Band(self._kmesh + np.pi, self._chem_pot, self._hop)

    @property
    def hop(self):
        return self._hop
    @hop.setter
    def hop(self, t):
        self._hop = t
        self._band = BareElectron.Band(self._kmesh, self._chem_pot, self._hop)
        self._band2 = BareElectron.Band(self._kmesh + np.pi, self._chem_pot, self._hop)
    
    @property
    def kmesh(self):
        return self._kmesh
    @kmesh.setter
    def kmesh(self, kmesh):
        self._kmesh = kmesh.copy()  # Stores a copy of the input kmesh
        self._nk1d = n1d_tri_mesh(self._comm, self._kmesh)  # Meaningful only if the k-mesh is triangular
        self._k_diag_mask = np.absolute(self._kmesh[0] - self._kmesh[1]) < FRES # This is the mask for the diagonal of the k-mesh
        self._band = BareElectron.Band(self._kmesh, self._chem_pot, self._hop)
        self._band2 = BareElectron.Band(self._kmesh + np.pi, self._chem_pot, self._hop)
        self._pair_symm = BareElectron.Pair_symm(self._kmesh)
        self._pair_symm2 = BareElectron.Pair_symm(-self._kmesh - np.pi)
    
    @staticmethod
    def Band(k, mu, t):
        cx = np.cos(k[0])
        cy = np.cos(k[1])
        return -2.0 * (cx + cy) - 4.0 * t[0] * cx * cy - 4.0 * t[1] * (cx * cx + cy * cy - 1.0) - mu
    
    @staticmethod
    def Pair_symm(k):
        return np.cos(k[0]) - np.cos(k[1])

def dens_normal(beta, bare_elec: BareElectron, U):
    #e1 = np.exp(-beta * xi(kx_mesh, ky_mesh, mu, t1, t2))
    #e2 = np.exp(-beta * xi(kx_mesh + np.pi, ky_mesh + np.pi, mu, t1, t2))
    #e3 = np.exp(-beta * U)
    #return np.sum((e1 + e1 * e2 * e3) / (1.0 + e1 + e2 + e1 * e2 * e3)) * 2.0 / kx_mesh.size
    exp3 = bare_elec.band + bare_elec.band_shift_pi + U
    emin = np.minimum(bare_elec.band, bare_elec.band_shift_pi)
    np.minimum(exp3, emin, out=emin)
    np.minimum(0.0, emin, out=emin)
    exp1 = np.exp(-beta * (bare_elec.band - emin))
    exp2 = np.exp(-beta * (bare_elec.band_shift_pi - emin))
    np.exp(-beta * (exp3 - emin), out=exp3)
    np.exp(beta * emin, out=emin)
    densk = (exp1 + exp3) / (emin + exp1 + exp2 + exp3)
    densk[bare_elec.k_diag_mask] *= 0.5
    return bare_elec.comm.allreduce(np.sum(densk), op=MPI.SUM) * 2.0 / (bare_elec.tri_nk1d * bare_elec.tri_nk1d * 0.5)

def ham_block4(xi1, xi2, U, D1, D2):
    '''Works for xi1, xi2, D1, and D2 being scalars or numpy arrays.
    Returns a numpy array of shape xi1.shape + (4, 4) if xi1 is a numpy array or (4, 4) if xi1 is a scalar.
    Only the lower triangular part is specified.'''
    xi1_ = np.asanyarray(xi1)
    ham = np.empty(xi1_.shape + (4, 4))
    ham[...,0,0] = 0.0
    ham[...,1,0] = D1
    ham[...,2,0] = -D2
    ham[...,3,0] = 0.0
    ham[...,1,1] = 2.0 * xi1
    ham[...,2,1] = 0.0
    ham[...,3,1] = D2
    ham[...,2,2] = 2.0 * xi2
    ham[...,3,2] = -D1
    ham[...,3,3] = 2.0 * (xi1 + xi2 + U)
    #return np.array([[0.0, D1,        -D2,       0.0],
    #                 [D1,  2.0 * xi1, 0.0,       D2],
    #                 [-D2, 0.0,       2.0 * xi2, -D1],
    #                 [0.0, D2,        -D1,       2.0 * (xi1 + xi2 + U)]])
    return ham

def ham_block2(xi1, xi2U, D):
    '''xi2U is 2 * xi2 + U.
    
    Works for xi1 and xi2U being scalars or numpy arrays.
    Returns a numpy array of shape xi1.shape + (2, 2) if xi1 is a numpy array or (2, 2) if xi1 is a scalar.
    Only the lower triangular part is specified.'''
    xi1_ = np.asanyarray(xi1)
    ham = np.empty(xi1_.shape + (2, 2))
    ham[...,0,0] = xi1
    ham[...,1,0] = D
    ham[...,1,1] = xi1 + xi2U
    # return np.array([[xi1, D], [D, xi1 + xi2U]])
    return ham

def eigenstates(bare_elec: BareElectron, U, D0):
    # D1 = D0 * pair_symmetry(kx, ky)
    # D2 = D0 * pair_symmetry(-kx - np.pi, -ky - np.pi)
    D1 = D0 * bare_elec.pair_symm
    D2 = D0 * bare_elec.pair_symm_shift_pi
    e1, v1 = LA.eigh(ham_block4(bare_elec.band, bare_elec.band_shift_pi, U, D1, D2))
    e2, v2 = LA.eigh(ham_block2(bare_elec.band_shift_pi, 2.0 * bare_elec.band + U, D1))
    e3, v3 = LA.eigh(ham_block2(bare_elec.band, 2.0 * bare_elec.band_shift_pi + U, D2))
    e4 = bare_elec.band + bare_elec.band_shift_pi
    e5 = e4 + U
    #np.exp(-beta * e1, out=e1)
    #np.exp(-beta * e2, out=e2)
    #np.exp(-beta * e3, out=e3)
    #e4 = np.exp(-beta * e4)
    #e5 = np.exp(-beta * e5)
    emin = np.minimum(np.min(e1, axis=-1), np.min(e2, axis=-1))
    np.minimum(np.min(e3, axis=-1), emin, out=emin)
    np.minimum(e4, emin, out=emin)
    np.minimum(e5, emin, out=emin)
    #np.exp(-beta * (e1 - enmin), out=e1)
    #np.exp(-beta * (e2 - enmin), out=e2)
    #np.exp(-beta * (e3 - enmin), out=e3)
    #e4 = np.exp(-beta * (e4 - enmin))
    #e5 = np.exp(-beta * (e5 - enmin))
    emin_ = emin[..., np.newaxis]
    e1 -= emin_  # This treatment is necessary to avoid overflow in exponential functions when beta is large
    e2 -= emin_
    e3 -= emin_
    e4 -= emin
    e5 -= emin
    return (e1, v1), (e2, v2), (e3, v3), e4, e5

def gap_eq(D0, beta, bare_elec: BareElectron, U, J, fixed_point=False):
    '''Works only for a triangular k-mesh used in `bare_elec`.'''
    (e1, v1), (e2, v2), (e3, v3), e4, e5 = eigenstates(bare_elec, U, D0)
    np.exp(-beta * e1, out=e1)
    np.exp(-beta * e2, out=e2)
    np.exp(-beta * e3, out=e3)
    np.exp(-beta * e4, out=e4)
    np.exp(-beta * e5, out=e5)
    D0new_k = ( 
        -J * bare_elec.pair_symm * ( np.sum(e1 * (v1[...,0,:] * v1[...,1,:] - v1[...,2,:] * v1[...,3,:]), axis=-1) 
                                           + 2.0 * np.sum(e2 * v2[...,0,:] * v2[...,1,:], axis=-1) )
        / ( np.sum(e1, axis=-1) + 2.0 * np.sum(e2, axis=-1) + 2.0 * np.sum(e3, axis=-1) + 2.0 * e4 + 2.0 * e5 ) 
    )
    D0new_k[bare_elec.k_diag_mask] *= 0.5
    D0new = bare_elec.comm.allreduce(np.sum(D0new_k), op=MPI.SUM) / (bare_elec.tri_nk1d * bare_elec.tri_nk1d * 0.5)
    if not fixed_point:
        D0new = D0 - D0new
    bare_elec.comm.Barrier() # This is necessary to synchronize the root finding on different processes
    return D0new

# def gap_func_coeff(comm, beta, mu, t1, t2, U, J, kxs_tri=None, kys_tri=None, tol=0.001, max_iter=50, verbose=False):
#     proc_rank = comm.Get_rank()
#     if kxs_tri is None or kys_tri is None:
#         nk1d = 64
#         kxs_tri, kys_tri = tri_kmesh(comm, nk1d)
#         karea = nk1d * nk1d * 0.5
#     else:
#         nk_global = comm.allreduce(kxs_tri.size, op=MPI.SUM)
#         nk1d = np.floor(np.sqrt(2.0 * nk_global))
#         karea = nk1d * nk1d * 0.5
#     D0 = J
#     niter = 0
#     if verbose and proc_rank == 0:
#         print("Iteration D0/J")
#     while True:
#         niter += 1
#         D0old = D0
#         D0 = 0.0
#         for i in np.ndindex(kxs_tri.shape):
#             (e1, v1), (e2, v2), (e3, v3), e4, e5 = eigenstates(kxs_tri[i], kys_tri[i], mu, t1, t2, U, D0old)
#             np.exp(-beta * e1, out=e1)
#             np.exp(-beta * e2, out=e2)
#             np.exp(-beta * e3, out=e3)
#             e4 = np.exp(-beta * e4)
#             e5 = np.exp(-beta * e5)
#             D0k = ( 
#                 -J * pair_symmetry(kxs_tri[i], kys_tri[i]) * ( np.sum(e1 * (v1[0,:] * v1[1,:] - v1[2,:] * v1[3,:])) 
#                                                    + 2.0 * np.sum(e2 * v2[0,:] * v2[1,:]) )
#                 / ( np.sum(e1) + 2.0 * np.sum(e2) + 2.0 * np.sum(e3) + 2.0 * e4 + 2.0 * e5 ) 
#             )
#             if abs(kxs_tri[i] - kys_tri[i]) < FRES:
#                 D0k *= 0.5
#             D0 += D0k
#         D0 = comm.allreduce(D0, op=MPI.SUM)
#         D0 /= karea
#         if verbose and proc_rank == 0:
#             print(f"{niter:<9d} {D0 / J:.6e}")
#         if abs((D0 - D0old) / J) < tol:
#             break
#         elif niter >= max_iter:
#             print("Warning: Iteration did not converge")
#             break
#     return D0

def density(beta, bare_elec: BareElectron, U, D0):
    '''Works only for a triangular k-mesh used in `bare_elec`.'''
    (e1, v1), (e2, v2), (e3, v3), e4, e5 = eigenstates(bare_elec, U, D0)
    np.exp(-beta * e1, out=e1)
    np.exp(-beta * e2, out=e2)
    np.exp(-beta * e3, out=e3)
    np.exp(-beta * e4, out=e4)
    np.exp(-beta * e5, out=e5)
    densk = ( 
            ( np.sum(e1 * (v1[...,1,:] * v1[...,1,:] + v1[...,3,:] * v1[...,3,:]), axis=-1) 
              + 2.0 * np.sum(e2 * v2[...,1,:] * v2[...,1,:], axis=-1) + np.sum(e3 * v3[...,1,:] * v3[...,1,:], axis=-1)
              + e4 + e5 ) 
            / ( np.sum(e1, axis=-1) + 2.0 * np.sum(e2, axis=-1) + 2.0 * np.sum(e3, axis=-1) + 2.0 * e4 + 2.0 * e5 ) 
        )
    densk[bare_elec.k_diag_mask] *= 0.5
    return bare_elec.comm.allreduce(np.sum(densk), op=MPI.SUM) * 2.0 / (bare_elec.tri_nk1d * bare_elec.tri_nk1d * 0.5)

    # dens = 0.0
    # for i in np.ndindex(kxs_tri.shape):
    #     (e1, v1), (e2, v2), (e3, v3), e4, e5 = eigenstates(kxs_tri[i], kys_tri[i], mu, t1, t2, U, D0)
    #     np.exp(-beta * e1, out=e1)
    #     np.exp(-beta * e2, out=e2)
    #     np.exp(-beta * e3, out=e3)
    #     e4 = np.exp(-beta * e4)
    #     e5 = np.exp(-beta * e5)
    #     densk = ( 
    #         ( np.sum(e1 * (v1[1,:] * v1[1,:] + v1[3,:] * v1[3,:])) 
    #           + 2.0 * np.sum(e2 * v2[1,:] * v2[1,:]) + np.sum(e3 * v3[1,:] * v3[1,:])
    #           + e4 + e5 ) 
    #         / ( np.sum(e1) + 2.0 * np.sum(e2) + 2.0 * np.sum(e3) + 2.0 * e4 + 2.0 * e5 ) 
    #     )
    #     if abs(kxs_tri[i] - kys_tri[i]) < FRES:
    #         densk *= 0.5
    #     dens += densk
    # dens = comm.allreduce(dens, op=MPI.SUM)
    # return dens * 2.0 / karea

def lorentzian(x, delta=0.04):
    return delta / ((x * x + delta * delta) * np.pi)

def spectrum(omega, beta, bare_elec: BareElectron, U, D0, delta=0.04):
    '''Works for any k-mesh used in `bare_elec`. Returns a spectrum of shape omega.shape + kmesh.shape[1:].'''
    (e1, v1), (e2, v2), (e3, v3), e4, e5 = eigenstates(bare_elec, U, D0)
    exp1 = np.exp(-beta * e1)
    exp2 = np.exp(-beta * e2)
    exp3 = np.exp(-beta * e3)
    exp4 = np.exp(-beta * e4)
    exp5 = np.exp(-beta * e5)
    Z = np.sum(exp1, axis=-1) + 2.0 * np.sum(exp2, axis=-1) + 2.0 * np.sum(exp3, axis=-1) + 2.0 * exp4 + 2.0 * exp5
    s = np.array([[-1.0], [1.0]])
    omega1 = np.asanyarray(omega)  # Store this because it might make a copy, e.g., when omega is a scalar
    # omega2 = np.expand_dims(omega1, axis=omega1.ndim)
    # return (
    #     np.sum(np.square(np.sum(v3 * v1[1::2,0,np.newaxis], axis=0)) * ((exp3 + exp1[0]) / Z) * lorentzian(omega2 + e3 - e1[0], delta=delta), axis=omega2.ndim - 1)
    #     + np.sum(np.square(np.sum(v3 * v1[1::2,1,np.newaxis], axis=0)) * ((exp3 + exp1[1]) / Z) * lorentzian(omega2 + e3 - e1[1], delta=delta), axis=omega2.ndim - 1)
    #     + np.sum(np.square(np.sum(v3 * v1[1::2,2,np.newaxis], axis=0)) * ((exp3 + exp1[2]) / Z) * lorentzian(omega2 + e3 - e1[2], delta=delta), axis=omega2.ndim - 1)
    #     + np.sum(np.square(np.sum(v3 * v1[1::2,3,np.newaxis], axis=0)) * ((exp3 + exp1[3]) / Z) * lorentzian(omega2 + e3 - e1[3], delta=delta), axis=omega2.ndim - 1)
    #     + np.sum(np.square(np.sum(v1[::2,:] * v3[:,0,np.newaxis] * s, axis=0)) * ((exp1 + exp3[0]) / Z) * lorentzian(omega2 + e1 - e3[0], delta=delta), axis=omega2.ndim - 1)
    #     + np.sum(np.square(np.sum(v1[::2,:] * v3[:,1,np.newaxis] * s, axis=0)) * ((exp1 + exp3[1]) / Z) * lorentzian(omega2 + e1 - e3[1], delta=delta), axis=omega2.ndim - 1)
    #     + np.sum(np.square(v2[1,:]) * ((exp4 + exp2) / Z) * lorentzian(omega2 + e4 - e2, delta=delta), axis=omega2.ndim - 1)
    #     + np.sum(np.square(v2[1,:]) * ((exp5 + exp2) / Z) * lorentzian(omega2 + e5 - e2, delta=delta), axis=omega2.ndim - 1)
    #     + np.sum(np.square(v2[0,:]) * ((exp2 + exp5) / Z) * lorentzian(omega2 + e2 - e5, delta=delta), axis=omega2.ndim - 1)
    #     + np.sum(np.square(v2[0,:]) * ((exp2 + exp4) / Z) * lorentzian(omega2 + e2 - e4, delta=delta), axis=omega2.ndim - 1)
    # )
    Z_ = Z[..., np.newaxis]
    # s_ = s.reshape((1,) * (e1.ndim - 1) + s.shape)
    omega_ = omega1.reshape(omega1.shape + (1,) * e1.ndim)
    # return (  # v1[...,1::2,0:1] is equivalent to v1[1::2,0,np.newaxis], i.e., keeping the last dimension
    #     np.sum(np.square(np.sum(v3 * v1[...,1::2,0:1], axis=-2)) * ((exp3 + exp1[...,0:1]) / Z_) * lorentzian(omega_ + e3 - e1[...,0:1], delta=delta), axis=-1)
    #     + np.sum(np.square(np.sum(v3 * v1[...,1::2,1:2], axis=-2)) * ((exp3 + exp1[...,1:2]) / Z_) * lorentzian(omega_ + e3 - e1[...,1:2], delta=delta), axis=-1)
    #     + np.sum(np.square(np.sum(v3 * v1[...,1::2,2:3], axis=-2)) * ((exp3 + exp1[...,2:3]) / Z_) * lorentzian(omega_ + e3 - e1[...,2:3], delta=delta), axis=-1)
    #     + np.sum(np.square(np.sum(v3 * v1[...,1::2,3:4], axis=-2)) * ((exp3 + exp1[...,3:4]) / Z_) * lorentzian(omega_ + e3 - e1[...,3:4], delta=delta), axis=-1)
    #     + np.sum(np.square(np.sum(v1[...,::2,:] * v3[...,:,0:1] * s_, axis=-2)) * ((exp1 + exp3[...,0:1]) / Z_) * lorentzian(omega_ + e1 - e3[...,0:1], delta=delta), axis=-1)
    #     + np.sum(np.square(np.sum(v1[...,::2,:] * v3[...,:,1:2] * s_, axis=-2)) * ((exp1 + exp3[...,1:2]) / Z_) * lorentzian(omega_ + e1 - e3[...,1:2], delta=delta), axis=-1)
    #     + np.sum(np.square(v2[...,1,:]) * ((exp4[...,np.newaxis] + exp2) / Z_) * lorentzian(omega_ + e4[...,np.newaxis] - e2, delta=delta), axis=-1)
    #     + np.sum(np.square(v2[...,1,:]) * ((exp5[...,np.newaxis] + exp2) / Z_) * lorentzian(omega_ + e5[...,np.newaxis] - e2, delta=delta), axis=-1)
    #     + np.sum(np.square(v2[...,0,:]) * ((exp2 + exp5[...,np.newaxis]) / Z_) * lorentzian(omega_ + e2 - e5[...,np.newaxis], delta=delta), axis=-1)
    #     + np.sum(np.square(v2[...,0,:]) * ((exp2 + exp4[...,np.newaxis]) / Z_) * lorentzian(omega_ + e2 - e4[...,np.newaxis], delta=delta), axis=-1)
    # )
    Z__ = Z[..., np.newaxis, np.newaxis]
    s__ = s.reshape((1,) * (e1.ndim - 1) + s.shape + (1,))
    omega__ = omega1.reshape(omega1.shape + (1,) * (e1.ndim + 1))
    return (
        np.sum(np.square(np.sum(v3[...,np.newaxis] * v1[...,1::2,np.newaxis,:], axis=-3)) * ((exp3[...,np.newaxis] + exp1[...,np.newaxis,:]) / Z__) * lorentzian(omega__ + e3[...,np.newaxis] - e1[...,np.newaxis,:], delta=delta), axis=(-1, -2))
        + np.sum(np.square(np.sum(v1[...,::2,:,np.newaxis] * v3[...,np.newaxis,:] * s__, axis=-3)) * ((exp1[...,np.newaxis] + exp3[...,np.newaxis,:]) / Z__) * lorentzian(omega__ + e1[...,np.newaxis] - e3[...,np.newaxis,:], delta=delta), axis=(-1, -2))
        + np.sum(np.square(v2[...,1,:]) * ((exp4[...,np.newaxis] + exp2) / Z_) * lorentzian(omega_ + e4[...,np.newaxis] - e2, delta=delta), axis=-1)
        + np.sum(np.square(v2[...,1,:]) * ((exp5[...,np.newaxis] + exp2) / Z_) * lorentzian(omega_ + e5[...,np.newaxis] - e2, delta=delta), axis=-1)
        + np.sum(np.square(v2[...,0,:]) * ((exp2 + exp5[...,np.newaxis]) / Z_) * lorentzian(omega_ + e2 - e5[...,np.newaxis], delta=delta), axis=-1)
        + np.sum(np.square(v2[...,0,:]) * ((exp2 + exp4[...,np.newaxis]) / Z_) * lorentzian(omega_ + e2 - e4[...,np.newaxis], delta=delta), axis=-1)
    )