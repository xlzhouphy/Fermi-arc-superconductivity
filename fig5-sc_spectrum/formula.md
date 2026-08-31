$$
\begin{aligned}
H&=H_0+H_\text{pair}\\

&=\sum_{\mathbf{k} \sigma}\left(\xi_{\mathbf{k}} \hat{n}_{\mathbf{k} \sigma}+\frac{U}{2} \hat{n}_{\mathbf{k} \sigma} \hat{n}_{\mathbf{k}+\mathbf{Q} \bar{\sigma}}\right)-\frac{J}{N} \sum_{\mathbf{k}, \mathbf{k}^{\prime}} g_{\mathbf{k}} g_{\mathbf{k}^{\prime}} c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger} c_{-\mathbf{k}^{\prime} \downarrow} c_{\mathbf{k}^{\prime} \uparrow}
\end{aligned}
$$

$$
\begin{aligned}
\hat{A}\hat{B}&=(\langle \hat{A} \rangle + \delta\langle\hat{A}\rangle)(\langle \hat{B} \rangle + \delta\langle\hat{B}\rangle)\\

&=\langle \hat{A} \rangle\langle \hat{B} \rangle+\delta\langle\hat{A}\rangle\langle \hat{B} \rangle+\langle\hat{A}\rangle\delta\langle \hat{B} \rangle+\delta\langle\hat{A}\rangle\delta\langle \hat{B} \rangle\\

&\approx\langle \hat{A} \rangle\langle \hat{B} \rangle+\delta\langle\hat{A}\rangle\langle \hat{B} \rangle+\langle\hat{A}\rangle\delta\langle \hat{B} \rangle\\

&=\hat{A}\langle \hat{B} \rangle+\langle\hat{A}\rangle \hat{B} -\langle \hat{A} \rangle\langle \hat{B} \rangle
\end{aligned}
$$

$$
\begin{aligned}
H_\text{pair}
&=-\frac{J}{N} \sum_{\mathbf{k}} g_{\mathbf{k}}  c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger}\sum_{ \mathbf{k}^{\prime}}g_{\mathbf{k}^{\prime}} c_{-\mathbf{k}^{\prime} \downarrow} c_{\mathbf{k}^{\prime} \uparrow}\\

&\approx-\frac{J}{N} \sum_{\mathbf{k}} g_{\mathbf{k}}  c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger}\sum_{ \mathbf{k}^{\prime}}g_{\mathbf{k}^{\prime}} \langle c_{-\mathbf{k}^{\prime} \downarrow} c_{\mathbf{k}^{\prime} \uparrow}\rangle-\frac{J}{N} \sum_{\mathbf{k}} g_{\mathbf{k}}  \langle c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger}\rangle\sum_{ \mathbf{k}^{\prime}}g_{\mathbf{k}^{\prime}} c_{-\mathbf{k}^{\prime} \downarrow} c_{\mathbf{k}^{\prime} \uparrow}+\text{const.}\\

&=\sum_{\mathbf{k}} g_{\mathbf{k}}\Delta_0  c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger}+\sum_{ \mathbf{k}}g_{\mathbf{k}}\Delta_0^* c_{-\mathbf{k} \downarrow} c_{\mathbf{k} \uparrow}+\text{const.}\\

&=\sum_{\mathbf{k}} \left(\Delta_{\mathbf{k}}  c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger}+\Delta_{\mathbf{k}}^* c_{-\mathbf{k} \downarrow} c_{\mathbf{k} \uparrow}\right)+\text{const.}\\


\end{aligned}
$$

$$
\Delta_0=-\frac{J}{N} \sum_{\mathbf{k}} g_{\mathbf{k}}\langle c_{-\mathbf k\downarrow} c_{\mathbf k\uparrow}\rangle
$$

$$
\Delta_{\mathbf{k}}=\Delta_0\left(\cos k_x-\cos k_y\right)
$$

Ignoring the constant
$$
H_\text{MF}=\sum_{\mathbf{k} \sigma}\left(\xi_{\mathbf{k}} \hat{n}_{\mathbf{k} \sigma}+\frac{U}{2} \hat{n}_{\mathbf{k} \sigma} \hat{n}_{\mathbf{k}+\mathbf{Q} \bar{\sigma}}\right)+\sum_{\mathbf{k} }\left(\Delta_{\mathbf{k}}c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger}+\Delta_{\mathbf{k}}^*c_{-\mathbf{k} \downarrow} c_{\mathbf{k} \uparrow}\right)
$$

$$
\begin{array}{ll}
\mathcal{A}: & (\mathbf{k} \uparrow, \mathbf{k}+\mathbf{Q} \downarrow,-\mathbf{k} \downarrow,-\mathbf{k}-\mathbf{Q} \uparrow), \\
\mathcal{B}: & (\mathbf{k} \downarrow, \mathbf{k}+\mathbf{Q} \uparrow,-\mathbf{k} \uparrow,-\mathbf{k}-\mathbf{Q} \downarrow) .
\end{array}
$$

$$
\boxed{
\begin{aligned}
H_{\mathcal A}
={}&
(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q})
\oplus
\left(H_{S_z=1}^{(a)}\oplus H_{S_z=1}^{(d)}\right) \\
& \oplus
\left[
H_{S_z=0}^{(4)}
\oplus
(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U)
\oplus
(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q}+U)
\right] \\
& \oplus
\left(H_{S_z=-1}^{(b)}\oplus H_{S_z=-1}^{(c)}\right)
\oplus
(\xi_{\mathbf k}+\xi_{\mathbf{k}+\mathbf Q})
\end{aligned}
}
$$

Single-particle excitation
$$
A(k, \omega)=\sum_{n m}|\langle n| c_k| m\rangle\left.\right|^ 2\left(\rho_n+\rho_m\right) \delta\left(\omega+E_n-E_m\right),
$$






