# Figure 6: Superfluid stiffness

This directory contains the calculations of the superfluid stiffness in the superconducting Fermi-arc model and the benchmark calculations used to interpret it. It supports Figure 6 of the accompanying paper.

## Contents

- `Fermi-arc_stiffness.ipynb` — main finite-temperature superfluid-stiffness calculation for the Fermi-arc model.
- `Fermi-arc_mean-field_gap.ipynb` — self-consistent mean-field gap used in the stiffness calculation.
- `BCS_stiffness.ipynb` — BCS-limit benchmark.
- `HK_stiffness.ipynb` — Hatsugai--Kohmoto-model benchmark.
- `plot_stiffness.ipynb` — generates the publication plot from the stored arrays.
- `stiffness.md` — derivation notes for the current response and stiffness formula.
- `tight_binding_normal_state_stiffness.md` — normal-state tight-binding benchmark showing the cancellation of the superfluid stiffness without pairing.
- `dated/` — earlier calculation scripts, notebooks, parameter sweeps, and intermediate data.
- `doping_*.npy`, `normal_doping_*.npy`, and `stiffness_*.npy` — saved doping, normal-state, and stiffness data.
- `fermi_arc_stiffness.pdf` and `.png` — final Figure 6 output.

## Reproducing the figure

Use Python 3 with NumPy, SciPy, Matplotlib, and Jupyter Notebook. Run `Fermi-arc_mean-field_gap.ipynb` and `Fermi-arc_stiffness.ipynb` to regenerate the main data, then run `plot_stiffness.ipynb` to make the figure. The saved `.npy` arrays allow the plotting step to be reproduced without rerunning the full calculation.

Data filenames record the numerical settings, including the interaction $U$, pairing strength $J$, inverse temperature $\beta$, and momentum-grid sizes. `publication.mplstyle` contains the plotting style used for the publication-ready output.

## Reference material

The `reference/` directory contains background literature used during development. It is not required to run the calculation notebooks.
