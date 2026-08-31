[toc]

## Fermi arc model (normal state)

Fermi arc model Hamiltonian:
$$
\hat{H}_0=\sum_{\mathbf{k} \sigma}\left(\xi_{\mathbf{k}} \hat{n}_{\mathbf{k} \sigma}+\frac{U}{2} \hat{n}_{\mathbf{k} \sigma} \hat{n}_{\mathbf{k}+\mathbf{Q} \bar{\sigma}}\right)
$$
$\mathbf{Q}=(\pi, \pi)$

Half BZ:
$$
\begin{gathered}
\hat{H}_0=\sum_{\mathbf{k} \in \mathrm{Half-BZ}}\left[\xi_{\mathbf{k}}\left(n_{\mathbf{k} \uparrow}+n_{\mathbf{k} \downarrow}\right)+\xi_{\mathbf{k}+\mathbf{Q}}\left(n_{\mathbf{k}+\mathbf{Q}, \uparrow}+n_{\mathbf{k}+\mathbf{Q}, \downarrow}\right)\right. \\
\left.+U n_{\mathbf{k} \uparrow} n_{\mathbf{k}+\mathbf{Q}, \downarrow}+U n_{\mathbf{k} \downarrow} n_{\mathbf{k}+\mathbf{Q}, \uparrow}\right] .
\end{gathered}
$$
Eigenstates and eigenenergy:
$$
\begin{array}{lll}
|0,0\rangle, & E_0 = 0, \\
|1,0\rangle = c_{\mathbf{k}\sigma}^\dagger |0\rangle, & E_1 = \xi_{\mathbf{k}}, \\
|0,1\rangle = c_{\mathbf{k}+\mathbf{Q},-\sigma}^\dagger |0\rangle, & E_2 = \xi_{\mathbf{k}+\mathbf{Q}}, \\
|1,1\rangle = c_{\mathbf{k}\sigma}^\dagger c_{\mathbf{k}+\mathbf{Q},-\sigma}^\dagger |0\rangle, & E_3 = \xi_{\mathbf{k}} + \xi_{\mathbf{k}+\mathbf{Q}} + U
\end{array}
$$
partition function:
$$
Z_{\mathbf{k}}=1+e^{-\beta \xi_{\mathbf{k}}}+e^{-\beta \xi_{\mathbf{k}+\mathbf{Q}}}+e^{-\beta\left(\xi_{\mathbf{k}}+\xi_{\mathbf{k}+\mathbf{Q}}+U\right)}
$$

$$
\langle n_{\mathbf{k}+\mathbf Q,-\sigma}\rangle
=
\frac{
e^{-\beta \xi_{\mathbf{k}+\mathbf Q}}
+
e^{-\beta(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U)}
}{
1
+
e^{-\beta \xi_{\mathbf k}}
+
e^{-\beta \xi_{\mathbf{k}+\mathbf Q}}
+
e^{-\beta(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U)}
}.
$$

Spectral function (derivation in Appendix 1):
$$
A(\mathbf{k}, \omega)=\left(1-n_{\mathbf{k}+\mathbf{Q}}\right) \delta\left(\omega-\xi_{\mathbf{k}}\right)+n_{\mathbf{k}+\mathbf{Q}} \delta\left(\omega-\xi_{\mathbf{k}}-U\right)
$$

## Superconducting spectrum (mean-field)

Mean-field Hamiltonian:
$$
H_{\mathrm{SC}}^{\mathrm{MF}}=\sum_{\mathbf{k} \in \Omega_{1 / 4}} H_{\mathbf{k}}^{\mathrm{MF}}
$$

$$
H_{\mathrm{k}}^{\mathrm{MF}}=H_{\mathrm{kin}}+H_U+H_{\Delta}
$$

$$
H_{\mathrm{kin}}=\sum_\sigma\left[\xi_{\mathbf{k}} n_{\mathbf{k} \sigma}+\xi_{\mathbf{k}+\mathbf{Q}} n_{\mathbf{k}+\mathbf{Q}, \sigma}+\xi_{-\mathbf{k}} n_{-\mathbf{k} \sigma}+\xi_{-\mathbf{k}-\mathbf{Q}} n_{-\mathbf{k}-\mathbf{Q}, \sigma}\right]
$$

