<script type="text/javascript"  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">  
</script>

# Oridinary Least Square
1. Hệ số xác định $\mathbf{Y}_i = \hat{\mathbf{Y}}_i + \epsilon_i$
2. $TSS=ESS + RSS$ (cần chứng minh)
3. $ESS=\sum_{i=1}^{n}\left(\hat{\mathbf{Y}}_i - \bar{\mathbf{Y}}\right)^2$
> tiên đoán nằm trên siêu phẳng, trung bình nằm trên quả cầu () (mẫu xác định)
4. $RSS= \sum_{i=1}^n\epsilon_i^2$ 
> Tổng lỗi của tiên đoán so với xác thực
5. $TSS$ 
> Độ lệch phương sai. Độ lệch so với giá trị trung bình.
6. $R^2=\frac{ESS}{TSS} = 1 - \frac{RSS}{TSS}, 0 \leq R^2 \leq 1$
> $R^2$ càng lớn, mô hình càng tốt.

> **Chú ý** : Cần phải tìm mẫu phù hợp với giả thuyết
# Hệ số xác định hiệu chỉnh.
1. Đưa thêm biến vào mô hình $\Rightarrow k ~tăng$
2. $TSS$ không phu thuộc vào $k$ (tổng bình phương độ lỗi) vì : 
3. $\bar{R}^2=1- \frac{\frac{RSS}{n-k}}{\frac{TSS}{n-1}}=1- \frac{n-1}{n-k}(1-R^2)$
4. Comment :
	- Thêm biến có ý nghĩa $k$(số mẫu) tăng. $RSS$(sai số) giảm.
	- Thêm biến ko có ý nghĩa $k$. $RSS$ không bị giảm hoặc tăng ít
	> Có nghĩa là $RSS$ sẽ ít bị ảnh hưởng bởi $k$. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMjY0MDQ3MDAsMTczMTMzOTE0LC0xMD
M1NzQyMzg1XX0=
-->