HK model variational method

generalized BCS variation wave function
$$
|\psi\rangle=\prod_{k>0}\left(x_k+y_k b_k^{\dagger} b_{-k}^{\dagger}+\frac{z_k}{\sqrt{2}}\left(b_k^{\dagger}+b_{-k}^{\dagger}\right)\right)|0\rangle
$$

$$
\left|x_k\right|^2+\left|y_k\right|^2+\left|z_k\right|^2=1
$$

$$
\begin{aligned}
H=&\sum_k\left(\xi_k\left(n_{k \uparrow}+n_{k \downarrow}\right)+U n_{k \uparrow} n_{k \downarrow}\right)-\frac{g}{L^d} \sum_{k, k^{\prime}} c_{k \uparrow}^{\dagger} c_{-k, \downarrow}^{\dagger} c_{-k', \downarrow} c_{k', \uparrow}\\

=&\sum_k\left(\xi_k\left(n_{k \uparrow}+n_{k \downarrow}\right)+U n_{k \uparrow} n_{k \downarrow}\right)-\frac{g}{L^d} \sum_{k, k^{\prime}} b_{k }^{\dagger}  b_{k'}


\end{aligned}
$$

$$
\langle\psi| n_{k \sigma}|\psi\rangle=\left|y_k\right|^2+\frac{\left|z_k\right|^2}{2}
$$

$$
\langle\psi| n_{k \uparrow} n_{k \downarrow}|\psi\rangle=\left|y_k\right|^2
$$

$$
\langle\psi| b_k^{\dagger} b_k|\psi\rangle=\left|y_k\right|^2+\frac{\left|z_k\right|^2}{2}
$$

$$
\langle\psi| b_k^{\dagger} b_p|\psi\rangle=\frac{1}{2}\left(z_k^* x_k+y_k^* z_k\right)\left(x_p^* z_p+z_p^* y_p\right)
$$

Approximation 1 (throw $\langle\psi| b_k^{\dagger} b_k|\psi\rangle$ term)

inversion symmetry $k\rarr-k$
$$
\begin{aligned}
\langle\psi| H|\psi\rangle= & \sum_{k>0} \xi_k\left(4\left|y_k\right|^2+2\left|z_k\right|^2\right)+U\left(2\left|y_k\right|^2\right) \\
& -g^{\prime} \sum_{k, p>0 ; k \neq p} 2\left(z_k^* x_k+y_k^* z_k\right)\left(x_p^* z_p+z_p^* y_p\right)\\

= & \sum_{k>0}\left(4 \xi_k+2 U\right)\left|y_k\right|^2+2 \xi_k\left|z_k\right|^2 \\
& -2 g^{\prime} \sum_{k, p>0 ; k \neq p}\left(z_k^* x_k+y_k^* z_k\right)\left(x_p^* z_p+z_p^* y_p\right)

\end{aligned}
$$

$$
\begin{aligned}
0&=\frac{\partial}{\partial x_k}\left[\langle\psi| H|\psi\rangle+\lambda_k\left(\left|x_k\right|^2+\left|y_k\right|^2+\left|z_k\right|^2-1\right)\right]\\
&=\lambda_kx^*_k-2g'z_k^*\sum_{p>0,p\neq k}\left(x_p^* z_p+z_p^* y_p\right)

\end{aligned}
$$

$$
\lambda_k=2 \frac{z_k^*}{x_k^*} O
$$

$$
O=g^{\prime} \sum_{p>0}\left(x_p^* z_p+z_p^* y_p\right)
$$

including $p=k$ which is a $\mathcal{O}\left(1 / L^d\right)$ difference
$$
\begin{aligned}
0=\frac{\partial}{\partial y_k^*}[\ldots]&=\left(4 \xi_k+2 U\right) y_k-2 z_k O+\lambda_k y_k\\

&=\left(4 \xi_k+2 U\right) y_k-2\left(z_k-\frac{z_k^* y_k}{x_k^*}\right) O

\end{aligned}
$$

$$
2 \xi_k+U=\left(\frac{z_k}{y_k}-\frac{z_k^*}{x_k^*}\right) O
$$

two terms
$$
\begin{aligned}
0=\frac{\partial}{\partial z_k^*}[\ldots] & =2 \xi_k z_k-2\left(x_k O+y_k O^*\right)+\lambda_k z_k \\
& =2 \xi_k z_k-2\left(x_k O+y_k O^*-\frac{\left|z_k\right|^2}{x_k^*} O\right)
\end{aligned}
$$

$$
\xi_k x_k^* z_k=\left(\left|x_k\right|^2-\left|z_k\right|^2\right) O+x_k^* y_k O^*
$$

$$
\xi_k=\left(\frac{x_k}{z_k}-\frac{z_k^*}{x_k^*}\right) O+\frac{y_k}{z_k} O^*
$$

$$
\xi_k+U=\left(\frac{z_k}{y_k}-\frac{x_k}{z_k}\right) O-\frac{y_k}{z_k} O^*
$$

assuming everything is real (derivative?)
$$
\begin{aligned}
\xi_k & =\left(\frac{x_k}{z_k}+\frac{y_k}{z_k}-\frac{z_k}{x_k}\right) O \\
\xi_k+U & =-\left(\frac{x_k}{z_k}+\frac{y_k}{z_k}-\frac{z_k}{y_k}\right) O
\end{aligned}
$$
if $U=0$ produce BCS result (appendix)

Weak coupling
$$
\begin{aligned}
\xi_k^l x_k z_k & =\left(x_k^2-z_k^2+x_k y_k\right) O \\
\xi_k^u y_k z_k & =\left(z_k^2-y_k^2-x_k y_k\right) O
\end{aligned}
$$
drop $x_ky_k$ term
$$
\begin{aligned}
\xi_k^l x_k z_k & =\left(x_k^2-z_k^2\right) O \\
\xi_k^u y_k z_k & =\left(z_k^2-y_k^2\right) O
\end{aligned}
$$

$$
\frac{x_k^2-z_k^2}{\xi_k^l}=\frac{2x_k z_k}{2O}=C
$$

$$
x_k^2-z_k^2=C \cdot \xi_k^l, \quad 2 x_k z_k=C \cdot 2 O
$$

$$
\left(x_k^2-z_k^2\right)^2+\left(2 x_k z_k\right)^2=C^2\left(\xi_k^{l^2}+(2 O)^2\right)
$$

$$
\left(x_k^2+z_k^2\right)^2=C^2\left(\xi_k^{l^2}+\Delta_k^{l^2}\right)
$$

with $\Delta_k^l=2 O$
$$
\left(x_k^2+z_k^2\right)^2=C^2(E_k^l)^2
$$

$$
C=\frac{x_k^2+z_k^2}{E_k^l}
$$

$$
C=\frac{1-y_k^2}{E_k^l}
$$

$$
\begin{aligned}
& x_k^2-z_k^2=C \cdot \xi_k^l=\frac{\xi_k^l}{E_k^l}\left(1-y_k^2\right) \\
& 2 x_k z_k=C \cdot \Delta_k^l=\frac{\Delta_k^l}{E_k^l}\left(1-y_k^2\right)
\end{aligned}
$$

$$
\begin{aligned}
\Delta_k^l & =g^{\prime} \sum_{p>0} \frac{\Delta_p^l}{E_p^l}\left(1-y_k^2\right)+\frac{\Delta_p^u}{E_p^u}\left(1-x_k^2\right) \\
\Delta_k^u & =g^{\prime} \sum_{p>0} \frac{\Delta_p^l}{E_p^l}\left(1-y_k^2\right)+\frac{\Delta_p^u}{E_p^u}\left(1-x_k^2\right)
\end{aligned}
$$

$$
\begin{aligned}
& 1=g^{\prime} \sum_{k>0} \frac{1-y_k^2}{\sqrt{\xi_k^2+\Delta^2}}+\frac{1-x_k^2}{\sqrt{\xi_k^2+\Delta^2}} \\
& 1=\frac{g}{2} \int \mathrm{~d} \omega \frac{N^{\prime \prime}(\omega)}{\sqrt{\omega^2+\Delta^2}} .
\end{aligned}
$$

$$
N^{\prime \prime}(\omega)=\frac{1}{L^d} \sum_k \delta\left(\omega-\xi_k^l\right)\left(1-y_k^2\right)+\delta\left(\omega-\xi_k^u\right)\left(1-x_k^2\right)
$$

$1-y_k^2=\theta\left(\xi_k^u\right) \text { and } 1-x_k^2=\theta\left(-\xi_k^l\right)$
$$
N^{\prime \prime}(\omega)=\frac{1}{L^d} \sum_k \delta\left(\omega-\xi_k^l\right) \theta\left(\xi_k^u\right)+\delta\left(\omega-\xi_k^u\right) \theta\left(-\xi_k^l\right)
$$

$$
\begin{aligned}
N^{\prime \prime}(\omega) & =\sum_{k \in \Omega_0} \delta\left(\omega-\xi_k^l\right)+\sum_{k \in \Omega_2} \delta\left(\omega-\xi_k^u\right) \\
& +\sum_{k \in \Omega_1} \delta\left(\omega-\xi_k^l\right)+\delta\left(\omega-\xi_k^u\right)
\end{aligned}
$$



Fermi arc model

standard BCS wave function
$$
|\psi\rangle=\prod_{k}\left(u_k+v_kb_k^{\dagger}\right)|0\rangle
$$
$b_k^{\dagger}=\hat{c}_{k \uparrow}^{\dagger} \hat{c}_{-k \downarrow}^{\dagger}$
$$
\langle\psi| n_{k \sigma}|\psi\rangle=|v_k|^2
$$

$$
H=\sum_{k\sigma}\left(\xi_kn_{k \sigma}+\frac{U}{2} n_{k \sigma} n_{k+Q  -\sigma}\right)-\frac{g}{L^d} \sum_{k, k^{\prime}} \gamma_{k,k'}c_{k\uparrow}^{\dagger} c_{-k, \downarrow}^{\dagger} c_{-k', \downarrow} c_{k', \uparrow}
$$

$\sum_\sigma\frac{U}{2} n_{k \sigma} n_{k+Q  -\sigma}=U n_{k} n_{k+Q}$
$$
\begin{aligned}
\langle\psi| H|\psi\rangle= & \sum_{k} 2\xi_k|v_k|^2+U|v_k|^2|v_{k+Q}|^2 \\
& -g^{\prime} \sum_{k, k^{\prime}}\gamma_{k,k'}u_{k}v^*_{k}u^*_{k'}v_{k'}
\end{aligned}
$$

$$
u_k = \cos\theta_k\quad v_k =\sin\theta_k
$$

$$
\begin{aligned}
\langle\psi| H|\psi\rangle =&\sum_k\left[2\xi_k\sin^2\theta_k+U\sin^2\theta_k\sin^2\theta_{k+Q}\right] -\frac{g'}{4}\sum_{k, k^{\prime}}\gamma_{k,k'}\sin2\theta_k\sin2\theta_{k'}\\

=&\sum_k\left[\xi_k(1-\cos2\theta_k)+U\sin^2\theta_k\sin^2\theta_{k+Q}\right]-\frac{g'}{4}\sum_{k, k^{\prime}}\gamma_{k,k'}\sin2\theta_k\sin2\theta_{k'}

\end{aligned}
$$

$\gamma_{k,k'}=\gamma_k\times\gamma_{k'}$
$$
\sum_pU\sin^2\theta_p\sin^2\theta_{p+Q}
$$

$$
\begin{aligned}
&\frac{\partial}{\partial\theta_k}\sum_pU\sin^2\theta_p\sin^2\theta_{p+Q}\\
=&\frac{\partial}{\partial\theta_k}U\left(\sin^2\theta_k\sin^2\theta_{k+Q}+\sin^2\theta_{k-Q}\sin^2\theta_{k}\right)\\
=&U\sin{2\theta_k}\sin^2\theta_{k+Q}+U\sin{2\theta_k}\sin^2\theta_{k-Q}

\end{aligned}
$$

$\sin^2\theta_{k-Q}=\sin^2\theta_{k-Q+G}=\sin^2\theta_{k+Q}$
$$
\begin{aligned}
\frac{\partial}{\partial\theta_k}E=2\xi_k\sin2\theta_k+2U\sin2\theta_k\sin^2\theta_{k+Q}-g'\gamma_k\cos2\theta_k\sum_{k'}\gamma_{k'}\sin2\theta_{k'}=0


\end{aligned}
$$

$$
\Delta_k =\frac{g'}{2}\gamma_k\sum_{k'}\gamma_{k'}\sin2\theta_{k'}
$$

$$
\tan2\theta_k=\frac{\Delta_k}{\xi_k+U         \sin^2\theta_{k+Q}}
$$

$\xi_k^{\text{effect}}=\xi_k+U\sin^2\theta_{k+Q}$
$$
\sin2\theta_k=\frac{\Delta_k}{\sqrt{\Delta_k^2+(\xi_k^{\text{effect}})^2}}
$$

$$
\Delta_k =\frac{g'}{2}\gamma_k\sum_{k'}\gamma_{k'}\frac{\Delta_{k'}}{\sqrt{\Delta_{k'}^2+(\xi_{k'}^{\text{effect}})^2}}
$$

suppose $\Delta_k=\Delta\gamma_k$
$$
\begin{aligned}
\Delta\gamma_k =&\frac{g'}{2}\sum_{k'}\gamma_k\gamma_{k'}\frac{\Delta\gamma_k'}{\sqrt{\Delta_{k'}^2+(\xi_{k'}^{\text{effect}})^2}}\\

1=&\frac{g'}{2}\sum_{k'}\frac{\gamma_k'^2}{\sqrt{\Delta_{k'}^2+(\xi_{k'}^{\text{effect}})^2}}\\

\end{aligned}
$$
$\xi_k^{\text{effect}}=\xi_k+U\sin^2\theta_{k+Q}=\xi_k+Un_{k+Q}$

$n_{k+Q}$ superconducting value
$$
1=\frac{g'}{2} \int \mathrm{~d} \omega \gamma_k'^2\frac{N(\omega)}{\sqrt{\omega^2+\Delta^2}}
$$
at Fermi arc region, $n_{k+Q}=0$, at pseudo gap region, $n_{k+Q}=1$
$$
\begin{aligned}
N(\omega)=&\sum_{k} \delta\left(\omega-\xi_{k}^{\text{effect}}\right)\\
\approx&\sum_\text{Fermi arc}\delta(\omega-\xi_k)+\sum_\text{pseudo gap}\delta(\omega-\xi_k-U)
\end{aligned}
$$






## appendix

BCS result

if $U=0$
$$
\begin{aligned}
\xi_k & =\left(\frac{x_k}{z_k}+\frac{y_k}{z_k}-\frac{z_k}{x_k}\right) O \\
\xi_k & =-\left(\frac{x_k}{z_k}+\frac{y_k}{z_k}-\frac{z_k}{y_k}\right) O
\end{aligned}
$$
parameter connection to BCS
$$
x_k=u_k^2, y_k=v_k^2, z_k=\sqrt{2} u_k v_k
$$

$$
\begin{aligned}
\xi_k & =\left(\frac{u_k^2}{\sqrt{2} u_k v_k}+\frac{v_k^2}{\sqrt{2} u_k v_k}-\frac{\sqrt{2} u_k v_k}{u_k^2}\right) O \\
\xi_k & =-\left(\frac{u_k^2}{\sqrt{2} u_k v_k}+\frac{v_k^2}{\sqrt{2} u_k v_k}-\frac{\sqrt{2} u_k v_k}{v_k^2}\right) O
\end{aligned}
$$

$$
\begin{aligned}
\xi_k & =\frac{1-2v_k^2}{\sqrt{2} u_k v_k}O \\


\xi_k & =\frac{-1+2u_k^2}{\sqrt{2} u_k v_k} O
\end{aligned}
$$

$u_k^2+v_k^2=1$, so two equations are the same
$$
\begin{aligned}
\xi_k  &=\frac{1-2v_k^2}{\sqrt{2} u_k v_k}g^{\prime} \sum_{p>0}\left(u_p^2 \sqrt{2} u_p v_p+\sqrt{2} u_p v_p v_p^2\right)\\

\xi_k&=\frac{1-2v_k^2}{u_k v_k}g^{\prime}\sum_{p>0}u_p v_p

\end{aligned}
$$

$$
u_k = \cos\theta_k\quad v_k =\sin\theta_k
$$

$$
\begin{aligned}

\xi_k&=\frac{\cos2\theta_k}{\sin2\theta_k}g^{\prime}\sum_{p>0}\sin2\theta_p

\end{aligned}
$$

define
$$
\Delta_k=g'\sum_{p>0}\sin2\theta_p
$$
BCS result!
$$
\tan2\theta_k=\frac{\Delta_k}{\xi_k}
$$



$$
\begin{aligned}
&\langle\psi| b_k^{\dagger} b_p|\psi\rangle\\


=&\langle0|\left(x^*_{p}+y^*_{p}  b_{-p}b_{p}+\frac{z_{p}^*}{\sqrt{2}}\left(b_{p}+b_{-p}\right)\right)\left(x^*_{k}+y^*_{k}  b_{-k}b_{k}+\frac{z_k^*}{\sqrt{2}}\left(b_{k}+b_{-k}\right)\right)
\\

&|b_k^{\dagger} b_p|\left(x_k+y_k b_k^{\dagger} b_{-k}^{\dagger}+\frac{z_k}{\sqrt{2}}\left(b_k^{\dagger}+b_{-k}^{\dagger}\right)\right)\left(x_{p}+y_{p} b_{p}^{\dagger} b_{-p}^{\dagger}+\frac{z_{p}}{\sqrt{2}}\left(b_{p}^{\dagger}+b_{-p}^{\dagger}\right)\right)|0\rangle\\

=&\langle0|\left(x^*_{p}+y^*_{p}  b_{-p}b_{p}+\frac{z_{p}^*}{\sqrt{2}}\left(b_{p}+b_{-p}\right)\right)\left(x^*_{k}+y^*_{k}  b_{-k}b_{k}+\frac{z_k^*}{\sqrt{2}}\left(b_{k}+b_{-k}\right)\right)
\\

&|x_ky_pb_k^\dagger b_{-p}^\dagger+\frac{x_kz_p}{\sqrt{2}}b_k^\dagger +\frac{z_ky_p}{\sqrt{2}}b_{k}^\dagger b_{-k}^\dagger b_{-p}^\dagger +\frac{z_kz_p}{2}b_{k}^\dagger b_{-k}^\dagger|0\rangle\\

=&\frac{1}{2}\left(z_p^*z_k^*x_ky_p+x_p^*z_k^*x_kz_p+z_p^*y_k^*z_ky_p+x_p^*y_k^*z_kz_p\right)\\

=&\frac{1}{2}z_k^*x_k(x_p^*z_p+z_p^*y_p)+y_k^*z_k(x_p^*z_p+z_p^*y_p)\\
=&\frac{1}{2}(z_k^*x_k+y_k^*z_k)(x_p^*z_p+z_p^*y_p)
\end{aligned}
$$



$$
\begin{aligned}
&\langle\psi| n_{k \uparrow} n_{k+Q \downarrow}|\psi\rangle\\

=&\langle0|\left(x^*_{k+Q}+y^*_{k+Q}  b_{-k-Q}b_{k+Q}+\frac{z_{k+Q}^*}{\sqrt{2}}\left(b_{k+Q}+b_{-k-Q}\right)\right)\left(x^*_{k}+y^*_{k}  b_{-k}b_{k}+\frac{z_k^*}{\sqrt{2}}\left(b_{k}+b_{-k}\right)\right)
\\

&|n_{k \uparrow} n_{k+Q \downarrow}|\left(x_k+y_k b_k^{\dagger} b_{-k}^{\dagger}+\frac{z_k}{\sqrt{2}}\left(b_k^{\dagger}+b_{-k}^{\dagger}\right)\right)\left(x_{k+Q}+y_{k+Q} b_{k+Q}^{\dagger} b_{-k-Q}^{\dagger}+\frac{z_{k+Q}}{\sqrt{2}}\left(b_{k+Q}^{\dagger}+b_{-k-Q}^{\dagger}\right)\right)|0\rangle\\

=&\langle0|\left(x^*_{k+Q}+y^*_{k+Q}  b_{-k-Q}b_{k+Q}+\frac{z_{k+Q}^*}{\sqrt{2}}\left(b_{k+Q}+b_{-k-Q}\right)\right)\left(x^*_{k}+y^*_{k}  b_{-k}b_{k}+\frac{z_k^*}{\sqrt{2}}\left(b_{k}+b_{-k}\right)\right)
\\
&|y_ky_{k+Q}b_k^{\dagger} b_{-k}^{\dagger}b_{k+Q}^{\dagger} b_{-k-Q}^{\dagger}+y_kb_k^{\dagger} b_{-k}^{\dagger}\frac{z_{k+Q}}{\sqrt{2}}b^\dagger_{-k-Q}+y_{k+Q}\frac{z_k}{\sqrt{2}}b_k^\dagger b_{k+Q}^{\dagger} b_{-k-Q}^{\dagger}+\frac{z_kz_{k+Q}}{2}b_k^\dagger b_{-k-Q}^\dagger |0\rangle\\

=&|y_k|^2|y_{k+Q}|^2+\frac{1}{2}|y_k|^2|z_{k+Q}|^2+\frac{1}{2}|y_{k+Q}|^2|z_k|^2+\frac{1}{4}|z_k|^2|z_{k+Q}|^2\\

=&\left(|y_k|^2+\frac{|z_k|^2}{2}\right)\left(|y_{k+Q}|^2+\frac{|z_{k+Q}|^2}{2}\right)

\end{aligned}
$$


Fermi arc model

what if use standard BCS wave function?
$$
|\psi\rangle=\prod_{k>0}\left(x_k+y_k b_k^{\dagger} b_{-k}^{\dagger}+\frac{z_k}{\sqrt{2}}\left(b_k^{\dagger}+b_{-k}^{\dagger}\right)\right)|0\rangle
$$

$$
H=\sum_{k\sigma}\left(\xi_kn_{k \sigma}+\frac{U}{2} n_{k \sigma} n_{k+Q  -\sigma}\right)-\frac{g}{L^d} \sum_{k, k^{\prime}} \gamma_{k,k'}c_{k\uparrow}^{\dagger} c_{-k, \downarrow}^{\dagger} c_{-k', \downarrow} c_{k', \uparrow}
$$

$Q=(\pi,\pi)$
$$
\langle\psi| n_{k \sigma}|\psi\rangle=\left|y_k\right|^2+\frac{\left|z_k\right|^2}{2}
$$
derivation in appendix
$$
\langle\psi| n_{k \uparrow} n_{k+Q \downarrow}|\psi\rangle
=\left(|y_k|^2+\frac{|z_k|^2}{2}\right)\left(|y_{k+Q}|^2+\frac{|z_{k+Q}|^2}{2}\right)
$$
k>0 meaning?1d 2d?
$$
\begin{aligned}
\langle\psi| H|\psi\rangle= & \sum_{k>0} \xi_k\left(4\left|y_k\right|^2+2\left|z_k\right|^2\right)+U\left(|y_k|^2+\frac{|z_k|^2}{2}\right)\left(|y_{k+Q}|^2+\frac{|z_{k+Q}|^2}{2}\right) \\
& -g^{\prime} \sum_{k, p>0 ; k \neq p} \gamma_{k,p}2\left(z_k^* x_k+y_k^* z_k\right)\left(x_p^* z_p+z_p^* y_p\right)
\end{aligned}
$$

$$
0=\frac{\partial}{\partial x_k}\left[\langle\psi| H|\psi\rangle+\lambda_k\left(\left|x_k\right|^2+\left|y_k\right|^2+\left|z_k\right|^2-1\right)\right]
$$

