# BCS theory

[toc]

## 1. Cooper instability （Cooper pair）

Two electron Schrodinger equation
$$
H=-\frac{\nabla_1^2+\nabla_2^2}{2 m}+V\left(r_1-r_2\right)
$$
$R=\left(r_1+r_2\right) / 2$$, $$r=r_1-r_2$
$$
H=-\frac{1}{4 m} \frac{\partial^2}{\partial R^2}-2 \frac{1}{2 m} \frac{\partial^2}{\partial r^2}+V(r)
$$

$$
\Psi\left(r_1, r_2\right)=\Psi(R, r)=\frac{1}{\sqrt{V}} e^{i \vec{q} \cdot \vec{R}} \psi(r)
$$

Goal: Find the lowest energy (states) for attractive interaction $V$.

To minimize the total energy of two electron systems, $q=0$, the total kinetic energy =0. So the two electrons have opposite moment $\vec{k}$ and $-\vec{k}$.

To enhance the attractive interaction (short-range interaction) of two electrons, the spatial wavefunction should overlap, which yields the **symmetric spatial wavefunction** (recall covalent bond), and **antisymmetric spin wave function** ( exchange terms reduce the interaction for parallel spins.):
$$
\begin{aligned}
\Psi\left(r_1, r_2\right)&=\sum_{k>k_f} g_k\frac{1}{\sqrt{2}}\left[e^{i\vec{k}\cdot\vec{r_1}}e^{-i\vec{k}\cdot\vec{r_2}}+e^{i\vec{k}\cdot\vec{r_2}}e^{-i\vec{k}\cdot\vec{r_1}}\right]\frac{1}{\sqrt{2}}[|\uparrow \downarrow\rangle-|\downarrow \uparrow|]
\\
&=\sum_{k>k_f} g_k \cos \left[\vec{k} \cdot\left(\vec{r_1}-\vec{r_2}\right)\right][|\uparrow \downarrow\rangle-|\downarrow \uparrow|]
\\
&=\sum_{k>k_f} g_k \cos \left[\vec{k} \cdot\vec{r}\right][|\uparrow \downarrow\rangle-|\downarrow \uparrow|]
\end{aligned}
$$

$$
H \Psi=E \Psi \Rightarrow\left[-2 \frac{1}{2 m} \frac{\partial^2}{\partial r^2}+V(r)\right] \psi(r)=E \psi(r)
$$

$$
\left(E-2 \varepsilon_{\vec{k}}\right) g_{\vec{k}}=\sum_{k^{\prime}} V_{\vec{k}- \vec{k}^{\prime}} g_{\vec{k}^{\prime}}
$$

Cooper assumption of the attraction potential
$$
V_{k-k}=\left\{\begin{array}{c}
-V, \quad 0<\varepsilon_k, \varepsilon_{\bar{k}}<\omega_D \\
0, \text { otherwise }
\end{array}\right\}
$$

$$
g_k=V \sum_{k^{\prime}} \frac{g_k^{\prime}}{2 \varepsilon_{k}-E}
$$

sum over k
$$
\frac{1}{V}=\sum_{k>k_f} \frac{1}{2 \varepsilon_k-E }
$$

$$
\frac{1}{V}=N\left(\varepsilon_f\right) \int_{\varepsilon_f}^{\varepsilon_f+h \omega_D} \frac{d \varepsilon}{2 \varepsilon-E}=\frac{1}{2} N\left(\varepsilon_f\right) \ln \left(\frac{2 \varepsilon_f-\varepsilon+h \omega_D}{2 \epsilon_f-E}\right)
$$

$$
\frac{2}{N\left(\varepsilon_f\right) V}=\ln \left(\frac{2 \varepsilon_f-\varepsilon+h \omega_D}{2 \epsilon_f-E}\right)
$$

$$
\frac{2 \varepsilon_f-E+2 \hbar \omega_D}{2 \varepsilon_f-E}=e^{2 / N\left(\varepsilon_f\right) V}
$$

$$
2 \varepsilon_f-E=(2 \varepsilon_f-E+2 \hbar \omega_D)e^{-2 / N\left(\varepsilon_f\right) V}
$$

