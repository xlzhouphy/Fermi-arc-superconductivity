# Figure 4 — Zero-temperature gap-to-$T_c$ ratio

This folder computes Fig. 4 of the paper: the doping dependence of the ratio $2\Delta(0)/T_c$, comparing results from the full variational method and the mean-field approximation.

## Notebooks

| Notebook | Description |
|----------|-------------|
| `0K_gap.ipynb` | **Variational method** — minimizes $\langle\psi|\hat{H}|\psi\rangle$ with respect to the BCS variational parameters $\theta_{\mathbf{k}}$, yielding $\Delta(0)$ and $T_c$ with full treatment of the many-body correction $A'$ |
| `0K_mean_field_gap.ipynb` | **Mean-field approximation** — computes $\Delta(0)$ and $T_c$ using only the single-particle spectral function $A(\mathbf{k},\omega)$, dropping the many-body correction $A'$ |
| `0K_ratio_plot.ipynb` | **Ratio plot** — loads precomputed data and produces the final Fig. 4, overlaid with Hubbard model and YBCO experimental data |

## Methods

### Variational method (full treatment)

The BCS variational wavefunction $|\psi\rangle = \prod_{\mathbf{k}}[\cos\theta_{\mathbf{k}} + \sin\theta_{\mathbf{k}}\hat{b}_{\mathbf{k}}^{\dagger}]|0\rangle$ is minimized:

$$
2\xi_{\mathbf{k}}\sin 2\theta_{\mathbf{k}} + 2U\sin 2\theta_{\mathbf{k}}\sin^2\theta_{\mathbf{k}+\mathbf{Q}} - \frac{J}{N}g_{\mathbf{k}}\cos 2\theta_{\mathbf{k}}\sum_{\mathbf{k}'}g_{\mathbf{k}'}\sin 2\theta_{\mathbf{k}'} = 0
$$

The zero-temperature gap is then $\Delta(0) = \frac{J}{N}\sum_{\mathbf{k}}g_{\mathbf{k}}\sin(2\theta_{\mathbf{k}})$. $T_c$ is computed using the full pair susceptibility (including the many-body correction $A'$).

### Mean-field approximation

Uses the standard BCS-like gap equation with only the single-particle spectral function:

$$
\frac{J}{N}\sum_{\mathbf{k}}\left[\frac{(1-n_{\mathbf{k}+\mathbf{Q}})g_{\mathbf{k}}^2}{2\sqrt{\Delta^2 g_{\mathbf{k}}^2/4 + \xi_{\mathbf{k}}^2}} + \frac{n_{\mathbf{k}+\mathbf{Q}}g_{\mathbf{k}}^2}{2\sqrt{\Delta^2 g_{\mathbf{k}}^2/4 + (\xi_{\mathbf{k}}+U)^2}}\right] = 1
$$

Here $T_c$ is computed with $A'=0$.

## Data files

Precomputed $\Delta(0)$, $T_c$, and doping values for various parameter sets:

| Naming pattern | Description |
|----------------|-------------|
| `*_N256_variational.npy` | Variational method, $256\times256$ k-grid |
| `*_N512_mean.npy` | Mean-field method, $512\times512$ k-grid |
| `Tc_*.npy` | Superconducting $T_c$ |
| `delta_*.npy` | Zero-temperature gap $\Delta(0)$ |
| `x_*.npy` | Hole doping $p$ |

## Derivations

The `formula/` subfolder contains step-by-step derivations:

- `Fermi arc model gap.md` / `.pdf` — derivation of the variational gap equation for the Fermi arc model
- `HK model variational method.md` — variational method applied to the HK model
- `Mean_field_delta.md` — mean-field gap equation
- `YBCO-note.md` — notes on YBCO experimental data used in the comparison plot

## Key result

The variational method (full treatment) yields a gap-to-$T_c$ ratio far exceeding the BCS value of 3.53 in the underdoped regime, consistent with experimental observations in cuprates. The mean-field approximation stays close to the BCS value, demonstrating that the enhancement is a consequence of the many-body nature of the Fermi arcs.
