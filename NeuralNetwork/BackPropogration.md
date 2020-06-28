<script type="text/javascript"  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">  
</script>

> Quy định về màu : 
> #000000 : các công thức cần thiết, nhưng không quan trọng trong ngữ cảnh.
> #21CBD6 : các công thức có được thông qua khai triển.
> #0B47F3 : các công thức chính, cần nhớ.
# Đạo hàm ma trận :
1. **Scalar-By-Vector**
$$\frac{\partial y}{\partial \mathbf{x}} = \left[\frac{\partial y}{\partial x_1} \\ \frac{\partial y}{\partial x_2} \cdots \frac{\partial y}{\partial x_n}\right]$$
2. **Vector-By-Vector**
$$\frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \begin{bmatrix}\frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} & \cdots &\frac{\partial y_1}{\partial x_n}\\ \frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} & \cdots & \frac{\partial y_2}{\partial x_n}\\ \vdots & \vdots & \ddots & \vdots \\  \frac{\partial y_n}{\partial x_1} & \frac{\partial y_n}{\partial x_2} & \cdots & \frac{\partial y_n}{\partial x_n}\end{bmatrix}$$
3. **Scalar-By-Matrix** 
$$\frac{\partial y}{\partial A} = \begin{bmatrix}\frac{\partial y}{\partial A_{11}} & \frac{\partial y}{\partial A_{12}} & \cdots & \frac{\partial y}{\partial A_{1n}} \\ \frac{\partial y}{\partial A_{21}} & \frac{\partial y}{\partial A_{22}} & \cdots & \frac{\partial y}{\partial A_{2n}} \\ \vdots &\vdots & \ddots & \vdots \\ \frac{\partial y}{\partial A_{m1}} &\frac{\partial y}{\partial A_{m2}} & \cdots &\frac{\partial y}{\partial A_{mn}}\end{bmatrix}$$
4. **Vector-By-Matrix**
> Đầu tiên từ công thức thứ 3, ta có $\color{#21CBD6}\frac{\partial y}{\partial A_{ij}} = \frac{\partial y}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial A_{ij}} \text{(chain rule)}$

> Cho $\mathbf{z} = A\mathbf{x}$

>  Khi đó : $\color{#21CBD6}\frac{\partial \mathbf{z}}{\partial A_{ij}} = \begin{bmatrix} 0 \\ \vdots \\ 0 \\ x_j \\ 0 \\ \vdots \\0 \end{bmatrix} \leftarrow \text{Vị trí thứ }i$

> Cho nên theo công thức: $\frac{\partial J}{\partial A_{ij}} = \frac{\partial J}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial A_{ij}}$

> Ta sẽ có: 
> 
$$\color{#0B47F3}\frac{\partial J}{\partial A_{ij}} = \delta . \mathbf{x}_j \Rightarrow \frac{\partial J}{\partial A}=\delta^T.\mathbf{x}$$

## Công thức tổng quát dùng trong NN:
1. $z=Wx$
	1.1 
	$$\color{#0B47F3}\frac{\partial z}{\partial x} = W$$
	1.2 Với:  $\delta=\frac{\partial J}{\partial z}$ 
	$$\color{#0B47F3}\frac{\partial J}{\partial W}= \delta^Tx$$
2. $z=x$
$$\color{#0B47F3}\frac{\partial z}{\partial x} = I$$
3. $z=xW$
	3.1
	$$\color{#0B47F3}\frac{\partial z}{\partial x} = W^T$$
	3.2 Với: $\delta=\frac{\partial J}{\partial z}$ 
	$$\color{#0B47F3}\frac{\partial J}{\partial W} = x^T\delta$$
# Định nghĩa Neural Network : 
<center><img src="https://miro.medium.com/max/1400/1*sSIeU-WhsuHCQlOA00IBXg.jpeg" /></center>

> Ở đây ta thấy có 4 layers, 4 neuron cho hidden layers, 1 neuron cho output layer.

## Input Layer
Neuron màu tím. Đại diện cho input data. Nó có thể đơn giản là scalar hay là vector hoặc là một ma trận nhiều chiều.
$$x_j = a_j^{(1)}, i \in \{1,2,3,4\}$$
## Hidden Layers
Giá trị cuối cùng của các hidden neurons có màu xanh, được tính toán dựa trên $z^l$ - trọng số input tại lớp $l$ và $a^l$ - activations tại lớp $l$. Tại layer2, layer3, ta có công thức.
- $l=2$
$$\color{#21CBD6}z^{(2)} = W^{(1)}x + b^{(1)}$$
$$\color{#21CBD6}a^{(2)}=f(z^{(2)})$$

- $l=3$ 
$$\color{#21CBD6}z^{(3)}=W^{(2)}a^{(2)} + b^{(2)}$$
$$\color{#21CBD6}a^{(3)}=f(z^{(3)})$$
> Với $W^2,W^3$ là trọng số tại layer2 và layer3, $b^2,b^3$ là bias tại các lớp ấy.

> Activations $a^2,a^3$ được tính toán dựa trên hàm activation $f$. Hàm $f$ là một hàm non-linear ($\text{sigmoid},\text{ReLU},\tanh$)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTUwNTkxOTMxMywtMTk2ODkxMzY0NiwtOT
QzNTAzNTk2XX0=
-->