$$
\begin{aligned}
& H_U=U n_{\mathbf{k} \uparrow} n_{\mathbf{k}+\mathbf{Q}, \downarrow}+U n_{\mathbf{k} \downarrow} n_{\mathbf{k}+\mathbf{Q}, \uparrow} \\
& +U n_{-\mathbf{k} \uparrow} n_{-\mathbf{k}-\mathbf{Q}, \downarrow}+U n_{-\mathbf{k} \downarrow} n_{-\mathbf{k}-\mathbf{Q}, \uparrow}
\end{aligned}
$$

derivation of $H_\Delta$ in Appendix 2
$$
\begin{aligned}
H_{\Delta}
= & \Delta_{\mathbf{k}}^*\left(c_{-\mathbf{k} \downarrow} c_{\mathbf{k} \uparrow}+c_{\mathbf{k} \downarrow} c_{-\mathbf{k} \uparrow}\right)+\Delta_{\mathbf{k}}(c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger}+c_{-\mathbf{k} \uparrow}^{\dagger} c_{\mathbf{k} \downarrow}^{\dagger}) \\
& -\Delta_{\mathbf{k}}^*\left(c_{-\mathbf{k}-\mathbf{Q}, \downarrow} c_{\mathbf{k}+\mathbf{Q}, \uparrow}+c_{\mathbf{k}+\mathbf{Q}, \downarrow} c_{-\mathbf{k}-\mathbf{Q}, \uparrow}\right) \\
& -\Delta_{\mathbf{k}}(c_{\mathbf{k}+\mathbf{Q}, \uparrow}^{\dagger} c_{-\mathbf{k}-\mathbf{Q}, \downarrow}^{\dagger}+c_{-\mathbf{k}-\mathbf{Q}, \uparrow}^{\dagger} c_{\mathbf{k}+\mathbf{Q}, \downarrow}^{\dagger}) 
\end{aligned}
$$

$$
\Delta_{\mathbf{k}}=\Delta_0\left(\cos k_x-\cos k_y\right)
$$

$$
\Delta_0=-\frac{J}{N} \sum_{\mathbf{k}} g_{\mathbf{k}}\langle c_{-\mathbf k\downarrow} c_{\mathbf k\uparrow}\rangle
$$

This mean-field Hamiltonian is decoupled in:
$$
\mathcal{H}_{\mathbf{k}}=\mathcal{H}_{\mathcal{A}} \otimes \mathcal{H}_{\mathcal{B}},
$$

$$
\begin{array}{ll}
\mathcal{A}: & (\mathbf{k} \uparrow, \mathbf{k}+\mathbf{Q} \downarrow,-\mathbf{k} \downarrow,-\mathbf{k}-\mathbf{Q} \uparrow), \\
\mathcal{B}: & (\mathbf{k} \downarrow, \mathbf{k}+\mathbf{Q} \uparrow,-\mathbf{k} \uparrow,-\mathbf{k}-\mathbf{Q} \downarrow) .
\end{array}
$$

### Block Diagonalization

Define the four fermion operators

$$
a=c_{\mathbf k\uparrow},
\qquad
b=c_{\mathbf{k}+\mathbf Q,\downarrow},
\qquad
c=c_{-\mathbf k\downarrow},
\qquad
d=c_{-\mathbf k-\mathbf Q,\uparrow}.
$$

Use the fixed mode ordering

$$
(a,b,c,d)
=
\left(
\mathbf k\uparrow,\ 
\mathbf{k}+\mathbf Q\downarrow,\ 
-\mathbf k\downarrow,\ 
-\mathbf k-\mathbf Q\uparrow
\right).
$$

The occupation basis is

$$
|n_a,n_b,n_c,n_d\rangle .
$$

Assume inversion symmetry of the dispersion:

$$
\xi_{-\mathbf k}=\xi_{\mathbf k},
\qquad
\xi_{-\mathbf k-\mathbf Q}=\xi_{\mathbf{k}+\mathbf Q}.
$$

