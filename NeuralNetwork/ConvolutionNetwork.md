<script type="text/javascript"  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">  
</script>
# An Individual Neuron
1. Input: $\mathbf{X}$ $(n\times 1 \text{ vector})$
2. Parameters :  trọng số $w(n\times 1\text{ vector})$
3. Activation: $a=\sum_{i=1}^n x_iw_i+b$. Chú ý rằng $a$ là một số vô hướng.
4. Point-wise non-linear function : $\sigma(.), ex: \sigma(.)=\tanh(.)$
5. Output: $y=f(a)=\sigma\left(\sum_{i=1}^n x_iw_i+b\right)$
6. Thông thường *bias* $b=1$
# Non-linearities: 
## Sigmoid Function
1. $\sigma(\mathbf{z}) = \frac{1}{1+\exp(-\mathbf{z})}$.
2. Nằm trong đoạn từ $[0,1]$.
3. Đạo hàm tiến về không.
4. Không được dùng trong thực tế.
5. Vị trí trung tâm tại $0.5$
6. Thông tin thêm : [tại đây](https://vi.wikipedia.org/wiki/H%C3%A0m_sigmoid)

## Tanh Function
1. $\sigma(\mathbf{z})=\tanh(\mathbf{z})$
2. Nằm trong khoảng $[+1,-1]$
3. Trung tâm tại $0$
4. Ưu tiên hơn ***sigmoid***
5. Thông tin thêm về các hàm *hyperbolic*: [tại đây](https://vi.wikipedia.org/wiki/H%C3%A0m_hyperbolic)

## Rectified Linear (ReLU)
1. $\sigma(\mathbf{z}) = \max(\mathbf{z},0)$.
2. Nằm trong khoảng $[0,+\inf]$
3. Dễ để implement: $\frac{\partial \sigma(\mathbf{z})}{\partial \mathbf{z}} = \{0,1\}$
4. Tăng nhanh việc hội tụ (nhanh hơn 6 lần so với $\tanh$).
5. Tuy nhiên nếu có phần âm lớn, đạo hàm luôn bằng 0,
6. Thường được dùng trong các model hiện tại.
7. Thông tin thêm tại đây : [tại đây](https://en.wikipedia.org/wiki/Rectifier_(neural_networks))

## Leaky ReLU
1. $\sigma(\mathbf{z}) = 1[z>0]\max(0,x) + 1[z<0]\max(0,\alpha \mathbf{z})$,  với $\alpha$ nhỏ.
2. Hay còn gọi là *probabilistic ReLU* (PReLU).
3. Luôn có đạo hàm tại mọi vị trí.
4. $\alpha$ có thể học được..

> Tìm hiểu thêm các ***Non-linearities*** tại đây : [https://medium.com/@himanshuxd/activation-functions-sigmoid-relu-leaky-relu-and-softmax-basics-for-neural-networks-and-deep-8d9c70eed91e](https://medium.com/@himanshuxd/activation-functions-sigmoid-relu-leaky-relu-and-softmax-basics-for-neural-networks-and-deep-8d9c70eed91e)

# Multiple Layers.
1. Neural Networks bao gồm nhiều lớp neuron. Cấu trúc tuần hoàn. Các model cơ bản giả sử là *full-connections* giữa mỗi lớp.
2. Các lớp giữa input, output được goi là *hidden layers*
3. Các tên cúng cơm khác :
	- *Artificial Neural Nets (ANN)*
	- *Multi-layer Perceptron (MLP)*
	- *Full-connected Network*
4. Các neurons thường được gọi là các đơn vị

<center><img src="https://i.imgur.com/JqJ5IoN.png" /></center>

# Mô hình 3 lớp MLP
1. Quy ước, số *hidden layers* = *hidden* + *output* (không bao gồm input).
2. Mô hình 3-layer có 2 hidden layers.
3. Params : ma trận trọng số $\mathbf{W}^1,\mathbf{W}^2,\mathbf{W}^3$, và vector bias là $\mathbf{b}^1,\mathbf{b}^2,\mathbf{b}^3$

# Architecture Selection for MLPs.
Dựa theo tỉ lệ $units/layers$ :
1. Parameters tăng với tỉ lệ $(unit/layers)^2$.
2. Với $units/layers$ dễ bị *overfit*
> Tìm hiểu thêm về *overfit* : [https://machinelearningcoban.com/2017/03/04/overfitting/](https://machinelearningcoban.com/2017/03/04/overfitting/)

3. Với bài toán phân lớp, dễ dàng mở rộng hướng đầu ra (phân lớp nhiều thứ)

# Training a model :
1. Cho một dataset $\{$
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY5MTA1MDk2OCw2NDk0MTYwMTUsMTQ5Nj
E0Nzg1Nl19
-->