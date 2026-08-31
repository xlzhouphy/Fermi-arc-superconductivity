## BCS theory

### BCS Hamiltonian

General two-body interaction:
$$
H_{\text{int}}= \frac{1}{2}\sum_{\substack{q, k_1, k_2 \\ \sigma_1, \sigma_2}} V_{ q} c_{k_1+q, \sigma_1}^{+} c_{k_2-q, \sigma_2}^{+} c_{k_2, \sigma_2} c_{k_1, \sigma_1}
$$
momentum conservation: $k_1+k_2=k_1+q+k_2-q$

total momentum: $K=k_1+k_2$

考虑散射前后电子都位于费米面的情况，$K=0$具有最大相空间体积。（李正中p162-163）

由于Pauli不相容原理限制自旋平行排列的电子相互靠近，因此$\sigma_1=\sigma_2$贡献比$\sigma_1=-\sigma_2$小。

BCS further assume $V_q\approx -V$ near the Fermi surface.
$$
H_{\text{int}}\approx-\frac{1}{2}\sum_{\substack{ k, k', \sigma}} V c_{k', \sigma}^{+} c_{-k', -\sigma}^{+} c_{-k, -\sigma} c_{k, \sigma}
$$
The BCS Hamiltonian is:
$$
H_\text{BCS}=\sum_{k,\sigma}(\varepsilon_k-\mu)c^+_{k,\sigma}c_{k,\sigma}-\sum_{\substack{ k, k'}} V c_{k, \uparrow}^{+} c_{-k, \downarrow}^{+} c_{-k', \downarrow} c_{k', \uparrow}
$$

### Mean-filed approximation

$$\hat{O} = \langle \hat{O} \rangle + (\hat{O} - \langle \hat{O} \rangle)=\langle \hat{O} \rangle + \delta\langle\hat{O}\rangle$$

$$
\begin{aligned}
\hat{A}\hat{B}&=(\langle \hat{A} \rangle + \delta\langle\hat{A}\rangle)(\langle \hat{B} \rangle + \delta\langle\hat{B}\rangle)\\

&=\langle \hat{A} \rangle\langle \hat{B} \rangle+\delta\langle\hat{A}\rangle\langle \hat{B} \rangle+\langle\hat{A}\rangle\delta\langle \hat{B} \rangle+\delta\langle\hat{A}\rangle\delta\langle \hat{B} \rangle\\

&\approx\langle \hat{A} \rangle\langle \hat{B} \rangle+\delta\langle\hat{A}\rangle\langle \hat{B} \rangle+\langle\hat{A}\rangle\delta\langle \hat{B} \rangle\\

&=\hat{A}\langle \hat{B} \rangle+\langle\hat{A}\rangle \hat{B} -\langle \hat{A} \rangle\langle \hat{B} \rangle
\end{aligned}
$$

define order parameter: $\Delta=\sum_{\substack{ k}} V  \langle c_{-k, \downarrow} c_{k, \uparrow}\rangle$

BCS mean-field approximation:
$$
\begin{aligned}
H_{\text{BCS-MF}} &= \sum_{\mathbf{k}, \sigma} \xi_{\mathbf{k}} c_{\mathbf{k} \sigma}^\dagger c_{\mathbf{k} \sigma} - \sum_{\mathbf{k}} (\Delta c_{\mathbf{k} \uparrow}^\dagger c_{-\mathbf{k} \downarrow}^\dagger + \Delta^* c_{-\mathbf{k} \downarrow} c_{\mathbf{k} \uparrow}) + \frac{|\Delta|^2}{V}\\

&=\sum_{\mathbf{k}} \left[\xi_{\mathbf{k}} c_{\mathbf{k} \uparrow}^\dagger c_{\mathbf{k} \uparrow}+\xi_{\mathbf{k}} c_{-\mathbf{k} \downarrow}^\dagger c_{-\mathbf{k} \downarrow}-\Delta c_{\mathbf{k} \uparrow}^\dagger c_{-\mathbf{k} \downarrow}^\dagger - \Delta^* c_{-\mathbf{k} \downarrow} c_{\mathbf{k} \uparrow}\right]+ \frac{|\Delta|^2}{V}

\end{aligned}
$$
Fock-space

$\{|0\rangle, c_{k\uparrow}^\dagger|0\rangle, c_{-k\downarrow}^\dagger|0\rangle, c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger|0\rangle\}$ 
$$
H_{\mathbf{k}}  = \begin{pmatrix} 0 & 0 & 0 & -\Delta^* \\ 0 & \xi_{\mathbf{k}} & 0 & 0 \\ 0 & 0 & \xi_{\mathbf{k}} & 0 \\ -\Delta & 0 & 0 & 2\xi_{\mathbf{k}} \end{pmatrix}
$$
block diagonalized:

$\{|0\rangle, c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger|0\rangle\}$
$$
H_{\text{sub-space}} = \begin{pmatrix} 0 & -\Delta \\ -\Delta & 2\xi_{\mathbf{k}} \end{pmatrix}
$$
eigenvalue: $$\lambda = \xi_{\mathbf{k}} \pm \sqrt{\xi_{\mathbf{k}}^2 + \Delta^2}$$

BCS variational ground-state function:

$$|\text{BCS}\rangle = \prod_{\mathbf{k}} (u_{\mathbf{k}} + v_{\mathbf{k}} c_{\mathbf{k}\uparrow}^\dagger c_{-\mathbf{k}\downarrow}^\dagger) |0\rangle$$

a mix of $\{|0\rangle, c_{k\uparrow}^\dagger c_{-k\downarrow}^\dagger|0\rangle\}$ states, so the mean-field approach is the same as the variational method.

### Bogoliubov transformation

$$
\hat{H}_{\text{BCS-MF}}=\sum_k\left(\begin{array}{cc}
\hat{c}_{k \uparrow}^{\dagger} & \hat{c}_{-k \downarrow}
\end{array}\right)\left(\begin{array}{cc}
\xi_k & \Delta_k \\
\Delta_k^* & -\xi_k
\end{array}\right)\binom{\hat{c}_{k \uparrow}}{\hat{c}_{-k \downarrow}^{\dagger}}+\frac{V}{g}|\Delta|^2+\sum_k \xi_k
$$



**Fock 空间的 $2 \times 2$ 对角化：**

你关注的是**状态空间（State Space）**。你选择基底是 $|0\rangle$（无电子）和 $|2\rangle = c_{\mathbf{k}\uparrow}^\dagger c_{-\mathbf{k}\downarrow}^\dagger|0\rangle$（有库珀对）。

你的对角化操作是在寻找一个**态矢量** $|\Psi\rangle = u|0\rangle + v|2\rangle$。

**Bogoliubov 变换：**

你关注的是**算符空间（Operator Space）**。你定义新的算符 $\gamma_{\mathbf{k}} = u c_{\mathbf{k}\uparrow} - v c_{-\mathbf{k}\downarrow}^\dagger$。

这里并没有显式地写出基矢，而是通过**算符的线性组合**，强制哈密顿量满足 $[\gamma, H] = E\gamma$。

**上述二者等价于Rabi oscillation（state space）与ac stark effect（operator space）的关系。**



