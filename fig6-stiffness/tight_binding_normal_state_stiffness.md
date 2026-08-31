# Stiffness of a Two-Dimensional Tight-Binding Model Without Pairing

For normal state (ignoring spin), the current-current correlation function only has the diagonal terms:
$$
\begin{aligned}
D&=D_s^{\mathrm{dia}}-D_s^{\text {para }}\\

&=\frac{1}{N} \sum_{\mathbf{k}} \frac{\partial^2 \epsilon_{\mathbf{k}}}{\partial k_x^2}\langle c_{\mathbf{k}}^{\dagger} c_{\mathbf{k}}\rangle-\frac{1}{N} \sum_{\mathbf{k}}\left(\frac{\partial \epsilon_{\mathbf{k}}}{\partial k_x}\right)^2\left[-\frac{\partial f\left(\epsilon_{\mathbf{k}}\right)}{\partial \epsilon_{\mathbf{k}}}\right]\\

&=\frac{1}{N} \sum_{\mathbf{k}} \left[\frac{\partial^2 \epsilon_{\mathbf{k}}}{\partial k_x^2}f(\epsilon_{\mathbf{k}})+\left(\frac{\partial \epsilon_{\mathbf{k}}}{\partial k_x}\right)^2\frac{\partial f\left(\epsilon_{\mathbf{k}}\right)}{\partial \epsilon_{\mathbf{k}}}\right]\\

&=\frac{1}{N} \sum_{\mathbf{k}} \left[\frac{\partial^2 \epsilon_{\mathbf{k}}}{\partial k_x^2}f(\epsilon_{\mathbf{k}})+\frac{\partial \epsilon_{\mathbf{k}}}{\partial k_x}\frac{\partial f\left(\epsilon_{\mathbf{k}}\right)}{\partial k_x}\right]\\

&=\frac{1}{N} \sum_{\mathbf{k}} \left[\frac{\partial}{\partial k_x}\left(\frac{\partial \epsilon_{\mathbf{k}}}{\partial k_x}f(\epsilon_{\mathbf{k}})\right)\right]\\

&=0



\end{aligned}
$$
Fermi-Dirac distribution:
$$
\langle c_{\mathbf{k}}^{\dagger} c_{\mathbf{k}}\rangle=\frac{e^{-\beta\epsilon_{\mathbf{k}}}}{1+e^{-\beta \epsilon_{\mathbf{k}}}}=\frac{1}{1+e^{\beta \epsilon_{\mathbf{k}}}}=f(\epsilon_{\mathbf{k}})
$$

## Codex version

This note summarizes the stiffness calculation for a simple two-dimensional tight-binding normal state without superconducting pairing.

The main conclusion is:

$$
D_s=0
$$

if $D_s$ is interpreted as the **superfluid stiffness** or **Meissner stiffness**. A normal tight-binding metal can have a charge response or Drude weight, but it does not have superfluid stiffness without pairing.

## Model

Consider the normal-state tight-binding Hamiltonian

$$
H
=
\sum_{\mathbf k\sigma}
\xi_{\mathbf k}
n_{\mathbf k\sigma},
$$

where, for the nearest-neighbor square lattice,

$$
\xi_{\mathbf k}
=
-2t(\cos k_x+\cos k_y)-\mu .
$$

There is no pairing term, so the Hamiltonian is diagonal in the occupation basis.

## Current and Diamagnetic Operators

Introduce a uniform vector potential $A_x$ through the Peierls substitution

$$
\xi_{\mathbf k}
\rightarrow
\xi_{\mathbf k-A_x}.
$$

Expanding to second order in $A_x$,

$$
\xi_{\mathbf k-A_x}
=
\xi_{\mathbf k}
-
A_x
\frac{\partial \xi_{\mathbf k}}{\partial k_x}
+
\frac{A_x^2}{2}
\frac{\partial^2 \xi_{\mathbf k}}{\partial k_x^2}
+\cdots .
$$

Therefore the paramagnetic current operator is

$$
J_x
=
\sum_{\mathbf k\sigma}
v_x(\mathbf k)
n_{\mathbf k\sigma},
\qquad
v_x(\mathbf k)
=
\frac{\partial \xi_{\mathbf k}}{\partial k_x},
$$

and the diamagnetic operator is

$$
K_{xx}
=
\sum_{\mathbf k\sigma}
m^{-1}_{xx}(\mathbf k)
n_{\mathbf k\sigma},
\qquad
m^{-1}_{xx}(\mathbf k)
=
\frac{\partial^2 \xi_{\mathbf k}}{\partial k_x^2}.
$$

