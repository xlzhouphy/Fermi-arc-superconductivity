### Fermi arc model

standard BCS wave function
$$
|\psi\rangle=\prod_{k}\left(u_k+v_kb_k^{\dagger}\right)|0\rangle
$$
$b_k^{\dagger}=\hat{c}_{k \uparrow}^{\dagger} \hat{c}_{-k \downarrow}^{\dagger}$

appendix:
$$
\langle\psi| n_{k \sigma}|\psi\rangle=|v_k|^2
$$

$$
H=\sum_{k\sigma}\left(\xi_kn_{k \sigma}+\frac{U}{2} n_{k \sigma} n_{k+Q  -\sigma}\right)-\frac{J}{N} \sum_{k, k^{\prime}} \gamma_{k,k'}c_{k\uparrow}^{\dagger} c_{-k, \downarrow}^{\dagger} c_{-k', \downarrow} c_{k', \uparrow}
$$

Sum of spin

$\sum_\sigma\frac{U}{2} n_{k \sigma} n_{k+Q  -\sigma}=U n_{k} n_{k+Q}$
$$
\begin{aligned}
\langle\psi| H|\psi\rangle= & \sum_{k} 2\xi_k|v_k|^2+U|v_k|^2|v_{k+Q}|^2 \\
& -\frac{J}{N} \sum_{k, k^{\prime}}\gamma_{k,k'}u_{k}v^*_{k}u^*_{k'}v_{k'}
\end{aligned}
$$

change variable
$$
u_k = \cos\theta_k\quad v_k =\sin\theta_k
$$

$$
\begin{aligned}
\langle\psi| H|\psi\rangle =&\sum_k\left[2\xi_k\sin^2\theta_k+U\sin^2\theta_k\sin^2\theta_{k+Q}\right] -\frac{J}{4N}\sum_{k, k^{\prime}}\gamma_{k,k'}\sin2\theta_k\sin2\theta_{k'}\\

=&\sum_k\left[\xi_k(1-\cos2\theta_k)+U\sin^2\theta_k\sin^2\theta_{k+Q}\right]-\frac{J}{4N}\sum_{k, k^{\prime}}\gamma_{k,k'}\sin2\theta_k\sin2\theta_{k'}

\end{aligned}
$$

$\gamma_{k,k'}=\gamma_k\times\gamma_{k'}$

Second term:
$$
\begin{aligned}
&\frac{\partial}{\partial\theta_k}\sum_pU\sin^2\theta_p\sin^2\theta_{p+Q}\\
=&\frac{\partial}{\partial\theta_k}U\left(\sin^2\theta_k\sin^2\theta_{k+Q}+\sin^2\theta_{k-Q}\sin^2\theta_{k}\right)\\
=&U\sin{2\theta_k}\sin^2\theta_{k+Q}+U\sin{2\theta_k}\sin^2\theta_{k-Q}

\end{aligned}
$$

$\sin^2\theta_{k-Q}=\sin^2\theta_{k-Q+G}=\sin^2\theta_{k+Q}$

Variational principle:
$$
\begin{aligned}
\frac{\partial}{\partial\theta_k}E=2\xi_k\sin2\theta_k+2U\sin2\theta_k\sin^2\theta_{k+Q}-\frac{J}{N}\gamma_k\cos2\theta_k\sum_{k'}\gamma_{k'}\sin2\theta_{k'}=0


\end{aligned}
$$

Gap:
$$
\Delta=\frac{J}{2N}\langle\hat\Delta^\dagger\rangle=\frac{J}{2N}\sum_{\mathbf{k}}\gamma_{\mathbf{k}}\sin2\theta_{\mathbf{k}}.
$$


### Appendix

1. $\langle\psi| n_{k \sigma}|\psi\rangle=|v_k|^2$

$$
\begin{aligned}
\langle T_k\rangle=&\langle\Psi_{\mathrm{G}}\mid\sum_{ \sigma} \xi_k c_{k \sigma}^{\dagger} c_{k \sigma}\mid\Psi_{\mathrm{G}}\rangle\\

=&\sum_\sigma\xi_k \langle0|\left(u^*_{\mathbf{-k}}+v^*_{\mathbf{-k}} \hat{c}_{\mathbf{k} \downarrow} \hat{c}_{-\mathbf{k} \uparrow}\right)\left(u^*_{\mathbf{k}}+v^*_{\mathbf{k}} \hat{c}_{-\mathbf{k} \downarrow} \hat{c}_{\mathbf{k} \uparrow}\right)|c_{k \sigma}^{\dagger} c_{k \sigma}|\left(u_{\mathbf{k}}+v_{\mathbf{k}} \hat{c}_{\mathbf{k} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k} \downarrow}^{\dagger}\right)\left(u_{-\mathbf{k}}+v_{-\mathbf{k}} \hat{c}_{-\mathbf{k} \uparrow}^{\dagger} \hat{c}_{\mathbf{k} \downarrow}^{\dagger}\right)|0\rangle\times\\

&\prod_{\mathbf{k'\neq k},\mathbf{k'\neq -k}}\langle0|\left(u^*_{\mathbf{k'}}+v^*_{\mathbf{k'}} \hat{c}_{-\mathbf{k'} \downarrow} \hat{c}_{\mathbf{k'} \uparrow}\right)|\left(u_{\mathbf{k'}}+v_{\mathbf{k'}} \hat{c}_{\mathbf{k'} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k'} \downarrow}^{\dagger}\right)|0\rangle\\

=&\xi_k \langle0|\left(u^*_{-\mathbf{k}}+v^*_{-\mathbf{k}} \hat{c}_{\mathbf{k} \downarrow} \hat{c}_{-\mathbf{k} \uparrow}\right)|c_{k \downarrow}^{\dagger} c_{k \downarrow}|\left(u_{-\mathbf{k}}+v_{-\mathbf{k}} \hat{c}_{-\mathbf{k} \uparrow}^{\dagger} \hat{c}_{\mathbf{k} \downarrow}^{\dagger}\right)|0\rangle+\xi_k \langle0|\left(u^*_{\mathbf{k}}+v^*_{\mathbf{k}} \hat{c}_{-\mathbf{k} \downarrow} \hat{c}_{\mathbf{k} \uparrow}\right)|c_{k \uparrow}^{\dagger} c_{k \uparrow}|\left(u_{\mathbf{k}}+v_{\mathbf{k}} \hat{c}_{\mathbf{k} \uparrow}^{\dagger} \hat{c}_{-\mathbf{k} \downarrow}^{\dagger}\right)|0\rangle\\

=&2\xi_k|v_{\mathbf{k}}|^2

\end{aligned}
$$

2. BCS theory

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