The Hamiltonian in sector $\mathcal A$ is

$$
H_{\mathcal A}
=
\xi_{\mathbf k}(n_a+n_c)
+
\xi_{\mathbf{k}+\mathbf Q}(n_b+n_d)
+
U(n_an_b+n_cn_d)
+
H_\Delta .
$$

For a $d$-wave singlet order parameter,

$$
\Delta_{\mathbf k}
=
\Delta_0(\cos k_x-\cos k_y),
$$

one has

$$
\begin{aligned}
\Delta_{-\mathbf k}&=\Delta_{\mathbf k},\\
\Delta_{\mathbf{k}+\mathbf Q}&=-\Delta_{\mathbf k}.
\end{aligned}
$$

Therefore

$$
\Delta_{-\mathbf k-\mathbf Q}
=
\Delta_{\mathbf{k}+\mathbf Q}
=
-\Delta_{\mathbf k}.
$$

The pairing part in this sector may be written as

$$
H_\Delta
=
\Delta_{\mathbf k}^*ca+\Delta_{\mathbf k}a^\dagger c^\dagger
-
\Delta_{\mathbf k}^*bd
-
\Delta_{\mathbf k}d^\dagger b^\dagger .
$$

The signs in the matrix elements below follow from the fixed fermion ordering $(a,b,c,d)$.

### Conserved Quantity

Inside this four-mode sector, define

$$
S_z=n_a+n_d-n_b-n_c.
$$

The modes $a,d$ carry spin up, while the modes $b,c$ carry spin down. The pairing terms create or annihilate one up-spin fermion and one down-spin fermion. Therefore $S_z$ is conserved:

$$
[H_{\mathcal A},S_z]=0.
$$

Thus the $16$-dimensional Fock space decomposes into

$$
S_z=2,\ 1,\ 0,\ -1,\ -2
$$

subspaces.

### The $S_z=2$ Block

The ordered basis is

$$
|1,0,0,1\rangle .
$$

This state contains the two up-spin modes $a$ and $d$. The pairing terms vanish, and there is no interaction energy. Therefore

$$
H_{S_z=2}
=
\begin{pmatrix}
\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}
\end{pmatrix}.
$$

### The $S_z=-2$ Block

The ordered basis is

$$
|0,1,1,0\rangle .
$$

This state contains the two down-spin modes $b$ and $c$. Again, the pairing terms vanish and there is no interaction energy. Therefore

$$
H_{S_z=-2}
=
\begin{pmatrix}
\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}
\end{pmatrix}.
$$

Together these two one-dimensional blocks give a doubly degenerate energy

$$
E_4=\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}.
$$

### The $S_z=1$ Blocks

The four states with $S_z=1$ are

$$
|1,0,0,0\rangle,
\quad
|0,0,0,1\rangle,
\quad
|1,1,0,1\rangle,
\quad
|1,0,1,1\rangle .
$$

The pairing terms do not mix all four states at once. Instead, the block further decomposes into two $2\times2$ blocks.

First use the ordered basis

$$
\left\{
|1,0,0,0\rangle,\ 
|1,1,0,1\rangle
\right\}.
$$

In this basis,

$$
H_{S_z=1}^{(a)}
=
\begin{pmatrix}
\xi_{\mathbf k} & \Delta_{\mathbf k}^*\\
\Delta_{\mathbf k} & \xi_{\mathbf k}+2\xi_{\mathbf{k}+\mathbf Q}+U
\end{pmatrix}.
$$

Second use the ordered basis

$$
\left\{
|0,0,0,1\rangle,\ 
|1,0,1,1\rangle
\right\}.
$$

In this basis,

$$
H_{S_z=1}^{(d)}
=
\begin{pmatrix}
\xi_{\mathbf{k}+\mathbf Q} & \Delta_{\mathbf k}^*\\
\Delta_{\mathbf k} & 2\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U
\end{pmatrix}.
$$

Thus

$$
H_{S_z=1}
=
H_{S_z=1}^{(a)}\oplus H_{S_z=1}^{(d)}.
$$