For nearest-neighbor hopping,

$$
v_x(\mathbf k)=2t\sin k_x,
$$

$$
m^{-1}_{xx}(\mathbf k)=2t\cos k_x.
$$

## Kubo Formula

The stiffness is computed from the eigenstate-sum form

$$
\frac{D_s}{\pi}
=
\frac{1}{N}
\left[
\langle K_{xx}\rangle
-
\sum_{n,m}
\left|\langle n|J_x|m\rangle\right|^2
\frac{\rho_m-\rho_n}{E_n-E_m}
\right],
$$

where $|m\rangle$ and $|n\rangle$ are many-body eigenstates of $H$, with eigenenergies $E_m$ and $E_n$, and

$$
\rho_m
=
\frac{e^{-\beta E_m}}{Z}.
$$

The first term is the diamagnetic response, and the second term is the paramagnetic current-current response written directly in the eigenbasis.

For the normal-state tight-binding Hamiltonian, the occupation number satisfies

$$
[n_{\mathbf k\sigma},H]=0.
$$

The diamagnetic term is therefore

$$
\langle K_{xx}\rangle
=
\sum_{\mathbf k\sigma}
\frac{\partial^2 \xi_{\mathbf k}}{\partial k_x^2}
\langle n_{\mathbf k\sigma}\rangle.
$$

For a free fermion normal state,

$$
\langle n_{\mathbf k\sigma}\rangle
=
f(\xi_{\mathbf k}),
$$

with

$$
f(\xi_{\mathbf k})
=
\frac{1}{e^{\beta \xi_{\mathbf k}}+1}
=
\frac{e^{-\beta \xi_{\mathbf k}}}
{1+e^{-\beta \xi_{\mathbf k}}}.
$$

Therefore

$$
\langle K_{xx}\rangle
=
\sum_{\mathbf k\sigma}
\frac{\partial^2 \xi_{\mathbf k}}{\partial k_x^2}
f(\xi_{\mathbf k}).
$$

For the paramagnetic current term, the current operator is diagonal in the same occupation basis:

$$
J_x
=
\sum_{\mathbf k\sigma}
v_x(\mathbf k)n_{\mathbf k\sigma}.
$$

Thus the current matrix elements in

$$
\sum_{n,m}
\left|\langle n|J_x|m\rangle\right|^2
\frac{\rho_m-\rho_n}{E_n-E_m}
$$

mainly involve diagonal or degenerate contributions with $E_n-E_m=0$. The ratio must then be interpreted as the limiting derivative

$$
\frac{\rho_m-\rho_n}{E_n-E_m}
\rightarrow
-\frac{\partial \rho}{\partial E}.
$$

For a single fermionic mode, this normalized derivative gives

$$
-\frac{\partial f(\xi_{\mathbf k})}{\partial \xi_{\mathbf k}}
=
\beta
f(\xi_{\mathbf k})
[1-f(\xi_{\mathbf k})].
$$

Equivalently, this is the occupation-number fluctuation multiplied by $\beta$:

$$
\beta
\left(
\langle n_{\mathbf k\sigma}^2\rangle
-
\langle n_{\mathbf k\sigma}\rangle^2
\right)
=
\beta
f(\xi_{\mathbf k})[1-f(\xi_{\mathbf k})].
$$

Therefore the eigenstate current sum reduces to

$$
\sum_{n,m}
\left|\langle n|J_x|m\rangle\right|^2
\frac{\rho_m-\rho_n}{E_n-E_m}
=
\beta
\sum_{\mathbf k\sigma}
\left(
\frac{\partial \xi_{\mathbf k}}{\partial k_x}
\right)^2
f(\xi_{\mathbf k})
[1-f(\xi_{\mathbf k})].
$$

Putting the diamagnetic and current terms together gives

$$
\frac{D_s}{\pi}
=
\frac{1}{N}
\sum_{\mathbf k\sigma}
\left[
\frac{\partial^2 \xi_{\mathbf k}}{\partial k_x^2}
f(\xi_{\mathbf k})
-
\beta
\left(
\frac{\partial \xi_{\mathbf k}}{\partial k_x}
\right)^2
f(\xi_{\mathbf k})
[1-f(\xi_{\mathbf k})]
\right].
$$

For nearest-neighbor hopping,

