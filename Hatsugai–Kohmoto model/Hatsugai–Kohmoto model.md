## Hatsugai–Kohmoto model （normal state）

$H_{\mathrm{HK}}=\sum_k H_k=\sum_k\left(\xi_k\left(n_{k \uparrow}+n_{k \downarrow}\right)+U n_{k \uparrow} n_{k \downarrow}\right)$

$H_{\mathrm{HK}}$ is decoupled in each momentum sector.

Eigenstates and eigenenergy:
$$
\begin{array}{ll}|0\rangle_k & E_0(k)=0 \\ |\uparrow\rangle_k=\hat{c}_{k \uparrow}^{\dagger}|0\rangle_k & E_u(k)=\varepsilon_k-\mu \\ |\downarrow\rangle_k=\hat{c}_{k \downarrow}^{\dagger}|0\rangle_k & E_n(k)=\varepsilon_k-\mu \\ |\uparrow \downarrow\rangle_k=\hat{c}_{k \uparrow}^{\dagger} \hat{c}_{k \downarrow}^{\dagger}|0\rangle_k & E_d(k)=2 \varepsilon_k-2 \mu+U \end{array}
$$
Partition function:
$$
\begin{aligned}
\mathcal{Z}=\operatorname{Tr} e^{-\beta \hat{H}}
&=\prod_k\sum_{\alpha_k=0, \uparrow, \downarrow, \uparrow \downarrow}\left\langle\left.\alpha_k\right| e^{-\beta \hat{H_k}} \mid \alpha_k\right\rangle\\
&=\prod_k\left(1+2 e^{-\beta\left(\varepsilon_k-\mu\right)}+e^{-\beta\left(2\varepsilon_k-2\mu+U\right)}\right)
\end{aligned}
$$
electron occupation

$n_{k \sigma}$ is the average occupation per spin

$\langle\uparrow\mid\hat{n}_{k \sigma}\mid\uparrow\rangle=\langle\downarrow\mid\hat{n}_{k \sigma}\mid\downarrow\rangle=1/2$

$\langle\uparrow\downarrow\mid\hat{n}_{k \sigma}\mid\uparrow\downarrow\rangle=1$
$$
\begin{aligned}
n_{k \sigma}
&=\frac{1}{\mathcal{Z}} \operatorname{Tr} \hat{n}_{k \sigma} e^{-\beta \hat{H}}\\
&=\frac{\sum_{\alpha_k=0, \uparrow, \downarrow, \uparrow \downarrow}\left\langle\left.\alpha_k\right| \hat{n}_{k \sigma}e^{-\beta \hat{H_k}} \mid \alpha_k\right\rangle}{1+2 e^{-\beta\left(\varepsilon_k-\mu\right)}+e^{-\beta\left(2\varepsilon_k-2\mu+U\right)}}\\
&=\frac{e^{-\beta\left(\varepsilon_k-\mu\right)}+e^{-\beta\left(2 \varepsilon_k-2 \mu+U\right)}}{1+2 e^{-\beta\left(\varepsilon_k-\mu\right)}+e^{-\beta\left(2\varepsilon_k-2\mu+U\right)}}
\end{aligned}
$$

### Spectrum

Single electron excitation:
$$
A^{+}(k, \omega)=\frac{1}{Z} \sum_{m, n} e^{-\beta E_m}|\langle n| c_k^{\dagger}| m\rangle|^ 2 \delta\left(\omega-\left(E_n-E_m\right)\right)
$$
Single hole excitation:
$$
A^{-}(k, \omega)=\frac{1}{Z} \sum_{m, n} e^{-\beta E_m}|\langle n| c_k| m\rangle|^ 2 \delta\left(\omega+\left(E_n-E_m\right)\right)
$$

$$
A(k, \omega)=\frac{1}{\mathcal{Z}} \sum_{m, n}(e^{-\beta E_m}+e^{-\beta E_n})|\langle m| c_k| n\rangle|^ 2 \delta\left(\omega+E_m-E_n\right)
$$

spectral function of HK model (derivation in appendix 1):
$$
A_\sigma(k,\omega)
=
\frac{1+e^{-\beta\xi_k}}{Z_k}\delta(\omega-\xi_k)
+
\frac{e^{-\beta\xi_k}+e^{-\beta(2\xi_k+U)}}{Z_k}
\delta(\omega-\xi_k-U)
$$