### The $S_z=-1$ Blocks

The four states with $S_z=-1$ are

$$
|0,1,0,0\rangle,
\quad
|0,0,1,0\rangle,
\quad
|1,1,1,0\rangle,
\quad
|0,1,1,1\rangle .
$$

Again, the block decomposes into two $2\times2$ blocks.

With the ordered basis

$$
\left\{
|0,1,0,0\rangle,\ 
|1,1,1,0\rangle
\right\},
$$

one obtains

$$
H_{S_z=-1}^{(b)}
=
\begin{pmatrix}
\xi_{\mathbf{k}+\mathbf Q} & -\Delta_{\mathbf k}^*\\
-\Delta_{\mathbf k} & 2\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U
\end{pmatrix}.
$$

With the ordered basis

$$
\left\{
|0,0,1,0\rangle,\ 
|0,1,1,1\rangle
\right\},
$$

one obtains

$$
H_{S_z=-1}^{(c)}
=
\begin{pmatrix}
\xi_{\mathbf k} & -\Delta_{\mathbf k}^*\\
-\Delta_{\mathbf k} & \xi_{\mathbf k}+2\xi_{\mathbf{k}+\mathbf Q}+U
\end{pmatrix}.
$$

Therefore

$$
H_{S_z=-1}
=
H_{S_z=-1}^{(b)}\oplus H_{S_z=-1}^{(c)}.
$$

The two $2\times2$ matrices each appear twice in the full $16$-dimensional sector.

### The $S_z=0$ Block

The six states with $S_z=0$ are

$$
|0,0,0,0\rangle,
\quad
|1,0,1,0\rangle,
\quad
|0,1,0,1\rangle,
\quad
|1,1,1,1\rangle,
\quad
|1,1,0,0\rangle,
\quad
|0,0,1,1\rangle .
$$

The first four states have zero total spin imbalance and are connected by the pairing terms. The last two states are isolated because they contain either the interacting pair $(a,b)$ or the interacting pair $(c,d)$ without forming the superconducting pair states.

The ordered basis of the nontrivial $4\times4$ block is

$$
\left\{
|0,0,0,0\rangle,\ 
|1,0,1,0\rangle,\ 
|0,1,0,1\rangle,\ 
|1,1,1,1\rangle
\right\}.
$$

Equivalently,

$$
|1\rangle=|0,0,0,0\rangle,
$$

$$
|2\rangle=|1,0,1,0\rangle=a^\dagger c^\dagger|0\rangle,
$$

$$
|3\rangle=|0,1,0,1\rangle=b^\dagger d^\dagger|0\rangle,
$$

$$
|4\rangle=|1,1,1,1\rangle=a^\dagger b^\dagger c^\dagger d^\dagger|0\rangle.
$$

In this basis,

$$
H_{S_z=0}^{(4)}
=
\begin{pmatrix}
0 & \Delta_{\mathbf k}^* & \Delta_{\mathbf k}^* & 0\\
\Delta_{\mathbf k} & 2\xi_{\mathbf k} & 0 & -\Delta_{\mathbf k}^*\\
\Delta_{\mathbf k} & 0 & 2\xi_{\mathbf{k}+\mathbf Q} & -\Delta_{\mathbf k}^*\\
0 & -\Delta_{\mathbf k} & -\Delta_{\mathbf k} & 2(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U)
\end{pmatrix}.
$$

The two isolated states are

$$
|1,1,0,0\rangle=a^\dagger b^\dagger|0\rangle,
\qquad
|0,0,1,1\rangle=c^\dagger d^\dagger|0\rangle .
$$

Both have energy

$$
E_5=\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U.
$$

Thus

$$
H_{S_z=0}
=
H_{S_z=0}^{(4)}
\oplus
(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U)
\oplus
(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U).
$$

### Full Block-Diagonal Form of One Sector

Combining all $S_z$ sectors, the $16$-dimensional Hamiltonian of sector $\mathcal A$ is

