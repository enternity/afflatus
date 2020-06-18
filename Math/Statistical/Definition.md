<script type="text/javascript"  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">  
</script>
> Cho ma trận :

<center><img src="https://i.imgur.com/Kdz0E9n.png"/></center>

> Ta có các công thức sau :
> Cho $x_{11},x_{21},\cdots,x_{n1}$ là giá trị của biến $\text{Variable 1}$. Trung bình của biến là: 

$\bar{x_1} = \frac{1}{n}\sum_{j=1}^{n}x_{j1}~~~,k=1,2,\cdots,p$
1. **Trung bình** của biến thứ $k$ là 

$\bar{x_k} = \frac{1}{n}\sum_{j=1}^{n}x_{jk}~~~,k=1,2,\cdots,p$

2. **Độ lệch chuẩn**
- Ví dụ :
$$s_1^2 = \frac{1}{n}\sum_{j=1}^n(x_{j1} - \bar{x}_1)^2$$
- Với biến $p$ :
$$s_{k}^2 = s_{kk} =\frac{1}{n}\sum{j=1}^{n}(x_{jk} - \bar{x}_k)^2 ~~~~,k = 1,2,\cdots,p$$
3. **Hiệp phương sai** :
- Ví dụ tương quan giữa 2 biến $1,2$ :
$$s_{12} = \frac{1}{n}\sum_{j=1}^n(x_{j1} - \bar{x}_1)(x_{j2} - \bar{x}_2)$$
- Với tương quan giữa 2 biến $i,k$
$$s_{ik} = \frac{1}{n}\sum_{j=1}^n(x_{ji} - \bar{x}_i)(x_{jk} - \bar{x}_k) ~~~~i=1,2,\cdots,p,~~~k=1,2,\cdots,p$$

> Ma trận hiệp phương sai là ma trận đối xứng qua đường chéo chính.
4. **Hệ số tương quan** :
$r_{ik} = \frac{s_{ik}}{\sqrt{s_{ii}}\sqrt{s_{kk}}} = \frac{\sum_{j=1}^{n}(x_{ji} - \bar{x}_i)(x_{jk} -\bar{x}_k)}{\sqrt{\sum_{j=1}^{n}(x_{ji} - \bar{x}_i)^2}\sqrt{\sum_{j=1}^{n}(x_{jk} -\bar{x}_k)^2}}$

> $r \in [-1,1]$
> $r = 0$ : Hai biến không liên quan nhau.
> $r < 0$ : hai biến nghịch biến.
> $r > 0$ : đồng biến 
> *Cho dễ hiểu thôi.*

<center><img src="https://i.imgur.com/ugGhY9g.png"/></center>

# Khoảng cách thống kê.
$d(O,P) = \sqrt{(x_1^{*})^2 + (x_2^{*})^2} = \sqrt{\frac{x_1^2}{s_{11}} + \frac{x_2^2}{s_{22}}}$
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUzODYyMjMyNCwtNzgzMzk5MDUsNDMyNT
MzMTg0XX0=
-->