# Hatsugai–Kohmoto (HK) Model

The HK model is the foundation of our work. This folder contains theoretical derivations and numerical implementations that span the normal-state HK model, the mean-field superconducting extension, and observables (spectral function, superfluid stiffness, and integrated spectral weight). The computational framework demonstrated here serves as the core engine for our paper's calculations.

## Reference

> Phillips, P.W., Yeo, L. & Huang, E.W. Exact theory for superconductivity in a doped Mott insulator. *Nat. Phys.* **16**, 1175–1180 (2020). [doi:10.1038/s41567-020-0988-4](https://doi.org/10.1038/s41567-020-0988-4)

For a broader review of HK models, see: [arXiv:2501.00388](https://arxiv.org/abs/2501.00388).

---

## Normal-State HK Model

The HK Hamiltonian in momentum space:

$$
\hat{H}_{\mathrm{HK}} = \sum_{\mathbf{k}}\left[(\varepsilon_{\mathbf{k}} - \mu)(\hat{n}_{\mathbf{k}\uparrow} + \hat{n}_{\mathbf{k}\downarrow}) + U \hat{n}_{\mathbf{k}\uparrow} \hat{n}_{\mathbf{k}\downarrow}\right]
$$

This is an exactly solvable model because different $\mathbf{k}$-modes are decoupled. Each $\mathbf{k}$-sector has four Fock states $\{|0\rangle, |\!\uparrow\rangle, |\!\downarrow\rangle, |\!\uparrow\downarrow\rangle\}$ with energies $\{0,\ \xi_{\mathbf{k}},\ \xi_{\mathbf{k}},\ 2\xi_{\mathbf{k}}+U\}$, where $\xi_{\mathbf{k}} = \varepsilon_{\mathbf{k}} - \mu$.

### Electron occupation

$$
n_{k\sigma} = \frac{e^{-\beta\xi_{\mathbf{k}}} + e^{-\beta(2\xi_{\mathbf{k}}+U)}}{1 + 2e^{-\beta\xi_{\mathbf{k}}} + e^{-\beta(2\xi_{\mathbf{k}}+U)}}
$$

### Single-particle Green's function & Spectral function

The Green's function has a two-pole structure with spectral weights determined by the electron occupation:

$$
G_{\mathbf{k}\sigma}(\omega) = \frac{1 - n_{\mathbf{k}}}{\omega - \xi_{\mathbf{k}}} + \frac{n_{\mathbf{k}}}{\omega - (\xi_{\mathbf{k}} + U)}
$$

The exact spectral function (derived in Appendix 1 of `Hatsugai–Kohmoto model.md`):

$$
A_\sigma(k,\omega) = \frac{1+e^{-\beta\xi_k}}{Z_k}\delta(\omega-\xi_k) + \frac{e^{-\beta\xi_k}+e^{-\beta(2\xi_k+U)}}{Z_k}\delta(\omega-\xi_k-U)
$$

where $Z_k = 1 + 2e^{-\beta\xi_k} + e^{-\beta(2\xi_k+U)}$.

### Pair susceptibility & $T_c$

With an s-wave pairing interaction, the bare pair susceptibility at zero frequency is:

$$
\chi_0 = \frac{1}{N}\sum_{\mathbf{k}}\left[\frac{(1 - n_{\mathbf{k}})^2}{2\xi_{\mathbf{k}}} \tanh\left(\frac{\beta\xi_{\mathbf{k}}}{2}\right) + \frac{n_{\mathbf{k}}^2}{2(\xi_{\mathbf{k}} + U)} \tanh\left(\frac{\beta(\xi_{\mathbf{k}} + U)}{2}\right)\right]
$$

The superconducting $T_c$ is determined by the Thouless criterion $g\chi_0 = 1$.

---

## Superconducting Mean-Field Extension

The superconducting mean-field Hamiltonian introduces a pairing field $\Delta$:

$$
H^{\mathrm{MF}} = \sum_{\mathbf{k}} \xi_{\mathbf{k}}(n_{\mathbf{k}\uparrow}+n_{\mathbf{k}\downarrow}) + U n_{\mathbf{k}\uparrow}n_{\mathbf{k}\downarrow} + \Delta^* b_{\mathbf{k}} + \Delta b_{\mathbf{k}}^{\dagger}
$$

with $b_{\mathbf{k}}^{\dagger} = c^{\dagger}_{\mathbf{k}\uparrow}c^{\dagger}_{-\mathbf{k}\downarrow}$ and the self-consistency condition:

$$
\Delta = -\frac{g}{N}\sum_{\mathbf{k}>0} \langle b_{\mathbf{k}} + b_{-\mathbf{k}} \rangle
$$

Each $(\mathbf{k},-\mathbf{k})$ sector spans a 16-dimensional Hilbert space. Using $S_z$ and momentum conservation, the Hamiltonian block-diagonalizes into nine blocks (see `Hatsugai–Kohmoto model.md` for the full derivation):

$$
\boxed{H_k^{\rm MF} = (2\xi_k) \oplus (h_1\oplus h_1) \oplus \left[H_{s_z=0}^{(4)}\oplus (2\xi_k+U)\oplus (2\xi_k+U)\right] \oplus (h_1\oplus h_1) \oplus (2\xi_k)}
$$

with

$$
h_1 = \begin{pmatrix} \xi_k & -\Delta^* \\ -\Delta & 3\xi_k+U \end{pmatrix}
$$

and $H_{s_z=0}^{(4)}$ a $4\times4$ block in the zero-momentum Cooper subspace.

### Superfluid stiffness

$$
\frac{D_s}{\pi} = \frac{1}{L^d}\left(\langle K_{xx}\rangle - \int_0^\beta d\tau \langle J_x(\tau) J_x\rangle\right)
$$

with the current operator $J_x = \sum_{\mathbf{k}\sigma} \frac{\partial\varepsilon_{\mathbf{k}}}{\partial k_x} c^{\dagger}_{\mathbf{k}\sigma}c_{\mathbf{k}\sigma}$.

---

## Files

| File | Description |
|------|-------------|
| `HK_model.md` | Theoretical notes: electron occupation, Green's function, pair susceptibility derivation, and the extension to the Fermi arc model (see [arXiv:2501.00388](https://arxiv.org/abs/2501.00388)) |
| `HK_model.ipynb` | **Normal-state $T_c$ calculation.** Computes electron occupation $n(\varepsilon)$ and $T_c$ vs doping; reproduces Figure 2 of Phillips *et al.* (2020) — $T_c/W$ vs doping on log scale for $U/W = 0.1, 0.4, 0.6$ |
| `plot_hk_spectral_function.py` | **Normal-state spectral function.** Computes $A_\sigma(k,\omega)$ with Lorentzian-broadened delta peaks for $U=4$, $\mu=U/2$ (half-filling). Quick standalone script. |
| `plot_hk_superconducting_spectral_function_block.ipynb` | **Superconducting spectral function & stiffness.** Cell 1: 1D $A_\uparrow(k,\omega)$ via exact block diagonalization + self-consistent gap (root-finding). Cell 2: 2D superfluid stiffness $D_s$ vs filling $\langle n\rangle$ for multiple $(U,g)$ pairs. |
| `spectrum_lower_hubbard_weight_fig3c.ipynb` | **Lower Hubbard band weight (Fig. 3c–style).** Computes $W_L(g)/W_L(g=0)$ — the integrated spectral weight in $-4 < \omega/t < 4$ — as a function of pairing coupling $g$, using exact block diagonalization. Demonstrates spectral weight transfer from the lower to the upper Hubbard band with increasing $g$. |
| `Hatsugai–Kohmoto model.md` | **Comprehensive theoretical derivation** (in LaTeX-style). Covers: normal-state spectral function (Appendix 1, complete derivation), superconducting block diagonalization ($S_z=0,\pm1,\pm2$ sectors), gap equation, and superfluid stiffness. This is the primary theory reference for our implementation. |
| `HK_n.png` | Output: electron occupation $n(\varepsilon)$ at $T=0.5$ and $T=0.01$ for $U=5$, $\mu=U/2$ |
| `hk_spectral_function.png` | Output: normal-state $A_\sigma(k,\omega)$ for $U=4$, $\mu=U/2$, $\beta=20$ |
| `hk_superconducting_spectral_function_block.png` | Output: superconducting $A_\uparrow(k,\omega)$ with self-consistent $\Delta$, $U=8$, $\mu=1$, $\beta=1000$ |
| `hk_stiffness_2d_from_spectrum_base.png` | Output: 2D superfluid stiffness $D_s$ vs filling $\langle n\rangle$ for $U/t=0,12$ and various $g/t$ |

### Notebook details

#### `HK_model.ipynb` (8 cells)

| Cell | Content |
|------|---------|
| 1 | Electron occupation $n(\varepsilon)$ at different temperatures |
| 2 | $T_c$ vs chemical potential $\mu$ |
| 3–6 | $T_c$ vs doping for different $U$ values |
| 7 | **Figure 2 reproduction**: $T_c/W$ vs doping on log scale for $U/W = 0.1, 0.4, 0.6$ |
| 8 | Same calculation with larger pairing strength $g = 0.2W$ |

#### `plot_hk_superconducting_spectral_function_block.ipynb` (2 cells)

| Cell | Content |
|------|---------|
| 1 | 1D spectral function: builds the block matrices, diagonalizes, solves the self-consistent gap equation via `root_scalar`, and plots $A_\uparrow(k,\omega)$ |
| 2 | 2D superfluid stiffness: computes $D_s$ vs filling on a $32\times32$ half-BZ grid for $U/t=0,12$ and $g/t=1.5,2.0,3.0$. Uses the same block diagonalization infrastructure. |

#### `spectrum_lower_hubbard_weight_fig3c.ipynb` (1 cell)

| Cell | Content |
|------|---------|
| 1 | Computes the integrated lower Hubbard band weight $W_L(g)/W_L(g=0)$ for $-4 < \omega/t < 4$ at $\mu/t=1$, for $U/t=8,16,32$ and a range of $g/t$ values. Demonstrates that pairing depletes the lower Hubbard band. |

---

## Computational Infrastructure

All superconducting calculations share a common codebase of core functions:

- **Block diagonalization**: `block_matrix_elements()`, `diagonalize_sector_block()` — build and diagonalize the $S_z$-sorted blocks
- **Fermionic operators**: `annihilation_operator()`, `sector_operators()` — construct $c_{k\sigma}$ and $b_k + b_{-k}$ in the occupation basis
- **Spectral function**: `spectral_function_for_k_block()` — compute $A_\sigma(k,\omega)$ from the Lehmann representation with Lorentzian broadening
- **Gap equation**: `solve_gap_block()` — self-consistent gap via `scipy.optimize.root_scalar`
- **Stiffness**: `sector_stiffness_observables_2d()`, `superfluid_stiffness_2d()` — compute $D_s$ from the current-current response

---

## Our Paper

Our work replaces the s-wave pairing interaction with a d-wave form factor $g_{\mathbf{k}} = \cos k_x - \cos k_y$ and extends the model to include a momentum-shifted interaction ($\mathbf{k} \leftrightarrow \mathbf{k} + \mathbf{Q}$) that generates Fermi arcs. The core computational loop — scanning $\mu$, solving $g\chi_0 = 1$ for $T_c$, and computing doping — is inherited directly from `HK_model.ipynb`. The superconducting spectral function and stiffness codes in the block-diagonalization notebooks directly generalize to the Fermi arc case.
