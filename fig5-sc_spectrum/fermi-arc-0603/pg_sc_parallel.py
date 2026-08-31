import numpy as np
from scipy import optimize
from mpi4py import MPI
# import h5py
import matplotlib.pyplot as plt
plt.style.use("publication")
from timeit import default_timer as timer
import wormsc
#np.show_config(mode="stdout")

t_start = timer()

comm = MPI.COMM_WORLD
proc_rank = comm.Get_rank()

hop = np.array([-0.16, 0.0])
mu_opt = 4.0 * (hop[0] - hop[1])   
U = 1.15  # 1.1
J = 0.235 * 2.32  # 0.8
# T = 0.001
# mu = -2.0
save_data = False
case_id = 4

# beta = 1.0 / T


kmesh = wormsc.tri_kmesh(comm, 256)
# kmesh_fine = wormsc.tri_kmesh(comm, 512)

# fig, ax = plt.subplots()
# ax.plot(kmesh[0], kmesh[1], marker='.', linestyle='None')
# ax.set_aspect('equal')
# ax.set_xlabel(r"$k_x$")
# ax.set_ylabel(r"$k_y$")
# ax.set_title(f"Triangular mesh on processor {proc_rank}")

bare_elec = wormsc.BareElectron(mu_opt, hop, kmesh, comm)

# Critical hole doping level for pseudogap onset at (near) zero temperature, for any U
p_pg = 1.0 - wormsc.dens_normal(1.0 / 0.001, bare_elec, U)
#p_pg = 1.0 - density(comm, 1.0 / 0.001, 4.0 * (t1 - t2), t1, t2, U, 0.0, kxs_tri=kxs_tri, kys_tri=kys_tri)
if proc_rank == 0:
    print(f"p_pg = {p_pg:g}")

Ts = np.linspace(0.0001 * J, 0.08 * J, 100)
mus = np.linspace(mu_opt + 0.4, mu_opt - 0.4, 50)
D0s = np.empty((Ts.size, mus.size))
ps = np.empty_like(D0s)
# N0 = np.zeros_like(mus)  # Normal-phase DOS at the Fermi level
for i, mu in enumerate(mus):
    if proc_rank == 0:
        print("{:4d}  {:11.4e}".format(i, mu))
    bare_elec.chem_pot = mu
    for j, T in enumerate(Ts):
        beta = 1.0 / T
        sol = optimize.root_scalar(wormsc.gap_eq, args=(beta, bare_elec, U, J), method='secant', x0=0.5 * J, x1=0.4 * J)
        D0s[j,i] = np.abs(sol.root)
        # for ind in np.ndindex(kxs_tri.shape):
        #     N0k = wormsc.spectrum(kxs_tri[ind], kys_tri[ind], 0.0, beta, mu, t1, t2, U, 0.0)
        #     if abs(kxs_tri[ind] - kys_tri[ind]) < wormsc.FRES:
        #         N0k *= 0.5
        #     N0[i] += N0k
        # N0k = wormsc.spectrum(0.0, beta, bare_elec, U, 0.0)
        # N0k[bare_elec.k_diag_mask] *= 0.5
        # N0[i] = bare_elec.comm.allreduce(np.sum(N0k)) / (bare_elec.tri_nk1d * bare_elec.tri_nk1d * 0.5)
        ps[j,i] = 1.0 - wormsc.dens_normal(beta, bare_elec, U)  # Density in the normal phase
        #ps[i] = 1.0 - density(comm, beta, mu, t1, t2, U, 0.0, kxs_tri=kxs_tri, kys_tri=kys_tri)  # Density in the normal phase
# comm.Allreduce(MPI.IN_PLACE, N0, op=MPI.SUM)
# N0 /= karea
dD0 = np.abs(np.diff(D0s, axis=0))
idD0max = np.argmax(dD0, axis=0)
no_trans = np.max(D0s, axis=0) < 0.001 * J
Tcs = (Ts[idD0max] + Ts[idD0max + 1]) * 0.5
Tcs[no_trans] = Ts[0]
pcs = (ps[idD0max, range(mus.size)] + ps[idD0max + 1, range(mus.size)]) * 0.5
pcs[no_trans] = ps[0,no_trans]
# if proc_rank == 0:
#    np.savetxt("worm-Tc-p.txt", np.stack((pcs, Tcs), axis=1),
#               header="Worm model, mean-field pairing interaction\nU={:g}, J={:g}, t={}\np  T_c".format(U, J, np.array2string(hop, formatter={"float_kind":lambda x: "{:g}".format(x)})))

numk = 100
Gpt = np.array([0.0, 0.0])
Xpt = np.array([np.pi, 0.0])
Mpt = np.array([np.pi, np.pi])
GX = np.linalg.norm(Xpt - Gpt)
XM = np.linalg.norm(Mpt - Xpt)
MG = np.linalg.norm(Gpt - Mpt)
kGX = np.linspace(Gpt, Xpt, numk, endpoint=False, axis=1)
kXM = np.linspace(Xpt, Mpt, numk, endpoint=False, axis=1)
kMG = np.linspace(Mpt, Gpt, numk + 1, axis=1)
kpath = np.hstack((kGX, kXM, kMG))
klen = np.zeros(kpath.shape[1])
for i in range(1, klen.size):
    klen[i] = klen[i - 1] + np.linalg.norm(kpath[:,i] - kpath[:,i - 1])
