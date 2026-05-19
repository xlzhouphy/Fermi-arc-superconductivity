# Figure 2 & 3 — Superconducting phase diagrams

This folder produces Fig. 2 and Fig. 3 of the paper: the superconducting $T_c$ phase diagrams of the Fermi-arc model as functions of hole doping, showing the interplay between superconductivity and the pseudogap.

## Physics

The superconducting $T_c$ is determined by the Thouless criterion $J\chi_0 = 1$, where the pair susceptibility includes a many-body correction $A'$ beyond the single-particle spectral function:

$$
\chi_0 = \frac{1}{N} \sum_{\mathbf{k}} \gamma_{\mathbf{k}}^2 \left\{
\frac{(1-n_{\mathbf{k}+\mathbf{Q}})^2}{2\xi_{\mathbf{k}}} \tanh\frac{\beta\xi_{\mathbf{k}}}{2}
+ \frac{n_{\mathbf{k}+\mathbf{Q}}^2}{2(\xi_{\mathbf{k}}+U)} \tanh\frac{\beta(\xi_{\mathbf{k}}+U)}{2}
+ \frac{n_{\mathbf{k}+\mathbf{Q}}(1-n_{\mathbf{k}+\mathbf{Q}})}{2\xi_{\mathbf{k}}+U} \left[\tanh\frac{\beta\xi_{\mathbf{k}}}{2} + \tanh\frac{\beta(\xi_{\mathbf{k}}+U)}{2}\right]
\right\}
$$

The first two terms come from the single-particle spectral function $A$; the third term is the many-body correction $A'$. Setting term 3 to zero gives the mean-field $T_c$ (labeled $A$ in the figures), while the full expression yields the interacting $T_c$ (labeled $\tilde{A}$).

The pseudogap onset temperature $T^*$ is determined by scanning temperature until the Fermi surface closes (spectral weight connects across the AFZB).

## Notebooks

| Notebook | Description |
|----------|-------------|
| `Fermi_arc_Tc.ipynb` | Core $T_c$ computation engine: scans chemical potential $\mu$, solves $J\chi_0=1$ for $T_c$, and converts to hole doping $p$. Computes both full (with $A'$) and mean-field (without $A'$) results. |
| `fig2.ipynb` | **Figure 2** — Phase diagrams for various repulsion strengths $U$ at fixed $J=0.8$. 2×2 panel showing $T_c$ vs $p$ for $U=2, 1, 0.4, 0$, with $T^*$ line overlaid. Panel (b) shows the relative many-body suppression $\Delta T_c/T_c$. |
| `fig3.ipynb` | **Figure 3** — Phase diagrams for various pairing strengths $J$ at fixed $U=2$. 2×2 panel showing $T_c$ vs $p$ for $J=0.8, 1.2, 1.6, 2.0$, with $T^*$ line overlaid. Panel (b) shows the relative many-body suppression. |

## Key findings

- **Superconducting dome**: $T_c$ traces a dome-shaped curve as a function of doping, with optimal doping near the quantum critical point where the pseudogap closes.
- **Many-body suppression**: The correction $A'$ (term 3) consistently *suppresses* $T_c$ in the underdoped regime. The suppression is strongest around mid-underdoping and intensifies with increasing $U$ and $J$.
- **Pseudogap boundary**: $T^*$ decreases approximately linearly with doping, consistent with experimental cuprate phase diagrams.
- **$U=0$ limit**: Recovers standard BCS theory; $T_c$ with and without $A'$ coincide.

## Data files

### Computed Tc data

| Naming pattern | Description |
|----------------|-------------|
| `Tc_U=*_g=*.npy` | $T_c$ with full susceptibility ($\tilde{A}$) |
| `Tc0_U=*_g=*.npy` | $T_c$ without $A'$, mean-field ($A$) |
| `x_U=*_g=*.npy` | Doping $p$ for the corresponding $T_c$ array |
| `x0_U=*_g=*.npy` | Doping $p$ for the corresponding $T_c^0$ array |

### Pseudogap data

| File | Description |
|------|-------------|
| `pseudo_U=*_T.npy` | Pseudogap onset temperature $T^*$ |
| `pseudo_U=*_doping.npy` | Doping values at $T^*$ |
| `pseudo_U=*_mu.npy` | Chemical potential values |

### Output figures

| File | Description |
|------|-------------|
| `U.pdf` | Fig. 2(a): Phase diagrams for varying $U$ |
| `U_difference.pdf` | Fig. 2(b): $\Delta T_c/T_c$ for varying $U$ |
| `g.pdf` | Fig. 3(a): Phase diagrams for varying $J$ |
| `g_difference.pdf` | Fig. 3(b): $\Delta T_c/T_c$ for varying $J$ |
| `Fermi_arc_n.png` | Electron filling density plot |

## Derivations

The `formula/` subfolder contains derivations of the two equivalent formulations of $\chi_0$ (Eqs. 24 and 25 in the derivation notes).