## Superconducting spectrum (mean-field)

Superconducting mean-field Hamiltonian:
$$
H^{M F}=\sum_k \xi_k\left(n_{k \uparrow}+n_{k \downarrow}\right)+U n_{k \uparrow} n_{k \downarrow}+\Delta^* b_k+\Delta b_k^{\dagger}
$$
with $\Delta=-\frac{g}{L^d} \sum_k\left\langle b_k\right\rangle$, $b_k^{\dagger} = c^{\dagger}_{k \uparrow}c^{\dagger}_{-k\downarrow}$.

While the Hamiltonian no longer separates completely in k-space, each k couples only to −k：
$$
H^{M F}=\sum_{k>0} H_k^{M F}
$$

$$
\begin{aligned}
H_k^{M F}= & \xi_k\left(n_{k \uparrow}+n_{k \downarrow}+n_{-k \uparrow}+n_{-k \downarrow}\right) \\
& +U\left(n_{k \uparrow} n_{k \downarrow}+n_{-k \uparrow} n_{-k \downarrow}\right) \\
& +\Delta^*\left(b_k+b_{-k}\right)+\Delta\left(b_k^{\dagger}+b_{-k}^{\dagger}\right)
\end{aligned}
$$

#### Block Diagonalization of the Mean-Field HK Hamiltonian

For each $(k,-k)$ sector there are four fermionic modes:

$$
k\uparrow,\quad k\downarrow,\quad -k\uparrow,\quad -k\downarrow.
$$

Therefore the Hilbert space dimension is

$$
2^4=16.
$$

One may use the occupation basis

$$
|n_{k\uparrow},n_{k\downarrow},n_{-k\uparrow},n_{-k\downarrow}\rangle,
$$

with each occupation number equal to $0$ or $1$.

The mode ordering is fixed as

$$
(k\uparrow,\ k\downarrow,\ -k\uparrow,\ -k\downarrow).
$$

Define

$$
s_z=N_\uparrow-N_\downarrow,
$$

where

$$
N_\uparrow=n_{k\uparrow}+n_{-k\uparrow},
\qquad
N_\downarrow=n_{k\downarrow}+n_{-k\downarrow}.
$$

The mean-field Hamiltonian is

$$
H_k^{\rm MF}
=
\xi_k N
+
U(n_{k\uparrow}n_{k\downarrow}
+n_{-k\uparrow}n_{-k\downarrow})
+
\Delta^*(b_k+b_{-k})
+
\Delta(b_k^\dagger+b_{-k}^\dagger),
$$

with

$$
b_k=c_{-k\downarrow}c_{k\uparrow},
\qquad
b_{-k}=c_{k\downarrow}c_{-k\uparrow}.
$$

The pairing term creates or annihilates one up electron and one down electron. Therefore $s_z=N_\uparrow-N_\downarrow$ is conserved. Since each Cooper pair has total momentum zero, the total momentum inside the $(k,-k)$ sector is also conserved.

For generic $k$, the full Hamiltonian decomposes as

$$
H_k^{\rm MF}
=
H_{s_z=2}
\oplus
H_{s_z=1}
\oplus
H_{s_z=0}
\oplus
H_{s_z=-1}
\oplus
H_{s_z=-2}.
$$

#### The $s_z=2$ Block

The only basis state is

$$
|1,0,1,0\rangle .
$$

There are two up electrons and no down electrons. The pairing term vanishes, and there is no HK double occupancy. Therefore

$$
H_{s_z=2}
=
\begin{pmatrix}
2\xi_k
\end{pmatrix}.
$$

#### The $s_z=-2$ Block

The only basis state is

$$
|0,1,0,1\rangle .
$$

There are two down electrons and no up electrons. Again, the pairing term vanishes and there is no HK double occupancy. Therefore

$$
H_{s_z=-2}
=
\begin{pmatrix}
2\xi_k
\end{pmatrix}.
$$

#### The $s_z=1$ Block

Use the ordered basis

$$
|1,0,0,0\rangle,
\quad
|0,0,1,0\rangle,
\quad
|1,1,1,0\rangle,
\quad
|1,0,1,1\rangle .
$$

In this basis,