$$
\frac{D_s}{\pi}
=
\frac{1}{N}
\sum_{\mathbf k\sigma}
\left[
2t\cos k_x\, f(\xi_{\mathbf k})
-
\beta(2t\sin k_x)^2
f(\xi_{\mathbf k})
[1-f(\xi_{\mathbf k})]
\right].
$$

## Cancellation in the Full Brillouin Zone

Using

$$
\frac{\partial f(\xi_{\mathbf k})}{\partial k_x}
=
\frac{\partial f}{\partial \xi_{\mathbf k}}
\frac{\partial \xi_{\mathbf k}}{\partial k_x}
=
-\beta
f(\xi_{\mathbf k})[1-f(\xi_{\mathbf k})]
\frac{\partial \xi_{\mathbf k}}{\partial k_x},
$$

we can rewrite the integrand as

$$
\frac{\partial^2 \xi_{\mathbf k}}{\partial k_x^2}
f(\xi_{\mathbf k})
-
\beta
\left(
\frac{\partial \xi_{\mathbf k}}{\partial k_x}
\right)^2
f(\xi_{\mathbf k})
[1-f(\xi_{\mathbf k})]
=
\frac{\partial}{\partial k_x}
\left[
\frac{\partial \xi_{\mathbf k}}{\partial k_x}
f(\xi_{\mathbf k})
\right].
$$

Therefore

$$
\frac{D_s}{\pi}
=
\frac{1}{N}
\sum_{\mathbf k\sigma}
\frac{\partial}{\partial k_x}
\left[
\frac{\partial \xi_{\mathbf k}}{\partial k_x}
f(\xi_{\mathbf k})
\right].
$$

On a complete periodic Brillouin zone, the sum or integral of this total derivative vanishes:

$$
D_s=0.
$$

This is the expected result for the superfluid stiffness of a normal state without pairing.

## Degenerate Limit of the Current Term

For the normal tight-binding model, $H$ and $J_x$ are diagonal in the same occupation basis. Therefore the current matrix elements in

$$
\sum_{n,m}
\left|\langle n|J_x|m\rangle\right|^2
\frac{\rho_m-\rho_n}{E_n-E_m}
$$

mainly involve degenerate or diagonal contributions with $E_n-E_m=0$. In this case, the current-current term must be interpreted through the degeneracy limit

$$
\frac{\rho_m-\rho_n}{E_n-E_m}
\rightarrow
-\frac{\partial \rho}{\partial E}.
$$

The important point is that this derivative should be understood for the properly normalized thermal probability. For a single fermionic mode, the two possible occupations are $n=0$ and $n=1$, with the single-mode partition function

$$
Z_{\mathbf k}=1+e^{-\beta \xi}.
$$

The occupation probability is

$$
f(\xi)
=
\frac{e^{-\beta \xi}}
{1+e^{-\beta \xi}}.
$$

Equivalently,

$$
f(\xi)
=
\frac{1}{e^{\beta \xi}+1}.
$$

The degeneracy limit is essentially the derivative of the thermal weight with respect to energy. Taking the derivative with respect to $\xi$ gives

$$
\frac{\partial f}{\partial \xi}
=
-\frac{\beta e^{\beta \xi}}
{(e^{\beta \xi}+1)^2}.
$$

On the other hand,

$$
f(1-f)
=
\frac{1}{e^{\beta \xi}+1}
\frac{e^{\beta \xi}}{e^{\beta \xi}+1}
=
\frac{e^{\beta \xi}}
{(e^{\beta \xi}+1)^2}.
$$

Therefore

$$
\frac{\partial f}{\partial \xi}
=
-\beta f(1-f),
$$

and hence

$$
-\frac{\partial f}{\partial \xi}
=
\beta f(\xi)[1-f(\xi)].
$$

Putting this back into the eigenstate current sum, when $E_n\to E_m$,

$$
\frac{\rho_m-\rho_n}{E_n-E_m}
\rightarrow
-\frac{\partial \rho}{\partial E}
\quad
\Longrightarrow
\quad
-\frac{\partial f}{\partial \xi}
=
\beta f(1-f).
$$

Equivalently, this is the occupation-number fluctuation multiplied by $\beta$:

$$
\beta
\left(
\langle n^2\rangle-\langle n\rangle^2
\right)
=
\beta f(1-f).
$$

Thus the paramagnetic current sum in the normal state must reduce to the occupation-number fluctuation

$$
\beta f(1-f),
$$

not simply $\beta f$.