$$
\boxed{E_{min}\approx2 \varepsilon_f-2 \hbar \omega_De^{-2 / N\left(\varepsilon_f\right) V}<2 \varepsilon_f}
$$

Non-analytic: No order of perturbation theory can give this result.

Fermi surface?screening?



## 2. BCS theory

Based on Cooper instability, BCS theory guess a variational many-body ground state wavefunction:(BCS Ansatz)
$$
\left|\Psi_{\mathrm{BCS}}\right\rangle=\prod_{\mathbf{k}}\left(u_{\mathbf{k}}+v_{\mathbf{k}} \hat{c}_{\mathbf{k} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k} \downarrow}^{\dagger}\right)|0\rangle
$$
For comparison, Fermi sea:
$$
|\mathrm{FS}\rangle=\prod_{\mathbf{k}, \sigma}^{\epsilon_{\mathbf{k}}<E_F} \hat{c}_{\mathbf{k} \sigma}^{\dagger}|0\rangle
$$
$\prod_{\mathbf{k}}$ Mean-Field (Hartree-like) approximation, $u_{\mathbf{k}}+v_{\mathbf{k}} \hat{c}_{\mathbf{k} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k} \downarrow}^{\dagger}$ superposition of normal states and cooper pair states.

Coherent Boson state:
$$
\begin{aligned}
\left|\psi_{B C S}\right\rangle & =\prod_k\left(\mu_k+\nu_k \hat{c}_{k \uparrow}^{\dagger} \hat{c}_{-k \downarrow}^{\dagger}\right)|0\rangle=\prod_k \mu_k\left(1+\frac{\nu_k}{\mu_k} \hat{c}_{k \uparrow}^{\dagger} \hat{c}_{-k \downarrow}^{\dagger}\right)|0\rangle \\
& =\prod_k e^{\frac{\nu_k}{\mu_k} \hat{c}_{k \uparrow}^{\dagger} \hat{c}_{-k \downarrow}^{\dagger}}|0\rangle \sim e^{\sum_k \frac{\nu_k}{\mu_k} \hat{c}_{k \uparrow}^{\dagger} \hat{c}_{-k \downarrow}^{\dagger}}|0\rangle
\end{aligned}
$$

$$
H=\sum_{\mathbf{k} \sigma} \epsilon_{\mathbf{k} \sigma} c_{\mathbf{k} \sigma}^{\dagger} c_{\mathbf{k} \sigma}+\sum_{\mathbf{k}, \mathbf{k}^{\prime}} V_{\mathbf{k}, \mathbf{k}^{\prime}} c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger} c_{-\mathbf{k}^{\prime} \downarrow} c_{\mathbf{k}^{\prime} \uparrow}
$$



| 理论 | 目标 | 哈密顿量 $\hat{H}$ | 试探波函数 $|\Psi\rangle$ | 近似层次 |
| :--- | :--- | :--- | :--- | :--- |
| Hartree-Fock | 求解 $\hat{H}_{\text{Coulomb}}$ | 完整的多体哈密顿量（库仑相互作用） | Slater 行列式 (独立粒子乘积态) | 仅近似波函数（独立粒子）|
| BCS 理论 | 求解超导基态 | $\hat{H}_{\text{BCS}}$（一个简化的、截断的有效哈密顿量）| BCS 态 (独立对乘积态) | 近似哈密顿量 + 近似波函数|

General interaction term:
$$
V=\sum_{k, k^{\prime}, q, \sigma, \sigma^{\prime}} V_q \hat{c}_{k+q \sigma}^{\dagger} \hat{c}_{k^{\prime}-q \sigma^{\prime}}^{\dagger} \hat{c}_{k^{\prime} \sigma^{\prime}} \hat{c}_{k \sigma}
$$
BCS term:
$$
V_{BCS}=\sum_{\mathbf{k}, \mathbf{k}^{\prime}} V_{\mathbf{k}, \mathbf{k}^{\prime}} c_{\mathbf{k} \uparrow}^{\dagger} c_{-\mathbf{k} \downarrow}^{\dagger} c_{-\mathbf{k}^{\prime} \downarrow} c_{\mathbf{k}^{\prime} \uparrow}
$$
only allow $\left(\mathbf{k}^{\prime},-\mathbf{k}^{\prime}\right) \rightarrow(\mathbf{k},-\mathbf{k})$