$$
H_{s_z=1}
=
\begin{pmatrix}
\xi_k & 0 & -\Delta^* & 0\\
0 & \xi_k & 0 & -\Delta^*\\
-\Delta & 0 & 3\xi_k+U & 0\\
0 & -\Delta & 0 & 3\xi_k+U
\end{pmatrix}.
$$

The block further decomposes into two identical $2\times2$ blocks. The two ordered bases are

$$
\{|1,0,0,0\rangle,\ |1,1,1,0\rangle\},
\qquad
\{|0,0,1,0\rangle,\ |1,0,1,1\rangle\}.
$$

$$
H_{s_z=1}=h_1\oplus h_1,
$$

where

$$
h_1
=
\begin{pmatrix}
\xi_k & -\Delta^*\\
-\Delta & 3\xi_k+U
\end{pmatrix}.
$$

The reason is momentum conservation. The pair operators create zero-momentum pairs, so an unpaired fermion with momentum $k$ cannot be converted into an unpaired fermion with momentum $-k$.

#### The $s_z=-1$ Block

Use the ordered basis

$$
|0,1,0,0\rangle,
\quad
|0,0,0,1\rangle,
\quad
|1,1,0,1\rangle,
\quad
|0,1,1,1\rangle .
$$

The structure is the same as the $s_z=1$ block. The two ordered $2\times2$ bases are

$$
\{|0,1,0,0\rangle,\ |1,1,0,1\rangle\},
\qquad
\{|0,0,0,1\rangle,\ |0,1,1,1\rangle\}.
$$

Therefore

$$
H_{s_z=-1}=h_1\oplus h_1,
$$

with

$$
h_1
=
\begin{pmatrix}
\xi_k & -\Delta^*\\
-\Delta & 3\xi_k+U
\end{pmatrix}.
$$

#### The $s_z=0$ Block

Use the ordered basis

$$
|0,0,0,0\rangle,
\quad
|1,0,0,1\rangle,
\quad
|0,1,1,0\rangle,
\quad
|1,1,1,1\rangle,
\quad
|1,1,0,0\rangle,
\quad
|0,0,1,1\rangle .
$$

The first four states have total momentum zero and are coupled by the pairing term. The last two states are isolated doublon states:

$$
|1,1,0,0\rangle,
\qquad
|0,0,1,1\rangle .
$$

They have total momenta $2k$ and $-2k$, respectively, and cannot be coupled by zero-momentum pairing.

Therefore

$$
H_{s_z=0}
=
H_{s_z=0}^{(4)}
\oplus
(2\xi_k+U)
\oplus
(2\xi_k+U),
$$

where the ordered basis of $H_{s_z=0}^{(4)}$ is

$$
\{|0,0,0,0\rangle,\ |1,0,0,1\rangle,\ |0,1,1,0\rangle,\ |1,1,1,1\rangle\}.
$$

In this basis,

$$
H_{s_z=0}^{(4)}
=
\begin{pmatrix}
0 & \Delta^* & -\Delta^* & 0\\
\Delta & 2\xi_k & 0 & -\Delta^*\\
-\Delta & 0 & 2\xi_k & \Delta^*\\
0 & -\Delta & \Delta & 4\xi_k+2U
\end{pmatrix}.
$$

The relative minus signs come from the fermionic ordering convention. With the mode order

$$
(k\uparrow,\ k\downarrow,\ -k\uparrow,\ -k\downarrow),
$$

define

$$
a=c_{k\uparrow},
\qquad
b=c_{k\downarrow},
\qquad
c=c_{-k\uparrow},
\qquad
d=c_{-k\downarrow}.
$$

The ordered basis states in $H_{s_z=0}^{(4)}$ are therefore

$$
|1\rangle=|0,0,0,0\rangle=|0\rangle,
$$

$$
|2\rangle=|1,0,0,1\rangle=a^\dagger d^\dagger|0\rangle,
$$

$$
|3\rangle=|0,1,1,0\rangle=b^\dagger c^\dagger|0\rangle,
$$

$$
|4\rangle=|1,1,1,1\rangle=a^\dagger b^\dagger c^\dagger d^\dagger|0\rangle.
$$

The pair-annihilation operator is

$$
b_k+b_{-k}=da+bc.
$$

For the first row, the relevant matrix elements are