$$
\boxed{
H_{\mathcal A}
=
(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q})
\oplus
\left(H_{S_z=1}^{(a)}\oplus H_{S_z=1}^{(d)}\right)
\oplus
\left[
H_{S_z=0}^{(4)}
\oplus
(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U)
\oplus
(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U)
\right]
\oplus
\left(H_{S_z=-1}^{(b)}\oplus H_{S_z=-1}^{(c)}\right)
\oplus
(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q})
}.
$$

The second four-mode sector $\mathcal B$ has the same block structure and the same eigenvalues. Therefore its contribution appears as a degeneracy factor rather than a separate diagonalization.













## Appendix 1

#### Spectral Function

Use the spectral-function definition

$$
A_\sigma(\mathbf k,\omega)
=
A_\sigma^+(\mathbf k,\omega)
+
A_\sigma^-(\mathbf k,\omega),
$$

with the electron-addition part

$$
A_\sigma^+(\mathbf k,\omega)
=
\frac{1}{Z_{\mathbf k}}
\sum_{m,n}
e^{-\beta E_m}
\left|
\langle n|c_{\mathbf k\sigma}^{\dagger}|m\rangle
\right|^2
\delta\left[\omega-(E_n-E_m)\right],
$$

and the electron-removal part

$$
A_\sigma^-(\mathbf k,\omega)
=
\frac{1}{Z_{\mathbf k}}
\sum_{m,n}
e^{-\beta E_m}
\left|
\langle n|c_{\mathbf k\sigma}|m\rangle
\right|^2
\delta\left[\omega+(E_n-E_m)\right].
$$

#### Electron-Addition Part

Substitute the eigenstates directly into

$$
\langle n|c_{\mathbf k\sigma}^{\dagger}|m\rangle .
$$

The nonzero actions are

$$
c_{\mathbf k\sigma}^{\dagger}|0,0\rangle
=
|1,0\rangle,
$$

and

$$
c_{\mathbf k\sigma}^{\dagger}|0,1\rangle
=
|1,1\rangle.
$$

All other actions vanish. Therefore

$$
A_\sigma^+(\mathbf k,\omega)
=
\frac{1}{Z_{\mathbf k}}
\delta(\omega-\xi_{\mathbf k})
+
\frac{
e^{-\beta\xi_{\mathbf{k}+\mathbf Q}}
}{
Z_{\mathbf k}
}
\delta(\omega-\xi_{\mathbf k}-U).
$$

Here we used

$$
E_1-E_0=\xi_{\mathbf k},
$$

and

$$
E_3-E_2=\xi_{\mathbf k}+U.
$$

#### Electron-Removal Part

Now substitute the eigenstates into

$$
\langle n|c_{\mathbf k\sigma}|m\rangle .
$$

The nonzero actions are

$$
c_{\mathbf k\sigma}|1,0\rangle
=
|0,0\rangle,
$$

and

$$
c_{\mathbf k\sigma}|1,1\rangle
=
\pm |0,1\rangle.
$$

The sign depends on the fermionic ordering convention, but it drops out after taking the absolute square. Hence

$$
A_\sigma^-(\mathbf k,\omega)
=
\frac{
e^{-\beta\xi_{\mathbf k}}
}{
Z_{\mathbf k}
}
\delta(\omega-\xi_{\mathbf k})
+
\frac{
e^{-\beta(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U)}
}{
Z_{\mathbf k}
}
\delta(\omega-\xi_{\mathbf k}-U).
$$

Here we used

$$
E_0-E_1=-\xi_{\mathbf k},
$$

so

$$
\delta[\omega+(E_0-E_1)]
=
\delta(\omega-\xi_{\mathbf k}),
$$

and

$$
E_2-E_3=-(\xi_{\mathbf k}+U),
$$

so

$$
\delta[\omega+(E_2-E_3)]
=
\delta(\omega-\xi_{\mathbf k}-U).
$$

#### Final Result

Adding $A_\sigma^+$ and $A_\sigma^-$ gives

