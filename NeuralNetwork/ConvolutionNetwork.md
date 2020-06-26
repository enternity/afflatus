<script type="text/javascript"  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">  
</script>
# An Individual Neuron
1. Input: $\mathbf{X}$ $(n\times 1 \text{ vector})$
2. Parameters :  trọng số $w(n\times 1\text{ vector})$
3. Activation: $a=\sum_{i=1}^n x_iw_i+b$. Chú ý rằng $a$ là một số vô hướng.
4. Point-wise non-linear function : $\sigma(.), ex: \sigma(.)=\tanh(.)$
5. Output: $y=f(a)=\sigma\left(\sum_{i=1}^n x_iw_i+b\right)$
6. Thông thường 

<!--stackedit_data:
eyJoaXN0b3J5IjpbNzY1MDA5NjQ3LDE0OTYxNDc4NTZdfQ==
-->