$$
\frac{1}{V}=\frac{1}{\text{Volume}}\sum_{\mathbf{k}} \frac{g(\mathbf{k})^2}{2 E_{\mathbf{k}}} \tanh \left(\frac{E_{\mathbf{k}}}{2 k_B T}\right)
$$
s-wave:

$k_B=1$
$$
\int_0^{\hbar \omega_D} \mathrm{d} E\left[\frac{\tanh \left(\frac{1}{2 T} \sqrt{E^2+\Delta^2}\right)}{\sqrt{E^2+\Delta^2}}-\frac{1}{E} \tanh \left(\frac{E}{2 T_C}\right)\right]=0
$$

$$
\int_{-\hbar\Theta_D}^{\hbar\Theta_D} d \xi \frac{1}{2 \sqrt{\xi^2+\Delta^2}} \tanh \frac{\sqrt{\xi^2+\Delta^2}}{2 T}-\frac{1}{V N(E_f)}=0
$$

1. $T=0$

$$
\frac{1}{V N(E_f)}=  \int_0^{\hbar\Theta_D} d \xi \frac{1}{ \sqrt{\xi^2+\Delta^2}}
$$

$$
\int d x \frac{1}{\sqrt{x^2+a^2}}=\ln \left(x+\sqrt{x^2+a^2}\right)
$$

$$
\frac{1}{V N(E_f)}=\ln\left(\frac{\hbar\Theta_D+\sqrt{\hbar^2\Theta_D^2+\Delta^2}}{\Delta}\right)
$$

$$
\begin{aligned}
\Delta(0)&=\left(\hbar\Theta_D+\sqrt{\hbar^2\Theta_D^2+\Delta^2}\right)e^{-\frac{1}{V N(E_f)}}\\
&\approx 2\hbar\Theta_De^{-\frac{1}{V N(E_f)}}
\end{aligned}
$$

if $V N(E_f)\ll 1$, $\hbar\Theta_D\gg\Delta$

2. $\Delta=0$

$$
\int_{0}^{\hbar\Theta_D} d \xi \frac{1}{ \xi} \tanh \frac{\xi}{2 T_c}-\frac{1}{V N(E_f)}=0
$$

$$
\begin{aligned}
T_c&\approx\frac{2e^\gamma}{\pi}\hbar\Theta_De^{-\frac{1}{V N(E_f)}}\\
&\approx1.13\hbar\Theta_De^{-\frac{1}{V N(E_f)}}
\end{aligned}
$$

$\gamma\approx0.5772$ is Euler constant.

3. Universal scaling

$$
\frac{2\Delta(0)}{T_c}=2\pi e^{-\gamma}\approx3.53
$$

$2\Delta(0)$ is the minimum excitation energy of a Cooper pair. 
$$
\left.\alpha_k^{+} \alpha_{-k}^{+}|0>\equiv| \text { Cooper~pair }\right\rangle
$$

$$
\begin{aligned}
& <\text { Cooper~pair  }|\bar{H}| \text { Cooper~pair  }>-<0|\bar{H}| 0> \\
& =\sum_{k^{\prime}} \xi_{k^{\prime}}<0\left|\alpha_{-k} \alpha_k\left(\alpha_{k^{\prime}}^{+} \alpha_{k^{\prime}}+\alpha_{-k^{\prime}}^{+} \alpha_{-k^{\prime}}\right) \alpha_k^{+} \alpha_{-k}^{+}\right| 0> \\
& =2 \xi_k\\
&=2\sqrt{\varepsilon_k^2+\Delta^2}
\end{aligned}
$$

d-wave:
$$
\int_0^{2\pi}\frac{d\varphi}{2\pi}\int_{-\hbar\Theta_D}^{\hbar\Theta_D} d \xi \frac{\gamma_\varphi^2}{2 \sqrt{\xi^2+\Delta^2\gamma_\varphi^2}} \tanh \frac{\sqrt{\xi^2+\Delta^2\gamma_\varphi^2}}{2 T}-\frac{1}{V N(E_f)}=0
$$


$$
\gamma=\cos(k_x)-\cos(k_y)
$$
around Fermi surface
$$
\gamma_\varphi=\cos(2\varphi)
$$