$$
A_\sigma(\mathbf k,\omega)
=
\frac{
1+e^{-\beta\xi_{\mathbf k}}
}{
Z_{\mathbf k}
}
\delta(\omega-\xi_{\mathbf k})
+
\frac{
e^{-\beta\xi_{\mathbf{k}+\mathbf Q}}
+
e^{-\beta(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U)}
}{
Z_{\mathbf k}
}
\delta(\omega-\xi_{\mathbf k}-U).
$$

Using

$$
n_{\mathbf{k}+\mathbf Q}
=
\frac{
e^{-\beta\xi_{\mathbf{k}+\mathbf Q}}
+
e^{-\beta(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U)}
}{
Z_{\mathbf k}
},
$$

and

$$
1-n_{\mathbf{k}+\mathbf Q}
=
\frac{
1+e^{-\beta\xi_{\mathbf k}}
}{
Z_{\mathbf k}
},
$$

the spectral function becomes

$$
\boxed{
A_\sigma(\mathbf k,\omega)
=
\left(1-n_{\mathbf{k}+\mathbf Q}\right)
\delta(\omega-\xi_{\mathbf k})
+
n_{\mathbf{k}+\mathbf Q}
\delta(\omega-\xi_{\mathbf k}-U)
}.
$$

The first peak corresponds to adding or removing a $\mathbf k\sigma$ electron when the partner mode $\mathbf{k}+\mathbf Q,-\sigma$ is empty. The second peak corresponds to the same excitation when the partner mode is occupied, which costs the additional interaction energy $U$.



## Appendix 2

$$
\begin{aligned}
H_{\Delta}

=&\Delta_{\mathbf{k}}^* c_{-\mathbf{k} \downarrow} c_{\mathbf{k} \uparrow}+\Delta_{\mathbf{k}} c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger} 
+\Delta_{-\mathbf{k}}^* c_{\mathbf{k} \downarrow} c_{-\mathbf{k} \uparrow}+\Delta_{-\mathbf{k}} c_{-\mathbf{k} \uparrow}^{\dagger} c_{\mathbf{k} \downarrow}^{\dagger} \\

&+\Delta_{\mathbf{k}+\mathbf{Q}}^* c_{-\mathbf{k}-\mathbf{Q}, \downarrow} c_{\mathbf{k}+\mathbf{Q}, \uparrow}+\Delta_{\mathbf{k}+\mathbf{Q}} c_{\mathbf{k}+\mathbf{Q}, \uparrow}^{\dagger} c_{-\mathbf{k}-\mathbf{Q}, \downarrow}^{\dagger} \\

&+\Delta_{-\mathbf{k}-\mathbf{Q}}^* c_{\mathbf{k}+\mathbf{Q}, \downarrow} c_{-\mathbf{k}-\mathbf{Q}, \uparrow}+\Delta_{-\mathbf{k}-\mathbf{Q}} c_{-\mathbf{k}-\mathbf{Q}, \uparrow}^{\dagger} c_{\mathbf{k}+\mathbf{Q}, \downarrow}^{\dagger}\\

= & \Delta_{\mathbf{k}}^*\left(c_{-\mathbf{k} \downarrow} c_{\mathbf{k} \uparrow}+c_{\mathbf{k} \downarrow} c_{-\mathbf{k} \uparrow}\right)+\Delta_{\mathbf{k}}\left(c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger}+c_{-\mathbf{k} \uparrow}^{\dagger} c_{\mathbf{k} \downarrow}^{\dagger}\right) \\
& -\Delta_{\mathbf{k}}^*\left(c_{-\mathbf{k}-\mathbf{Q}, \downarrow} c_{\mathbf{k}+\mathbf{Q}, \uparrow}+c_{\mathbf{k}+\mathbf{Q}, \downarrow} c_{-\mathbf{k}-\mathbf{Q}, \uparrow}\right) \\
& -\Delta_{\mathbf{k}}\left(c_{\mathbf{k}+\mathbf{Q}, \uparrow}^{\dagger} c_{-\mathbf{k}-\mathbf{Q}, \downarrow}^{\dagger}+c_{-\mathbf{k}-\mathbf{Q}, \uparrow}^{\dagger} c_{\mathbf{k}+\mathbf{Q}, \downarrow}^{\dagger}\right) .
\end{aligned}
$$

