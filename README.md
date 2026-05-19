# Exact Theory of Superconductivity in a Strongly Correlated Fermi-Arc Model

[![arXiv](https://img.shields.io/badge/arXiv-2603.24977-b31b1b.svg)](https://arxiv.org/abs/2603.24977)

This repository contains the code and data for the paper *"Exact theory of superconductivity in a strongly correlated Fermi-arc model"* by Xianliang Zhou, Fei Yang, Miao Liu, Yin Shi, and Sheng Meng.

## Overview

We study an exactly solvable model that exhibits both Fermi arcs and d-wave superconductivity. The model produces an asymptotically exact solution for the superconducting transition temperature $T_c$, tracing out a superconductivity dome as a function of hole doping in qualitative agreement with cuprate experiments. Crucially, the Fermi arcs generate an additional many-body effect that suppresses $T_c$ beyond the simple reduction expected from a shrinking Fermi surface, and renders the gap-to-$T_c$ ratio far exceeding the BCS limit.

## Model

The Fermi-arc Hamiltonian with d-wave pairing:

$$
\hat{H} = \sum_{\mathbf{k}\sigma}\left[\xi_{\mathbf{k}} \hat{n}_{\mathbf{k}\sigma} + \frac{U}{2} \hat{n}_{\mathbf{k}\sigma} \hat{n}_{\mathbf{k}+\mathbf{Q}\bar{\sigma}}\right] - \frac{J}{N}\hat{\Delta}^{\dagger}\hat{\Delta}, \qquad \hat{\Delta}^{\dagger} = \sum_{\mathbf{k}} \gamma_{\mathbf{k}} \hat{c}^{\dagger}_{-\mathbf{k}\downarrow}\hat{c}^{\dagger}_{\mathbf{k}\uparrow}
$$

where $\gamma_{\mathbf{k}} = \cos k_x - \cos k_y$ and $\mathbf{Q} = (\pi, \pi)$.

## Repository structure

```
.
├── Hatsugai–Kohmoto model/            # HK model foundation & benchmark
├── fig1-spectrum/                     # Figure 1: Fermi surface & spectral function
├── fig2&3-superconducting_temperature_Tc/  # Figures 2 & 3: Tc phase diagrams
├── fig4-0K_gap/                       # Figure 4: Zero-temperature gap-to-Tc ratio
├── BCS_theory/                        # BCS theory background notes
└── reference paper/                   # Key reference papers
```

| Directory | Figure | Description |
|-----------|--------|-------------|
| `Hatsugai–Kohmoto model/` | — | HK model derivation and reproduction of Phillips *et al.* (2020) Fig. 2 |
| `fig1-spectrum/` | Fig. 1 | Normal-state Fermi surfaces and single-particle excitation spectra at three doping levels |
| `fig2&3-superconducting_temperature_Tc/` | Figs. 2 & 3 | $T_c$ phase diagrams for varying $U$ (Fig. 2) and varying $J$ (Fig. 3), with pseudogap boundary $T^*$ |
| `fig4-0K_gap/` | Fig. 4 | Zero-temperature gap $\Delta(0)$ from variational and mean-field methods, and the ratio $2\Delta(0)/T_c$ |
| `BCS_theory/` | — | Standard BCS theory derivations and numerical benchmarks |

## Dependencies

- Python 3.x
- NumPy, SciPy, Matplotlib
- Jupyter Notebook

## Reference papers

Key references are provided in `reference paper/`:

- Phillips, Yeo & Huang, *Nat. Phys.* **16**, 1175 (2020) — exact HK model superconductivity
- Worm *et al.*, *Phys. Rev. Lett.* **133**, 166501 (2024) — Fermi arc model origin
- Hatsugai–Kohmoto models topic review (arXiv:2501.00388)

## Citation

If you use this code, please cite the corresponding paper.
