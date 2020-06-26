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
3. Dễ để implement: $\frac{}{}$
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjQ5NDE2MDE1LDE0OTYxNDc4NTZdfQ==
-->