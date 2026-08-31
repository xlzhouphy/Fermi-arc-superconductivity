# Figure 5: Superconducting spectral functions and density of states

This directory contains the mean-field calculation of the single-particle spectral function and density of states in the superconducting Fermi-arc model. It supports Figure 5 of the accompanying paper.

## Contents

- `superconducting_spectrum.ipynb` — constructs and diagonalizes the superconducting momentum-sector Hamiltonian and evaluates the spectral function.
- `superconducting_dos.ipynb` — evaluates the superconducting density of states.
- `plot_spectrum.ipynb`, `plot_DOS.ipynb`, and `plot.ipynb` — prepare the spectrum, DOS, and combined publication plots.
- `Fermi-arc model_sc_spectrum.md` — derivation of the normal-state model, mean-field superconducting Hamiltonian, and block-diagonal structure.
- `formula.md` — mean-field decoupling notes and spectral-function formulae.
- `fermi-arc-0603/` — Python implementation modules used by the notebooks.
- `data/` and the root-level `.npy` files — saved spectral-function and DOS arrays for representative chemical potentials and interaction parameters.
- `fermi_arc_spectrum_dos.pdf` and `.png` — final combined spectrum/DOS figure.

## Reproducing the figure

Use Python 3 with NumPy, SciPy, Matplotlib, and Jupyter Notebook. Run the calculation notebooks before the plotting notebooks when regenerating data. For the stored data supplied with the repository, the plotting notebooks can be run directly.

The displayed representative results use the parameter sets encoded in the data filenames, including $U$, $J$, chemical potential $\mu$, momentum-grid size, and spectral broadening $\gamma$ where applicable. `publication.mplstyle` should be available in the working directory when regenerating the publication-style figures.

## Output

The primary output is the superconducting single-particle spectrum together with the corresponding density of states at representative dopings. Normal-state DOS arrays with the `normal_dos_` prefix are included for direct comparison.
