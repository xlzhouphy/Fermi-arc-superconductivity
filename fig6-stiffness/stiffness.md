Current density operator definition 
$$
\frac{\partial \rho}{\partial t} + \nabla \cdot \mathbf{J} = 0
$$
Current density operator
$$
\hat{j}(r)=-\frac{\delta H}{\delta A(r)}
$$

$$
\begin{aligned}
\delta H&=\frac{1}{2 m}\left[(\hat{p}-q A-q \delta A)^2-(\hat{p}-q A)^2\right]\\

&\approx-\frac{q}{2 m}[(\hat{p}-q A) \cdot \delta A(\hat{r})+\delta A(\hat{r}) \cdot(\hat{p}-q A)]
\end{aligned}
$$

$$
\delta H=-\int d^3 r\left\{\frac{q}{2 m}[(\hat{p}-q A) \delta(\hat{r}-r)+\delta(\hat{r}-r)(\hat{p}-q A)]\right\} \cdot \delta A(r)
$$

$$
\frac{\delta H}{\delta A(r)}=-\frac{q}{2 m}[(\hat{p}-q A) \delta(\hat{r}-r)+\delta(\hat{r}-r)(\hat{p}-q A)]=-\hat{j}(r)
$$

$$
\begin{aligned}
\hat{j}(r)
&=\frac{q}{2 m}[(\hat{p}-q A) \delta(\hat{r}-r)+\delta(\hat{r}-r)(\hat{p}-q A)]\\

&=\frac{q}{2 m}[\hat{p} \delta(\hat{r}-r)+\delta(\hat{r}-r)\hat{p}]-\frac{q^2}{ m}A\delta(\hat{r}-r)

\end{aligned}
$$

Current density operator in tight-binding model
$$
K_0 = -t \sum_{l, s} \left( c_{l+x, s}^\dagger c_{l, s} + c_{l, s}^\dagger c_{l+x, s} \right)
$$

$$
K_A = -t \sum_{l, s} \left( e^{ie A_x(l)} c_{l+x, s}^\dagger c_{l, s} + e^{-ie A_x(l)} c_{l, s}^\dagger c_{l+x, s} \right)
$$

$$
e^{\pm ie A_x(l)} \approx 1 \pm ie A_x(l) - \frac{e^2}{2} A_x^2(l)
$$

$$
K_A = -t \sum_{l, s} \left[ \left(1 + ie A_x(l) - \frac{e^2}{2} A_x^2(l)\right) c_{l+x, s}^\dagger c_{l, s} + \left(1 - ie A_x(l) - \frac{e^2}{2} A_x^2(l)\right) c_{l, s}^\dagger c_{l+x, s} \right]
$$

$$
K_A^{(0)} = -t \sum_{l, s} \left( c_{l+x, s}^\dagger c_{l, s} + c_{l, s}^\dagger c_{l+x, s} \right) = \sum_l k_x(l)
$$

$$
\begin{aligned}
K_A^{(1)} &= -t \sum_{l, s} \left[ ie A_x(l) c_{l+x, s}^\dagger c_{l, s} - ie A_x(l) c_{l, s}^\dagger c_{l+x, s} \right]\\

&= -\sum_l e A_x(l) \cdot \left[ i t \sum_s \left( c_{l+x, s}^\dagger c_{l, s} - c_{l, s}^\dagger c_{l+x, s} \right) \right]\\

&= -\sum_l e j_x^P(l) A_x(l)

\end{aligned}
$$

$$
\begin{aligned}
K_A^{(2)} &= -t \sum_{l, s} \left[ -\frac{e^2}{2} A_x^2(l) c_{l+x, s}^\dagger c_{l, s} - \frac{e^2}{2} A_x^2(l) c_{l, s}^\dagger c_{l+x, s} \right]\\

&= -\sum_l \frac{e^2}{2} A_x^2(l) \cdot \left[ -t \sum_s \left( c_{l+x, s}^\dagger c_{l, s} + c_{l, s}^\dagger c_{l+x, s} \right) \right]\\

&= -\sum_l \frac{e^2}{2} k_x(l) A_x^2(l)

\end{aligned}
$$

$$
K_A = \sum_l k_x(l) - \sum_l e j_x^P(l) A_x(l) - \sum_l \frac{e^2}{2} k_x(l) A_x^2(l)
$$

$$
j_x(l)=-\frac{\delta K}{\delta A_x(l)}=e j_x^P(l)+e^2 k_x(l) A_x(l)
$$