$$
\langle 1|\Delta^*(da+bc)|2\rangle
=
\Delta^*\langle 0|da\,a^\dagger d^\dagger|0\rangle
=
\Delta^*,
$$

whereas

$$
\langle 1|\Delta^*(da+bc)|3\rangle
=
\Delta^*\langle 0|bc\,b^\dagger c^\dagger|0\rangle
=
-\Delta^*.
$$

The second sign is negative because

$$
c\,b^\dagger c^\dagger|0\rangle
=
-b^\dagger|0\rangle,
\qquad
b(-b^\dagger|0\rangle)=-|0\rangle.
$$

This is why the $(1,3)$ matrix element is $-\Delta^*$.

#### Full Block-Diagonal Form

Combining all sectors, the full $16$-dimensional Hamiltonian is

$$
\boxed{
H_k^{\rm MF}
=
(2\xi_k)
\oplus
(h_1\oplus h_1)
\oplus
\left[
H_{s_z=0}^{(4)}
\oplus
(2\xi_k+U)
\oplus
(2\xi_k+U)
\right]
\oplus
(h_1\oplus h_1)
\oplus
(2\xi_k)
}
$$

with

$$
h_1
=
\begin{pmatrix}
\xi_k & -\Delta^*\\
-\Delta & 3\xi_k+U
\end{pmatrix}.
$$

The off-diagonal signs depend on the fermionic ordering convention. Here the ordering is fixed as

$$
(k\uparrow,\ k\downarrow,\ -k\uparrow,\ -k\downarrow).
$$

Changing the phase of individual basis states can move minus signs between matrix elements, but the eigenvalues and spectral functions are unchanged.

### Superconducting gap equation

$$
\Delta
=
-\frac{g}{N}
\sum_{k>0}
\left\langle b_k+b_{-k}\right\rangle.
$$

### Superfluid stiffness

$$
\begin{aligned}
\frac{D_s}{\pi}

&=\frac{1}{L^d}\left(\left\langle K_{x x}\right\rangle-\int_0^\beta d \tau\left\langle J_x(\tau) J_x\right\rangle\right)\\

&=\frac{1}{L^d}\left(\sum_{k \sigma} \frac{\partial^2 \epsilon_k}{\partial k_x^2} c_{k \sigma}^{\dagger} c_{k \sigma}-\sum_{n m}|\langle n| J_x| m\rangle|^ 2 \frac{\rho_m-\rho_n}{E_n-E_m}\right)

\end{aligned}
$$

$$
J_x=\sum_{k \sigma} \frac{\partial \epsilon_k}{\partial k_x} c_{k \sigma}^{\dagger} c_{k \sigma}
$$





---

### Appendix 1

#### Electron-Addition Part

Fix the spin index $\sigma$, and denote the opposite spin by $\bar\sigma$. The four states in the fixed $k$ sector may be written as

$$
|0\rangle,\quad |\sigma\rangle,\quad |\bar\sigma\rangle,\quad |\uparrow\downarrow\rangle.
$$

For $A^+_\sigma(k,\omega)$, we substitute these states into

$$
\langle n|c_{k\sigma}^\dagger|m\rangle,
\qquad
m,n\in\{0,\sigma,\bar\sigma,\uparrow\downarrow\}.
$$

The action of $c_{k\sigma}^\dagger$ on the four possible initial states $|m\rangle$ is

$$
\begin{array}{ccl}
c_{k\sigma}^\dagger|0\rangle &=& |\sigma\rangle,\\[4pt]
c_{k\sigma}^\dagger|\sigma\rangle &=& 0,\\[4pt]
c_{k\sigma}^\dagger|\bar\sigma\rangle &=& \pm|\uparrow\downarrow\rangle,\\[4pt]
c_{k\sigma}^\dagger|\uparrow\downarrow\rangle &=& 0.
\end{array}
$$

The sign in the third line depends on the fermionic ordering convention, but it drops out after taking the absolute square.

Therefore, in the electron-addition sum, only two matrix elements are nonzero:

$$
\left|\langle \sigma|c_{k\sigma}^\dagger|0\rangle\right|^2=1,
$$

and

$$
\left|\langle \uparrow\downarrow|c_{k\sigma}^\dagger|\bar\sigma\rangle\right|^2=1.
$$

All other combinations of $m$ and $n$ give zero. Hence

