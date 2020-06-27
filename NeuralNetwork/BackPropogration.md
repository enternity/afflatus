<script type="text/javascript"  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">  
</script>

> 
# Đạo hàm ma trận :
1. **Scalar-By-Vector**
$$\frac{\partial y}{\partial \mathbf{x}} = \left[\frac{\partial y}{\partial x_1} \\ \frac{\partial y}{\partial x_2} \cdots \frac{\partial y}{\partial x_n}\right]$$
2. **Vector-By-Vector**
$$\frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \begin{bmatrix}\frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} & \cdots &\frac{\partial y_1}{\partial x_n}\\ \frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} & \cdots & \frac{\partial y_2}{\partial x_n}\\ \vdots & \vdots & \ddots & \vdots \\  \frac{\partial y_n}{\partial x_1} & \frac{\partial y_n}{\partial x_2} & \cdots & \frac{\partial y_n}{\partial x_n}\end{bmatrix}$$
3. **Scalar-By-Matrix** 
$$\frac{\partial y}{\partial A} = \begin{bmatrix}\frac{\partial y}{\partial A_{11}} & \frac{\partial y}{\partial A_{12}} & \cdots & \frac{\partial y}{\partial A_{1n}} \\ \frac{\partial y}{\partial A_{21}} & \frac{\partial y}{\partial A_{22}} & \cdots & \frac{\partial y}{\partial A_{2n}} \\ \vdots &\vdots & \ddots & \vdots \\ \frac{\partial y}{\partial A_{m1}} &\frac{\partial y}{\partial A_{m2}} & \cdots &\frac{\partial y}{\partial A_{mn}}\end{bmatrix}$$
4. **Vector-By-Matrix**
> Đầu tiên từ công thức thứ 3, ta có $\frac{\partial y}{\partial A_{ij}} = \frac{\partial y}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial A_{ij}} \text{(chain rule)}$

> Cho $\mathbf{z} = A\mathbf{x}$

>  Khi đó : $\frac{\partial \mathbf{z}}{\partial A_{ij}} = \begin{bmatrix} 0 \\ \vdots \\ 0 \\ x_j \\ 0 \\ \vdots \\0 \end{bmatrix} \leftarrow \text{Vị trí thứ }i$

> Cho nên theo công thức: $\frac{\partial J}{\partial A_{ij}} = \frac{\partial J}{\partial \mathbf{z}} \cdot \frac{\partial \mathbf{z}}{\partial A_{ij}}$

> Ta sẽ có: 
> 
$$\frac{\partial J}{\partial A_{ij}} = \delta . \mathbf{x}_j \Rightarrow \frac{\partial J}{\partial A}=\delta^T.\mathbf{x}$$

## Công thức tổng quát dùng trong NN:
1. $z=Wx$
	1.1 
	$$\frac{\partial z}{\partial x} = W$$
	1.2 Với:  $\delta=\frac{\partial J}{\partial z}$ 
	$$\frac{\partial J}{\partial W}= \delta^Tx$$
2. $z=x$
$$\frac{\partial z}{\partial x} = I$$
3. $z=xW$
	3.1
	$$\frac{\partial z}{\partial x} = W^T$$
	3.2 Với: $\delta=\frac{\partial J}{\partial z}$ 
	$$\frac{\partial J}{\partial W} = x^T\delta$$
# Motivation :
> Đơn giản là cực tiểu hóa hàm lỗi. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc5NzUzMDYwMywtOTQzNTAzNTk2XX0=
-->