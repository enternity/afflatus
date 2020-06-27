<script type="text/javascript"  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">  
</script>
# Đạo hàm ma trận :
1. **Scalar-By-Vector**
$$\frac{\partial y}{\partial \mathbf{x}} = \left[\frac{\partial y}{\partial x_1} \\ \frac{\partial y}{\partial x_2} \cdots \frac{\partial y}{\partial x_n}\right]$$
2. **Vector-By-Vector**
$$\frac{\partial \mathbf{y}}{\partial \mathbf{x}} = \begin{bmatrix}\frac{\partial y_1}{\partial x_1} & \frac{\partial y_1}{\partial x_2} & \cdots &\frac{\partial y_1}{\partial x_n}\\ \frac{\partial y_2}{\partial x_1} & \frac{\partial y_2}{\partial x_2} & \cdots & \frac{\partial y_2}{\partial x_n}\\ \vdots & \vdots & \ddots & \vdots \\  \frac{\partial y_n}{\partial x_1} & \frac{\partial y_n}{\partial x_2} & \cdots & \frac{\partial y_n}{\partial x_n}\end{bmatrix}$$
3. **Scalar-By-Matrix** 
$$\frac{\partial y}{\partial A} = \begin{bmatrix}\frac{\partial y}{\partial A_{11}} & \frac{\partial y}{\partial A_{12}} & \cdots & \frac{\partial y}{\partial A_{1n}} \\ \frac{\partial y}{\partial A_{21}} & \frac{\partial y}{\partial A_{22}} & \cdots & \frac{\partial y}{\partial A_{2n}} \\ \vdots &\vdots & \ddots & \vdots \\ \frac{\partial y}{\partial A_{m1}} &\frac{\partial y}{\partial A_{m2}} & \cdots &\frac{\partial y}{\partial A_{mn}}\end{bmatrix}$$
# Motivation :
> Đơn giản là cực tiểu hóa hàm lỗi. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTI5ODU3MTU3LC05NDM1MDM1OTZdfQ==
-->