$$
A^+_\sigma(k,\omega)
=
\frac{1}{Z_k}
e^{-\beta E_0}
\left|\langle \sigma|c_{k\sigma}^\dagger|0\rangle\right|^2
\delta\left(\omega-(E_\sigma-E_0)\right)
$$

$$
\quad
+
\frac{1}{Z_k}
e^{-\beta E_{\bar\sigma}}
\left|\langle \uparrow\downarrow|c_{k\sigma}^\dagger|\bar\sigma\rangle\right|^2
\delta\left(\omega-(E_{\uparrow\downarrow}-E_{\bar\sigma})\right).
$$

Using $E_0=0$, $E_\sigma=E_{\bar\sigma}=\xi_k$, and $E_{\uparrow\downarrow}=2\xi_k+U$, this gives

$$
A^+_\sigma(k,\omega)
=
\frac{1}{Z_k}\delta(\omega-\xi_k)
+
\frac{e^{-\beta\xi_k}}{Z_k}\delta(\omega-\xi_k-U).
$$

#### Hole-Removal Part

For $A^-_\sigma(k,\omega)$, we substitute the four states into

$$
\langle n|c_{k\sigma}|m\rangle,
\qquad
m,n\in\{0,\sigma,\bar\sigma,\uparrow\downarrow\}.
$$

The action of $c_{k\sigma}$ on the four possible initial states $|m\rangle$ is

$$
\begin{array}{ccl}
c_{k\sigma}|0\rangle &=& 0,\\[4pt]
c_{k\sigma}|\sigma\rangle &=& |0\rangle,\\[4pt]
c_{k\sigma}|\bar\sigma\rangle &=& 0,\\[4pt]
c_{k\sigma}|\uparrow\downarrow\rangle &=& \pm|\bar\sigma\rangle.
\end{array}
$$

Therefore, in the hole-removal sum, only two matrix elements are nonzero:

$$
\left|\langle 0|c_{k\sigma}|\sigma\rangle\right|^2=1,
$$

and

$$
\left|\langle \bar\sigma|c_{k\sigma}|\uparrow\downarrow\rangle\right|^2=1.
$$

Thus

$$
A^-_\sigma(k,\omega)
=
\frac{1}{Z_k}
e^{-\beta E_\sigma}
\left|\langle 0|c_{k\sigma}|\sigma\rangle\right|^2
\delta\left(\omega+(E_0-E_\sigma)\right)
$$

$$
\quad
+
\frac{1}{Z_k}
e^{-\beta E_{\uparrow\downarrow}}
\left|\langle \bar\sigma|c_{k\sigma}|\uparrow\downarrow\rangle\right|^2
\delta\left(\omega+(E_{\bar\sigma}-E_{\uparrow\downarrow})\right).
$$

Using the eigen-energies, this becomes

$$
A^-_\sigma(k,\omega)
=
\frac{e^{-\beta\xi_k}}{Z_k}\delta(\omega-\xi_k)
+
\frac{e^{-\beta(2\xi_k+U)}}{Z_k}\delta(\omega-\xi_k-U).
$$

#### Final Result

Adding the electron-addition and hole-removal parts gives

$$
A_\sigma(k,\omega)
=A^+_\sigma(k,\omega)+A^-_\sigma(k,\omega)
$$

$$
=
\frac{1+e^{-\beta\xi_k}}{Z_k}\delta(\omega-\xi_k)
+
\frac{e^{-\beta\xi_k}+e^{-\beta(2\xi_k+U)}}{Z_k}
\delta(\omega-\xi_k-U),
$$

with

$$
Z_k=1+2e^{-\beta\xi_k}+e^{-\beta(2\xi_k+U)}.
$$

Thus the spectral function consists of two delta-function peaks:

$$
\omega=\xi_k,
\qquad
\omega=\xi_k+U.
$$

The peak at $\omega=\xi_k$ receives contributions from adding a $\sigma$-electron to $|0\rangle$ and from removing a $\sigma$-electron from $|\sigma\rangle$. The peak at $\omega=\xi_k+U$ receives contributions from adding a $\sigma$-electron to $|\bar\sigma\rangle$ and from removing a $\sigma$-electron from $|\uparrow\downarrow\rangle$. The interaction $U$ therefore produces the second, shifted spectral line.