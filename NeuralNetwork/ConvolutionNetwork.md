<script type="text/javascript"  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">  
</script>
# An Individual Neuron
1. Input: $\mathbf{X}$ $(n\times 1 \text{ vector})$
2. Parameters :  trọng số $w(n\times 1\text{ vector})$
3. Activation: $a=\sum_{i=1}^n x_iw_i+b$. Chú ý rằng $a$ là một số vô hướng.
4. Point-wise non-linear function : $\sigma(.), ex: \sigma(.)=\tanh(.)$
5. Output: $y=f(a)=\sigma\left(\sum_{i=1}^n x_iw_i+b\right)$
6. Thông thường *bias* $b=1$
# Non-linearities: Sigmoid
1. $\sigma(\mathbf{z}) = \frac{1}{1+\exp(-\mathbf{z})}$.
2. Nằm trong đoạn từ $[0,1]$.
3. Đạo hàm tiến về không.
4. Không được dùng trong 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEyODgxODQwOSwxNDk2MTQ3ODU2XX0=
-->