Reference:

兰州大学钟寅老师的《凝聚态物理学导论》第十三章：“超导：拥有BCS理论的幸运？”

https://www.youtube.com/watch?v=Qlzkkjvi5EM&list=PLwdnzlV3ogoU1IvWa-_5u9iGVimN2uT3h&index=4

李正中固体理论第六章

向涛d波超导体

翟荟冷原子物理课程视频第六章



## BCS variational method

$$
\left|\Psi_{\mathrm{G}}\right\rangle=\prod_{\mathbf{k}}\left(u_{\mathbf{k}}+v_{\mathbf{k}} \hat{c}_{\mathbf{k} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k} \downarrow}^{\dagger}\right)|0\rangle
$$

$$
H=\sum_{k\sigma}\left(\epsilon_k-\mu\right) c_{k \sigma}^{\dagger} c_{k \sigma}-\frac{g}{V} \sum_{k, k^{\prime}}\gamma_{k,k'} c_{k \uparrow}^{\dagger} c_{-k, \downarrow}^{\dagger} c_{-k', \downarrow} c_{k', \uparrow}
$$

Normalization condition
$$
\langle0|\left(u^*_{\mathbf{k}}+v^*_{\mathbf{k}} \hat{c}_{-\mathbf{k} \downarrow} \hat{c}_{\mathbf{k} \uparrow}\right)|\left(u_{\mathbf{k}}+v_{\mathbf{k}} \hat{c}_{\mathbf{k} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k} \downarrow}^{\dagger}\right)|0\rangle=|u_{\mathbf{k}}|^2+|v_{\mathbf{k}}|^2=1
$$

$$
\langle0|\left(u^*_{\mathbf{k'}}+v^*_{\mathbf{k'}} \hat{c}_{-\mathbf{k'} \downarrow} \hat{c}_{\mathbf{k'} \uparrow}\right)|\left(u_{\mathbf{k}}+v_{\mathbf{k}} \hat{c}_{\mathbf{k} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k} \downarrow}^{\dagger}\right)|0\rangle=0
$$

kinetic term
$$
\begin{aligned}
\langle T_k\rangle=&\langle\Psi_{\mathrm{G}}\mid\sum_{ \sigma} \xi_k c_{k \sigma}^{\dagger} c_{k \sigma}\mid\Psi_{\mathrm{G}}\rangle\\

=&\sum_\sigma\xi_k \langle0|\left(u^*_{\mathbf{-k}}+v^*_{\mathbf{-k}} \hat{c}_{\mathbf{k} \downarrow} \hat{c}_{-\mathbf{k} \uparrow}\right)\left(u^*_{\mathbf{k}}+v^*_{\mathbf{k}} \hat{c}_{-\mathbf{k} \downarrow} \hat{c}_{\mathbf{k} \uparrow}\right)|c_{k \sigma}^{\dagger} c_{k \sigma}|\left(u_{\mathbf{k}}+v_{\mathbf{k}} \hat{c}_{\mathbf{k} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k} \downarrow}^{\dagger}\right)\left(u_{-\mathbf{k}}+v_{-\mathbf{k}} \hat{c}_{-\mathbf{k} \uparrow}^{\dagger} \hat{c}_{\mathbf{k} \downarrow}^{\dagger}\right)|0\rangle\times\\

&\prod_{\mathbf{k'\neq k},\mathbf{k'\neq -k}}\langle0|\left(u^*_{\mathbf{k'}}+v^*_{\mathbf{k'}} \hat{c}_{-\mathbf{k'} \downarrow} \hat{c}_{\mathbf{k'} \uparrow}\right)|\left(u_{\mathbf{k'}}+v_{\mathbf{k'}} \hat{c}_{\mathbf{k'} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k'} \downarrow}^{\dagger}\right)|0\rangle\\