$$
\begin{aligned}
\Delta_{-\mathrm{k}} & =\Delta_{\mathrm{k}}, \\
\Delta_{\mathrm{k}+\mathrm{Q}} & =-\Delta_{\mathrm{k}}\\
\Delta_{-\mathrm{k}-\mathrm{Q}} & =-\Delta_{\mathrm{k}}
\end{aligned}
$$

## Appendix 3

#### Sign of the $(1,3)$ Matrix Element in the $S_z=0$ Block

This note explains why the $(1,3)$ matrix element in the $S_z=0$ four-dimensional block is positive after using the $d$-wave relation

$$
\Delta_{-\mathbf k-\mathbf Q}=-\Delta_{\mathbf k}.
$$

Consider the four-mode sector

$$
(a,b,c,d)
=
\left(
\mathbf k\uparrow,\ 
\mathbf{k}+\mathbf Q\downarrow,\ 
-\mathbf k\downarrow,\ 
-\mathbf k-\mathbf Q\uparrow
\right),
$$

with fixed fermion ordering

$$
(a,b,c,d).
$$

The nontrivial $S_z=0$ basis is

$$
|1\rangle=|0,0,0,0\rangle=|0\rangle,
$$

$$
|2\rangle=|1,0,1,0\rangle=a^\dagger c^\dagger|0\rangle,
$$

$$
|3\rangle=|0,1,0,1\rangle=b^\dagger d^\dagger|0\rangle,
$$

$$
|4\rangle=|1,1,1,1\rangle
=
a^\dagger b^\dagger c^\dagger d^\dagger|0\rangle.
$$

The pair-annihilation part of the mean-field Hamiltonian is

$$
H_\Delta^{\mathrm{ann}}
=
\Delta_{\mathbf k}^*ca
+
\Delta_{-\mathbf k-\mathbf Q}^*bd.
$$

For a $d$-wave gap,

$$
\Delta_{-\mathbf k-\mathbf Q}
=
-\Delta_{\mathbf k},
$$

so

$$
H_\Delta^{\mathrm{ann}}
=
\Delta_{\mathbf k}^*ca
-
\Delta_{\mathbf k}^*bd.
$$

Now consider the matrix element in the first row and third column:

$$
\langle 1|H_\Delta|3\rangle
=
\langle 0|H_\Delta b^\dagger d^\dagger|0\rangle .
$$

Only the $bd$ term contributes:

$$
\langle 1|H_\Delta|3\rangle
=
-\Delta_{\mathbf k}^*
\langle 0|bd\,b^\dagger d^\dagger|0\rangle .
$$

Using the fermionic anticommutation relations, first move $d$ through $b^\dagger$:

$$
d b^\dagger d^\dagger|0\rangle
=
-b^\dagger d d^\dagger|0\rangle
=
-b^\dagger|0\rangle .
$$

Then act with $b$:

$$
b(-b^\dagger|0\rangle)
=
-|0\rangle .
$$

Therefore

$$
bd\,b^\dagger d^\dagger|0\rangle
=
-|0\rangle ,
$$

and hence

$$
\langle 0|bd\,b^\dagger d^\dagger|0\rangle
=
-1.
$$

Thus

$$
\langle 1|H_\Delta|3\rangle
=
(-\Delta_{\mathbf k}^*)(-1)
=
\Delta_{\mathbf k}^*.
$$

The positive sign therefore comes from the cancellation of two minus signs:

$$
\boxed{
\text{d-wave sign change}
\times
\text{fermionic reordering sign}
=
(-1)\times(-1)=+1.
}
$$

By contrast, if the pairing were $s$-wave so that

$$
\Delta_{-\mathbf k-\mathbf Q}=\Delta_{\mathbf k},
$$

then the same fermionic reordering sign would give

$$
\langle 1|H_\Delta|3\rangle
=
-\Delta_{\mathbf k}^*.
$$

Thus the positive $(1,3)$ matrix element is a direct consequence of the $d$-wave sign reversal under $\mathbf k\rightarrow \mathbf k+\mathbf Q$.