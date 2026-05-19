$$
\chi_0^{a b}=\frac{1}{L^d} \sum_k n_{k \uparrow}^a n_{-k \downarrow}^b \frac{f\left(\omega_k^a\right)+f\left(\omega_{-k}^b\right)-1}{i \nu_n-\omega_k^a-\omega_{-k}^b}
$$

$$
\chi_0=\frac{1}{L^d} \sum_k n_{k \uparrow}^l n_{-k \downarrow}^l \frac{\tanh{(\beta\omega_k^l/2)}}{2\omega_k^l}+n_{k \uparrow}^u n_{-k \downarrow}^u \frac{\tanh{(\beta\omega_k^u/2)}}{2\omega_k^u}
$$


$$
\chi_0=\frac{1}{N} \sum_k \left\{\frac{\left(1-n_{k}\right)^2}{2 \xi_k} \tanh \left(\frac{\beta \xi_k}{2}\right)+\frac{n_{k}^2}{2\left(\xi_k+U\right)} \tanh \left(\beta \frac{\xi_k+U}{2}\right)\right\}
$$

$$
n(k)=\frac{f_F\left(\xi_{\mathbf{k}}\right)}{f_F\left(\xi_{\mathbf{k}}\right)+1-f_F\left(\xi_{\mathbf{k}}+U\right)}
$$

$$
\xi_{\mathbf{k}}=-2\left(t_x \cos k_x+t_y \cos k_y\right)-\mu
$$

$$
g\chi_0-1=0
$$

### HK model electron occupation

Single site Hubbard model
$$
H=\left(\varepsilon_k-\mu\right)\left(n_{ \uparrow}+n_{ \downarrow}\right)+U n_{ \uparrow} n_{ \downarrow}
$$
HK model in k space
$$
\hat{H}_{H K}=\sum_k \hat{H}_k=\sum_k\left[\left(\varepsilon_k-\mu\right)\left(\hat{n}_{k \uparrow}+\hat{n}_{k \downarrow}\right)+U \hat{n}_{k \uparrow} \hat{n}_{k \downarrow}\right]
$$

$$
\begin{aligned}
\mathcal{Z}=\operatorname{Tr} e^{-\beta \hat{H}}
&=\prod_k\sum_{\alpha_k=0, \uparrow, \downarrow, \uparrow \downarrow}\left\langle\left.\alpha_k\right| e^{-\beta \hat{H_k}} \mid \alpha_k\right\rangle\\
&=\prod_k\left(1+2 e^{-\beta\left(\varepsilon_k-\mu\right)}+e^{-\beta\left(2\varepsilon_k-2\mu+U\right)}\right)
\end{aligned}
$$

electron occupation

$n_{k \sigma}$ is the average occupation per spin

$\langle\uparrow\mid\hat{n}_{k \sigma}\mid\uparrow\rangle=\langle\downarrow\mid\hat{n}_{k \sigma}\mid\downarrow\rangle=1/2$

$\langle\uparrow\downarrow\mid\hat{n}_{k \sigma}\mid\uparrow\downarrow\rangle=1$
$$
\begin{aligned}
n_{k \sigma}
&=\frac{1}{\mathcal{Z}} \operatorname{Tr} \hat{n}_{k \sigma} e^{-\beta \hat{H}}\\
&=\frac{\sum_{\alpha_k=0, \uparrow, \downarrow, \uparrow \downarrow}\left\langle\left.\alpha_k\right| \hat{n}_{k \sigma}e^{-\beta \hat{H_k}} \mid \alpha_k\right\rangle}{1+2 e^{-\beta\left(\varepsilon_k-\mu\right)}+e^{-\beta\left(2\varepsilon_k-2\mu+U\right)}}\\
&=\frac{e^{-\beta\left(\varepsilon_k-\mu\right)}+e^{-\beta\left(2 \varepsilon_k-2 \mu+U\right)}}{1+2 e^{-\beta\left(\varepsilon_k-\mu\right)}+e^{-\beta\left(2\varepsilon_k-2\mu+U\right)}}
\end{aligned}
$$
half-filling