=&\xi_k \langle0|\left(u^*_{-\mathbf{k}}+v^*_{-\mathbf{k}} \hat{c}_{\mathbf{k} \downarrow} \hat{c}_{-\mathbf{k} \uparrow}\right)|c_{k \downarrow}^{\dagger} c_{k \downarrow}|\left(u_{-\mathbf{k}}+v_{-\mathbf{k}} \hat{c}_{-\mathbf{k} \uparrow}^{\dagger} \hat{c}_{\mathbf{k} \downarrow}^{\dagger}\right)|0\rangle+\xi_k \langle0|\left(u^*_{\mathbf{k}}+v^*_{\mathbf{k}} \hat{c}_{-\mathbf{k} \downarrow} \hat{c}_{\mathbf{k} \uparrow}\right)|c_{k \uparrow}^{\dagger} c_{k \uparrow}|\left(u_{\mathbf{k}}+v_{\mathbf{k}} \hat{c}_{\mathbf{k} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k} \downarrow}^{\dagger}\right)|0\rangle\\

=&2\xi_k|v_{\mathbf{k}}|^2

\end{aligned}
$$
Inversion symmetry $v_{\mathbf{k}}=v_{-\mathbf{k}}$

Total kinetic term 
$$
\langle T\rangle=\sum_k\langle T_k\rangle=2\sum_k\xi_k|v_{\mathbf{k}}|^2
$$
Coulomb interaction term （omit $k=k'$ term）
$$
\begin{aligned}
\langle V\rangle=&\langle\Psi_{\mathrm{G}}\mid-\frac{g}{V} \sum_{k, k^{\prime}}\gamma_{k,k'} c_{k, \uparrow}^{\dagger} c_{-k, \downarrow}^{\dagger} c_{-k', \downarrow} c_{k', \uparrow}\mid\Psi_{\mathrm{G}}\rangle\\

=&-\frac{g}{V}\sum_{k, k^{\prime}}\gamma_{k,k'}\langle0\mid\left(u^*_{\mathbf{k}}+v^*_{\mathbf{k}} \hat{c}_{-\mathbf{k} \downarrow} \hat{c}_{\mathbf{k} \uparrow}\right)\left(u^*_{\mathbf{k'}}+v^*_{\mathbf{k'}} \hat{c}_{-\mathbf{k'} \downarrow} \hat{c}_{\mathbf{k'} \uparrow}\right)\mid c_{k \uparrow}^{\dagger} c_{-k, \downarrow}^{\dagger} c_{-k', \downarrow} c_{k', \uparrow}\mid\left(u_{\mathbf{k'}}+v_{\mathbf{k'}} \hat{c}_{\mathbf{k'} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k'} \downarrow}^{\dagger}\right)\left(u_{\mathbf{k}}+v_{\mathbf{k}} \hat{c}_{\mathbf{k} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k} \downarrow}^{\dagger}\right)\mid 0\rangle\\\

=&-\frac{g}{V}\sum_{k, k^{\prime}}\gamma_{k,k'}\langle0\mid\left(u^*_{\mathbf{k}}+v^*_{\mathbf{k}}  \hat{b}_{\mathbf{k} }\right)\left(u^*_{\mathbf{k'}}+v^*_{\mathbf{k'}} \hat{b}_{\mathbf{k'}}\right)\mid\hat{b}_{k }^{\dagger} \hat{b}_{k'}\mid\left(u_{\mathbf{k'}}+v_{\mathbf{k'}}  \hat{b}_{\mathbf{k'} }^{\dagger}\right)\left(u_{\mathbf{k}}+v_{\mathbf{k}} \hat{b}_{\mathbf{k} }^{\dagger} \right)\mid0\rangle\\

