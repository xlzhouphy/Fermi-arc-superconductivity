# Hatsugai-Kohmoto (HK) Model

The HK model is the foundation of our work. This folder reproduces Figure 2 from Phillips *et al.*, *Nat. Phys.* **16**, 1175–1180 (2020), and the computational method demonstrated here serves as the core framework for our paper's calculations.

## Reference

> Phillips, P.W., Yeo, L. & Huang, E.W. Exact theory for superconductivity in a doped Mott insulator. *Nat. Phys.* **16**, 1175–1180 (2020). [doi:10.1038/s41567-020-0988-4](https://doi.org/10.1038/s41567-020-0988-4)

For a broader review of HK models, see: [arXiv:2501.00388](https://arxiv.org/abs/2501.00388).

## Model

The HK Hamiltonian in momentum space:

$$
\hat{H}_{\mathrm{HK}} = \sum_{\mathbf{k}}\left[(\varepsilon_{\mathbf{k}} - \mu)(\hat{n}_{\mathbf{k}\uparrow} + \hat{n}_{\mathbf{k}\downarrow}) + U \hat{n}_{\mathbf{k}\uparrow} \hat{n}_{\mathbf{k}\downarrow}\right]
$$

This is an exactly solvable model because different $\mathbf{k}$-modes are decoupled. The single-particle Green's function has a two-pole structure with spectral weights determined by the electron occupation $n_{\mathbf{k}}$:

$$
G_{\mathbf{k}\sigma}(\omega) = \frac{1 - n_{\mathbf{k}}}{\omega - (\varepsilon_{\mathbf{k}} - \mu)} + \frac{n_{\mathbf{k}}}{\omega - (\varepsilon_{\mathbf{k}} - \mu + U)}
$$

## Pair susceptibility

With an s-wave pairing interaction, the bare pair susceptibility at zero frequency is:

$$
\chi_0 = \frac{1}{N}\sum_{\mathbf{k}}\left[\frac{(1 - n_{\mathbf{k}})^2}{2\xi_{\mathbf{k}}} \tanh\left(\frac{\beta\xi_{\mathbf{k}}}{2}\right) + \frac{n_{\mathbf{k}}^2}{2(\xi_{\mathbf{k}} + U)} \tanh\left(\frac{\beta(\xi_{\mathbf{k}} + U)}{2}\right)\right]
$$

where $\xi_{\mathbf{k}} = \varepsilon_{\mathbf{k}} - \mu$. The superconducting $T_c$ is determined by the Thouless criterion $g\chi_0 = 1$.

## Files

| File | Description |
|------|-------------|
| `HK_model.md` | Theoretical notes: electron occupation, Green's function, pair susceptibility derivation, and the extension to the Fermi arc model |
| `HK_model.ipynb` | Numerical calculation of electron occupation and Tc vs doping (reproduces Fig. 2 of Phillips *et al.* 2020) |

## Notebook structure

| Cell | Content |
|------|---------|
| 1 | Electron occupation $n(\varepsilon)$ at different temperatures |
| 2 | $T_c$ vs chemical potential $\mu$ |
| 3–6 | $T_c$ vs doping for different $U$ values |
| 7 | **Figure 2 reproduction**: $T_c/W$ vs doping on log scale for $U/W = 0.1, 0.4, 0.6$ |
| 8 | Same calculation with larger pairing strength $g$ |

## Our paper

Our work replaces the s-wave pairing interaction with a d-wave form factor $g_{\mathbf{k}} = \cos k_x - \cos k_y$ and extends the model to include a momentum-shifted interaction ($\mathbf{k} \leftrightarrow \mathbf{k} + \mathbf{Q}$) that generates Fermi arcs. The core computational loop — scanning $\mu$, solving $g\chi_0 = 1$ for $T_c$, and computing doping — is inherited directly from this notebook.