For $\varepsilon=0$, if $\mu=U/2$
$$
\begin{aligned}
n_{k \sigma}
&=\frac{e^{-\beta\left(-\mu\right)}+e^{-\beta\left(-2 \mu+U\right)}}{1+2 e^{-\beta\left(-\mu\right)}+e^{-\beta\left(-2\mu+U\right)}}\\
&=\frac{e^{\beta\left(U/2\right)}+e^{-\beta\left(0\right)}}{1+2 e^{\beta\left(U/2\right)}+e^{-\beta\left(0\right)}}\\
&=\frac{1}{2}
\end{aligned}
$$
$\mu=U/2$ is the half-filling point.

Or $\varepsilon-\mu=U/2$ is the half-filling point.



### HK model Tc

Green's function to get pair susceptibility

$$
\chi_0^{a b}(i\nu_0)=\frac{1}{L^d} \sum_k n_{k \uparrow}^a n_{-k \downarrow}^b \frac{f\left(\omega_k^a\right)+f\left(\omega_{-k}^b\right)-1}{i \nu_n-\omega_k^a-\omega_{-k}^b}
$$
for $T \ll U$, $f\left(\omega_k^l\right)+f\left(\omega_{-k}^u\right)-1\approx 1+0-1=0$

$\omega_k=\omega_{-k}$
$$
\chi_0(i\nu_n=0)\approx\frac{1}{L^d} \sum_k n_{k \uparrow}^l n_{-k \downarrow}^l \frac{\tanh{(\beta\omega_k^l/2)}}{2\omega_k^l}+n_{k \uparrow}^u n_{-k \downarrow}^u \frac{\tanh{(\beta\omega_k^u/2)}}{2\omega_k^u}
$$
The Green's function:
$$
G_{k \sigma}\left(i \omega_n \rightarrow \omega\right)=\frac{1-\left\langle n_{k \bar{\sigma}}\right\rangle}{\omega-\xi_k}+\frac{\left\langle n_{k \bar{\sigma}}\right\rangle}{\omega-\left(\xi_k+U\right)}
$$
$n_{k \sigma}^u=\left\langle n_{k \sigma}\right\rangle_0$, $n_{k \sigma}^l=1-n_{k o}^u$
$$
\chi_0=\frac{1}{N} \sum_k \left\{\frac{\left(1-n_{k}\right)^2}{2 \xi_k} \tanh \left(\frac{\beta \xi_k}{2}\right)+\frac{n_{k}^2}{2\left(\xi_k+U\right)} \tanh \left(\beta \frac{\xi_k+U}{2}\right)\right\}
$$

### Fermi arc model

$$
n_{k+Q}=\frac{\mathrm{e}^{-\beta \xi_{k+Q}}+\mathrm{e}^{-\beta\left(\xi_k+\xi_{k+Q}+\mathcal{V}\right)}}{1+\mathrm{e}^{-\beta \xi_k}+\mathrm{e}^{-\beta \xi_{k+Q}}+\mathrm{e}^{-\beta\left(\xi_k+\xi_{k+Q}+\mathcal{V}\right)}}
$$

$$
\begin{aligned}
\chi_0= & \frac{1}{N} \sum_{\boldsymbol{k}} \gamma_{\boldsymbol{k}}^2\left\{\frac{\left(1-n_{\boldsymbol{k}+\boldsymbol{Q}}\right)^2}{2 \xi_{\boldsymbol{k}}} \tanh \left(\frac{\beta \xi_{\boldsymbol{k}}}{2}\right)+\frac{n_{\boldsymbol{k}+\boldsymbol{Q}}^2}{2\left(\xi_{\boldsymbol{k}}+U\right)} \tanh \left(\beta \frac{\xi_{\boldsymbol{k}}+U}{2}\right)\right. \\
& \left.+\frac{n_{\boldsymbol{k}+\boldsymbol{Q}}\left(1-n_{\boldsymbol{k}+\boldsymbol{Q}}\right)}{2 \xi_{\boldsymbol{k}}+U}\left[\tanh \left(\frac{\beta \xi_{\boldsymbol{k}}}{2}\right)+\tanh \left(\beta \frac{\xi_{\boldsymbol{k}}+U}{2}\right)\right]\right\}
\end{aligned}
$$

reference:

1. Topic Review: Hatsugai-Kohmoto models: Exactly solvable playground for Mottness and Non-Fermi
   Liquid. **[ arXiv:2501.00388](https://arxiv.org/abs/2501.00388)**

2. Phillips, P.W., Yeo, L. & Huang, E.W. Exact theory for superconductivity in a doped Mott insulator. Nat. Phys. 16, 1175–1180 (2020). https://doi.org/10.1038/s41567-020-0988-4