=&-\frac{g}{V}\sum_{k, k^{\prime}}\gamma_{k,k'}\langle0\mid(u^*_{\mathbf{k}}u^*_{\mathbf{k'}}+u^*_{\mathbf{k}}v^*_{\mathbf{k'}}\hat{b}_{\mathbf{k'}}+v^*_{\mathbf{k}}u^*_{\mathbf{k'}}\hat{b}_{\mathbf{k}}+v^*_{\mathbf{k}}v^*_{\mathbf{k'}}\hat{b}_{\mathbf{k}}\hat{b}_{\mathbf{k'}})\mid\hat{b}_{k }^{\dagger} \hat{b}_{k'}\mid(u_{\mathbf{k}}u_{\mathbf{k'}}+u_{\mathbf{k}}v_{\mathbf{k'}}\hat{b}^\dagger_{\mathbf{k'}}+v_{\mathbf{k}}u_{\mathbf{k'}}\hat{b}^\dagger_{\mathbf{k}}+v_{\mathbf{k}}v_{\mathbf{k'}}\hat{b}^\dagger_{\mathbf{k'}}\hat{b}^\dagger_{\mathbf{k}})\mid0\rangle\\

=&-\frac{g}{V}\sum_{k, k^{\prime}}\gamma_{k,k'}v^*_{\mathbf{k}}u^*_{\mathbf{k'}}u_{\mathbf{k}}v_{\mathbf{k'}}\\

=&-\frac{g}{V}\sum_{k, k^{\prime}}\gamma_{k,k'}u_{\mathbf{k}}v^*_{\mathbf{k}}u^*_{\mathbf{k'}}v_{\mathbf{k'}}




\end{aligned}
$$


$$
E =2\sum_k\xi_k|v_{\mathbf{k}}|^2-\frac{g}{V}\sum_{k, k^{\prime}}\gamma_{k,k'}u_{\mathbf{k}}v^*_{\mathbf{k}}u^*_{\mathbf{k'}}v_{\mathbf{k'}}
$$
Since $|u_{\mathbf{k}}|^2+|v_{\mathbf{k}}|^2=1$

we can parameterize (real?):
$$
u_k = \cos\theta_k\quad v_k =\sin\theta_k
$$

$$
\begin{aligned}
E =&2\sum_k\xi_k\sin^2\theta_k -\frac{g}{4V}\sum_{k, k^{\prime}}\gamma_{k,k'}\sin2\theta_k\sin2\theta_{k'}\\

=&\sum_k\xi_k(1-\cos2\theta_k)-\frac{g}{4V}\sum_{k, k^{\prime}}\gamma_{k,k'}\sin2\theta_k\sin2\theta_{k'}

\end{aligned}
$$

suppose
$$
\gamma_{k,k'}=\gamma_k\times\gamma_{k'}
$$
variation (double summation)
$$
\begin{aligned}
\frac{\partial}{\partial\theta_k}E=2\xi_k\sin2\theta_k-\frac{g}{V}\gamma_k\cos2\theta_k\sum_{k'}\gamma_{k'}\sin2\theta_{k'}=0


\end{aligned}
$$

define
$$
\Delta_k =\frac{g}{2V}\gamma_k\sum_{k'}\gamma_{k'}\sin2\theta_{k'}
$$

put it back
$$
\tan2\theta_k=\frac{\Delta_k}{\xi_k}
$$

$$
\sin2\theta_k=\frac{\Delta_k}{\sqrt{\Delta_k^2+\xi_k^2}}
$$

$$
\cos2\theta_k=\frac{\xi_k}{\sqrt{\Delta_k^2+\xi_k^2}}
$$

put $\sin2\theta_k$ back to the definition of gap, we can get the self-consistent gap function:
$$
\begin{aligned}
\Delta_k =&\frac{g}{2V}\sum_{k'}\gamma_k\gamma_{k'}\frac{\Delta_{k'}}{\sqrt{\Delta_{k'}^2+\xi_{k'}^2}}\\

\end{aligned}
$$
suppose $\Delta_k=\Delta\gamma_k$

$$
\begin{aligned}
\Delta\gamma_k =&\frac{g}{2V}\sum_{k'}\gamma_k\gamma_{k'}\frac{\Delta\gamma_k'}{\sqrt{\Delta_{k'}^2+\xi_{k'}^2}}\\

1=&\frac{g}{V}\sum_{k}\frac{\gamma_k^2}{2\sqrt{\Delta_{k}^2+\xi_{k}^2}}\\

\end{aligned}
$$
$$
1=\frac{g}{V}\sum_{\mathbf{k}} \frac{\gamma_k^2}{2 \sqrt{\Delta_{k}^2+\xi_{k}^2}} \tanh \left(\frac{\sqrt{\Delta_{k}^2+\xi_{k}^2}}{2 k_B T}\right)
$$



self consistent equation


appendix
$$
\begin{aligned}
&\langle\Psi_{\mathrm{G}}\mid c_{-k', \downarrow} c_{k', \uparrow}\mid\Psi_{\mathrm{G}}\rangle\\

=&\langle0\mid\left(u^*_{\mathbf{k}}+v^*_{\mathbf{k}}  \hat{b}_{\mathbf{k} }\right)\left(u^*_{\mathbf{k'}}+v^*_{\mathbf{k'}} \hat{b}_{\mathbf{k'}}\right)\mid \hat{b}_{k'}\mid\left(u_{\mathbf{k'}}+v_{\mathbf{k'}}  \hat{b}_{\mathbf{k'} }^{\dagger}\right)\left(u_{\mathbf{k}}+v_{\mathbf{k}} \hat{b}_{\mathbf{k} }^{\dagger} \right)\mid0\rangle\\

=&\langle0\mid(u^*_{\mathbf{k}}u^*_{\mathbf{k'}}+u^*_{\mathbf{k}}v^*_{\mathbf{k'}}\hat{b}_{\mathbf{k'}}+v^*_{\mathbf{k}}u^*_{\mathbf{k'}}\hat{b}_{\mathbf{k}}+v^*_{\mathbf{k}}v^*_{\mathbf{k'}}\hat{b}_{\mathbf{k}}\hat{b}_{\mathbf{k'}})\mid\hat{b}_{k'}\mid(u_{\mathbf{k}}u_{\mathbf{k'}}+u_{\mathbf{k}}v_{\mathbf{k'}}\hat{b}^\dagger_{\mathbf{k'}}+v_{\mathbf{k}}u_{\mathbf{k'}}\hat{b}^\dagger_{\mathbf{k}}+v_{\mathbf{k}}v_{\mathbf{k'}}\hat{b}^\dagger_{\mathbf{k'}}\hat{b}^\dagger_{\mathbf{k}})\mid0\rangle\\

=&\langle0\mid(u^*_{\mathbf{k}}u^*_{\mathbf{k'}}+u^*_{\mathbf{k}}v^*_{\mathbf{k'}}\hat{b}_{\mathbf{k'}}+v^*_{\mathbf{k}}u^*_{\mathbf{k'}}\hat{b}_{\mathbf{k}}+v^*_{\mathbf{k}}v^*_{\mathbf{k'}}\hat{b}_{\mathbf{k}}\hat{b}_{\mathbf{k'}})\mid(u_{\mathbf{k}}v_{\mathbf{k'}}+v_{\mathbf{k}}v_{\mathbf{k'}}\hat{b}^\dagger_{\mathbf{k}})\mid0\rangle\\

=&u^*_{\mathbf{k}}u^*_{\mathbf{k'}}u_{\mathbf{k}}v_{\mathbf{k'}}+v^*_{\mathbf{k}}u^*_{\mathbf{k'}}v_{\mathbf{k}}v_{\mathbf{k'}}\\

=&u^*_{\mathbf{k'}}v_{\mathbf{k'}}(|u_{\mathbf{k}}|^2+|v_{\mathbf{k}}|^2)\\

=&u^*_{\mathbf{k'}}v_{\mathbf{k'}}

\end{aligned}
$$

double summation
$$
\begin{aligned}
&\frac{\partial}{\partial\theta_{k_0}}\left[\sum_{k, k^{\prime}}\gamma_{k,k'}\sin2\theta_k\sin2\theta_{k'}\right]\\

=&\frac{\partial}{\partial\theta_{k_0}}\left[\gamma_{k_0,k_0}\sin^22\theta_{k_0}+\sum_{k\neq k_0}\gamma_{k_0,k}\sin2\theta_{k_0}\sin2\theta_{k}+\sum_{k\neq k_0}\gamma_{k,k_0}\sin2\theta_{k}\sin2\theta_{k_0}\right]\\

=&4\gamma_{k_0,k_0}\sin2\theta_{k_0}\cos2\theta_{k_0}+2\sum_{k\neq k_0}\gamma_{k_0,k}\cos2\theta_{k_0}\sin2\theta_{k}+2\sum_{k\neq k_0}\gamma_{k,k_0}\sin2\theta_{k}\cos2\theta_{k_0}\\

=&4\sum_{k}\gamma_{k,k_0}\sin2\theta_{k}\cos2\theta_{k_0}

\end{aligned}
$$