omegas = np.linspace(-1.5, 1.5, 200)

iD0 = np.unravel_index(np.argmax(D0s), D0s.shape)  # np.argmax(D0s), -5
bare_elec.kmesh = kpath
bare_elec.chem_pot = mus[iD0[1]]
beta0 = 1.0 / Ts[iD0[0]]
A0kw = wormsc.spectrum(omegas, beta0, bare_elec, U, 0.0)
Akw = wormsc.spectrum(omegas, beta0, bare_elec, U, D0s[iD0])
if proc_rank == 0:
    print("Spectral weight integral =", np.trapezoid(Akw[:,numk], x=omegas))

kvec = np.linspace(0.0, np.pi, 100)
KX, KY = np.meshgrid(kvec, kvec)
KMESH = np.stack((KX, KY), axis=0)
bare_elec.kmesh = KMESH
Ak0 = wormsc.spectrum(0.0, beta0, bare_elec, U, D0s[iD0])

t_end = timer()
if proc_rank == 0:
    print("Time:", (t_end - t_start) / 60.0, "min")

#==================== Post-processing ====================
if proc_rank == 0:
    #------------------ Write to file --------------------
    if save_data:
        with h5py.File("worm-sc.hdf5", 'a') as data_file:
            grp = data_file.require_group(f"case{case_id}")
            grp.attrs.modify("t1", hop[0]) # This will also create the attribute if it does not exist
            grp.attrs.modify("t2", hop[1])
            grp.attrs.modify('U', U)  
            grp.attrs.modify('J', J)
            grp.attrs.modify("p_pg", p_pg)
            #del grp["temperature11"]
            grp.require_dataset("mu", mus.shape, mus.dtype)[...] = mus
            grp.require_dataset("p", ps.shape, ps.dtype)[...] = ps
            grp.require_dataset("T", Ts.shape, Ts.dtype)[...] = Ts
            grp.require_dataset("Delta0", D0s.shape, D0s.dtype)[...] = D0s
            print(grp.keys())
    #------------- End for writing to file ---------------
    fig, ax = plt.subplots()
    ax.plot(pcs, Tcs, marker='o')
    ax.set_xlabel(r"$p$")
    ax.set_ylabel(r"$T_c$")

    # fig, ax = plt.subplots()
    # ax.plot(ps, D0s, marker='o', color="C0")
    # ax.axvline(x=p_pg, color="gray", linestyle=":")
    # #ax.set_xlim(left=0)
    # #ax.set_ylim(bottom=0)
    # ax2 = ax.twiny()
    # ax3 = ax.twinx()
    # ax2.plot(mus, D0s, marker='o', color="C1")
    # ax2.xaxis.set_inverted(True)
    # ax3.plot(ps, N0, marker='^', color="C2")
    # ax.set_xlabel(r"Hole doping $p$", color="C0")
    # ax.set_ylabel(r"Order parameter $|\Delta_d|$")
    # ax2.set_xlabel(r"Chemical potential $\mu$", color="C1")
    # ax3.set_ylabel(r"$N(0)$", color="C2")
    # #fig.savefig("gap-p.pdf")

    fig, ax = plt.subplots()
    pcm = ax.pcolormesh(klen, omegas, Akw, rasterized=True, cmap="viridis")
    ax.set_xticks([0.0, GX, GX + XM, GX + XM + MG], [r"$\Gamma$", r"$X$", r"$M$", r"$\Gamma$"])
    ax.set_xlabel(r"$k$")
    ax.set_ylabel(r"$\omega$")
    cb = fig.colorbar(pcm, ax=ax)
    cb.set_label(r"$A(k,\omega)$")
    #fig.savefig("spectrum-sc.pdf", dpi=512)

    fig, ax = plt.subplots()
    pcm = ax.pcolormesh(klen, omegas, A0kw, rasterized=True, cmap="viridis")
    ax.set_xticks([0.0, GX, GX + XM, GX + XM + MG], [r"$\Gamma$", r"$X$", r"$M$", r"$\Gamma$"])
    ax.set_xlabel(r"$k$")
    ax.set_ylabel(r"$\omega$")
    cb = fig.colorbar(pcm, ax=ax)
    cb.set_label(r"$A_0(k,\omega)$")
    #fig.savefig("spectrum-normal.pdf", dpi=512)

    fig, ax = plt.subplots()
    im = ax.imshow(Ak0, origin="lower", aspect="equal", extent=(kvec[0], kvec[-1], kvec[0], kvec[-1]), cmap="viridis")
    ax.axline((0.0, np.pi), (np.pi, 0.0), linestyle="--", color="white", linewidth=0.5)
    ax.set_xlim((kvec[0], kvec[-1]))
    ax.set_ylim((kvec[0], kvec[-1]))
    ax.set_xticks([kvec[0], kvec[-1]], ["0", r"$\pi$"])
    ax.set_yticks([kvec[0], kvec[-1]], ["0", r"$\pi$"])
    ax.set_xlabel(r"$k_x$")
    ax.set_ylabel(r"$k_y$")
    fig.colorbar(im, ax=ax)


    plt.show()


