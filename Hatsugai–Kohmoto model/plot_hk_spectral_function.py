import numpy as np
import matplotlib.pyplot as plt


def lorentzian(x, gamma):
    """Normalized Lorentzian used to broaden delta functions."""
    return gamma / np.pi / (x**2 + gamma**2)


def hk_spectral_function(k_values, omega_values, t=1.0, mu=0.0, U=4.0, beta=20.0, gamma=0.05):
    """
    Spectral function of the Hatsugai-Kohmoto model.

    The exact result is

        A_sigma(k, omega)
        =
        [(1 + exp(-beta xi_k)) / Z_k] delta(omega - xi_k)
        +
        [(exp(-beta xi_k) + exp(-beta(2 xi_k + U))) / Z_k]
        delta(omega - xi_k - U),

    where

        xi_k = epsilon_k - mu,
        epsilon_k = -2 t cos(k),
        Z_k = 1 + 2 exp(-beta xi_k) + exp(-beta(2 xi_k + U)).

    For plotting, each delta function is replaced by a Lorentzian
    with width gamma.
    """
    k_grid, omega_grid = np.meshgrid(k_values, omega_values)

    epsilon_k = -2.0 * t * np.cos(k_grid)
    xi_k = epsilon_k - mu

    weight_1 = 1.0 + np.exp(-beta * xi_k)
    weight_2 = np.exp(-beta * xi_k) + np.exp(-beta * (2.0 * xi_k + U))
    z_k = 1.0 + 2.0 * np.exp(-beta * xi_k) + np.exp(-beta * (2.0 * xi_k + U))

    peak_1 = (weight_1 / z_k) * lorentzian(omega_grid - xi_k, gamma)
    peak_2 = (weight_2 / z_k) * lorentzian(omega_grid - xi_k - U, gamma)

    return peak_1 + peak_2


# Model and plotting parameters.
t = 1.0
U = 4.0
mu = U / 2.0
beta = 20.0
gamma = 0.06

nk = 401
nw = 600
k_values = np.linspace(-np.pi, np.pi, nk)
omega_values = np.linspace(-4.5, 4.5, nw)

spectral_weight = hk_spectral_function(
    k_values,
    omega_values,
    t=t,
    mu=mu,
    U=U,
    beta=beta,
    gamma=gamma,
)

plt.figure(figsize=(7.2, 5.2), dpi=160)
plt.imshow(
    spectral_weight,
    origin="lower",
    aspect="auto",
    extent=[k_values[0], k_values[-1], omega_values[0], omega_values[-1]],
    cmap="magma",
)
plt.colorbar(label=r"$A_\sigma(k,\omega)$")
plt.xlabel(r"$k$")
plt.ylabel(r"$\omega$")
plt.title(rf"HK spectral function, $U={U}$, $\mu={mu}$, $\beta={beta}$, $\gamma={gamma}$")
plt.xticks(
    [-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
    [r"$-\pi$", r"$-\pi/2$", r"$0$", r"$\pi/2$", r"$\pi$"],
)
plt.tight_layout()
plt.savefig("hk_spectral_function.png", bbox_inches="tight")
plt.close()
