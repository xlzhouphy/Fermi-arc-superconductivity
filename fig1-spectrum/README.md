# Figure 1 — Normal-state Fermi surface and single-particle spectrum

This folder produces Fig. 1 of the paper: the normal-state Fermi surfaces (top row) and single-particle excitation spectra (bottom row) of the Fermi-arc model at three representative doping levels.

## Physics

The single-particle spectral function of the Fermi-arc model has a two-pole structure:

$$
A(\mathbf{k}, \omega) = (1 - n_{\mathbf{k}+\mathbf{Q}})\,\delta(\omega - \xi_{\mathbf{k}}) + n_{\mathbf{k}+\mathbf{Q}}\,\delta(\omega - \xi_{\mathbf{k}} - U)
$$

The two terms correspond to the lower Hubbard band (LHB) and upper Hubbard band (UHB), with their spectral weights controlled by the momentum-dependent occupation $n_{\mathbf{k}+\mathbf{Q}}$. For underdoped states, $n_{\mathbf{k}+\mathbf{Q}}$ suppresses the spectral weight outside the antiferromagnetic zone boundary (AFZB), truncating the Fermi surface into disconnected segments — **Fermi arcs**.

## Figure panels

| Panel | Doping $p$ | $\mu$ | State |
|-------|-----------|-------|-------|
| (a, d) | 0.15 | −0.674 | Underdoped — Fermi arcs |
| (b, e) | 0.32 | −1.13 | Optimal doped — quantum critical point |
| (c, f) | 0.56 | −1.60 | Overdoped — full Fermi surface |

- **Top row (a–c)**: Spectral weight at $\omega = 0$ in the $(k_x, k_y)$ plane. White dashed lines mark the AFZB ($|k_x| + |k_y| = \pi$). Pentagon/star/square markers denote the three doping levels also shown in Figs. 2–3 of the paper.
- **Bottom row (d–f)**: Spectral function along the high-symmetry path $\Gamma \to X \to M \to \Gamma$. The white dashed line marks the Fermi level. UHB/LHB labels indicate the upper and lower Hubbard bands.

## Files

| File | Description |
|------|-------------|
| `Fermi_arc_spectrum_plot.ipynb` | Main notebook: computes and plots Fermi surfaces and spectral functions |
| `spectrum_K256_U=2.0_mu=*.npy` | Precomputed 2D spectral weight $A(\mathbf{k}, \omega=0)$ on a $256\times256$ grid |
| `band_K256_U=2.0_mu=*.npy` | Precomputed spectral function $A(k, \omega)$ along the $\Gamma$–$X$–$M$–$\Gamma$ path |
| `Kpath_NK200.npy` | Momentum coordinate array for the k-path (200 points per segment) |
| `spectrum.pdf` | Output figure |
| `publication.mplstyle` | Matplotlib style for publication-quality rendering |

## Notebook structure

| Cell | Content |
|------|---------|
| 1 | Parameter notes (doping levels, $T_c$ values) |
| 2 | 2D spectral weight at $\omega = 0$ (Fermi surface map) |
| 3 | Spectral function along $\Gamma$–$X$–$M$–$\Gamma$ |
| 4 | Final 2×3 panel figure with six subplots (panels a–f) |
| 5 | Plot of the many-body correction $A'(\mathbf{k}, \omega)$ defined in Eq. (12) of the paper |
