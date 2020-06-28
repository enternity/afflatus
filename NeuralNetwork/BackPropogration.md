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
> Chúng ta kết hợp tất cả các giá trị tham số vào trong ma trận, nhóm theo layer.

>  Lấy ví dụ tại layer2 và tham số của nó làm ví dụ. 

-  $W^{(1)}$ là ma trận trọng số có shape là $(n,m)$  trong đó $n$ là số lượng output neuron (neurons lớp tiếp theo) và $m$ là số lượng input neuron (neurons ở lớp trước). Trong ví dụ này là $n=2,m=4$

$$\color{#21CBD6}W^{(1)}=\begin{bmatrix}W^{(1)}_{11} & W^{(1)}_{12} & W^{(1)}_{13} & W^{(1)}_{14} \\ W^{(1)}_{21} & W^{(1)}_{22} & W^{(1)}_{23} & W^{(1)}_{24}\end{bmatrix}$$

- $x$ là input vector có dạng $(m,1)$ với $m$ là số lượng input neurons, ở đây $m=4$

$$\color{#21CBD6}\mathbf{x}=\begin{bmatrix}x_1 \\ x_2 \\x_3 \\x_4\end{bmatrix}$$
- $b^1$ là *bias vector* có shape $(n,1)$ với $n$ là số neurons tại lớp hiện tại, ở đây là $n=2$

$$\color{#21CBD6}b^{(1)}=\begin{bmatrix}b^{(1)}_1 \\ b^{(1)}_2\end{bmatrix}$$

> Từ các công thức tính $W^1,x,b^1$ ta suy ra được $z^{(2)}$

$$\color{#21CBD6}z^{(2)}=\begin{bmatrix}W^{(1)}_{11}x_1 + W^{(1)}_{12}x_1 + W^{(1)}_{13}x_3 + W^{(1)}_{14}x_4 \\ W^{(1)}_{21}x_1 + W^{(1)}_{22}x_2 + W^{(1)}_{23}x_3 + W^{(1)}_{24}x_4 \end{bmatrix} + \begin{bmatrix}b^{(1)}_1 \\ b^{(1)}_2\end{bmatrix}$$

<center><img src="https://miro.medium.com/max/1400/1*02zF6C6PYzGBbiah4-5fTQ.jpeg"></center>

## Output Layer
Dự đoán giá trị. Trong ví dụ này, là một neuron màu blue và tính toán dựa theo :
$$\color{#21CBD6}s=W^{(3)}a^{(3)}$$
## Forward Propagation and Evaluation 

<center><img src="https://miro.medium.com/max/1400/1*51X_xj8p-jO8-plMfsyajg.png"></center>

Đánh giá giữa $s$ và $y$ dựa vào ***cost function***. Có thể đơn ginả như *MSE* hay phức tạp như *cross-entropy*.
$$C = cost(s,y)$$
Dựa trên giá trị $C$, mô hình dùng để điều chỉnh tham số của chính nó để tiến gần hơn tới giá trị mong muốn $y$. Dùng trong thuậ toán backpropagation .
## Backpropagation and Computing Gradients
Mục tiêu đơn giản là cực tiểu hóa *cost fucntion* bằng các điều chỉnh giá trị trọng số và biases. 

Tính toán đạo hàm để cho chúng ta xem tham số $x$ cần thay đổi bao nhiêu (trừ hay cộng bao nhiêu) để cực tiểu hóa $C$

Tại một $w_{jk}^l$, đạo hàm sẽ là :
$$\color{#21CBD6} \frac{\partial C}{\partial w_{jk}^l}= \frac{\partial C}{\partial z_j^l}\cdot \frac{\partial z_j^l}{\partial w_{jk}^l} \text{ (chain rule)}$$
$$\color{#21CBD6} z_j^l = \sum_{k=1}^mw_{jk}^la_k^{l-1} + b_k^l \text{ (định nghĩa)} \\ m-number ~of ~neurons ~in ~l-1~ layer$$
$$\color{#21CBD6}\frac{\partial z_j^l}{\partial w_{jk}^l}=a_k^{l-1} \text{ (tính đạo hàm)}$$
$$\color{#21CBD6}\frac{\partial C}{\partial w_{jk}^l}=\frac{\partial C}{\partial z_j^l}a_k^{l-1} \text{ (giá trị cuối cùng)}$$

> Tương tự tính toán với $b_j^l$

$$\color{#21CBD6}\frac{\partial C}{\partial b_j^l}=\frac{\partial C}{\partial z_j^l}\cdot \frac{\partial z_j^l}{\partial b_j^l}$$
$$\color{#21CBD6}\frac{\partial z_j^l}{\partial b_j^l}=1$$
$$\color{#21CBD6}\frac{\partial C}{\partial b_j^l}=\frac{\partial C}{\partial z_j^l}\cdot 1$$

> Phần thường thấy trong cả hai công thức được gọi là *"local gradient"* :

$$\color{#21CBD6} \delta_j^l=\frac{\partial C}{\partial z_j^l}$$

Đạo hàm cho phép ta tối ưu hóa tham số :

---
**Các step**

while (không gặp điều kiện dừng)
	$$w:=w-\epsilon \frac{\partial C}{\partial w}$$
	$$b := b-\epsilon \frac{\partial C}{\partial b}$$
end

---
- Khởi tạo $w,b$ random.
- $\epsilon$ là learning rate. 
- $w,b$ là ma trận đại diện cho trọng số và biases. Tính toán đạo hàm $C$ trên $w,b$.
- 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NjAwODMzNzMsLTE4NDc5ODM5MDMsMz
QzODA4NDQ1LDM2OTE0NzU4MiwtMTk2ODkxMzY0NiwtOTQzNTAz
NTk2XX0=
-->