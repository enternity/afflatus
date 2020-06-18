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
> $\frac{x_1^2}{s_{11}} + \frac{x_2^2}{s_{22}} = c^2$
<center><img src="https://i.imgur.com/fMgKnkC.png"/></center>

### Khoảng cách thống kê với hơn 2 nhiều. Cho $P,Q$ có $p$ chiều. $P=(x_1,x_2,\cdots,x_p), Q=(x_1,x_2,\cdots,x_p)$. 

$$d(P,Q) = \sqrt{\frac{(x_1-y_1)^2}{s_{11}} + \frac{(x_2-y_2)^2}{s_{22}} + \frac{(x_3-y_3)^2}{s_{33}} + \cdots + \frac{(x_p-y_p)^2}{s_{pp}}}$$

> Khoảng cách từ $P$ đến tâm được tính bằng cách gán $y_1=y_2=\cdots = y_p=0$
> Nếu $s_{11} = s_{22} = \cdots = s_{pp}$, là như khoảng cách Euclid.
> Có một thực tế cần thấy rằng, đôi khi thằng $x_1$ có phương (direction) lớn hơn rất nhiều thằng $x_2$. Vì thế ta cần chuẩn hóa về lại sao cho 2 thằng giá trị đóng góp là như nhau.
> Khi đó,  khoảng cách từ $P=(\tilde{x}_1,\tilde{x}_2)$ đến tâm $O=(0,0)$ là 

$$d(O,P)  = \sqrt{\frac{\tilde{x}_1^2}{\tilde{s}_{11}} + \frac{\tilde{x}_2^2}{\tilde{s}_{22}}}$$
> Với $\tilde{x}_1 = x_1\cos(\theta) + x_2\sin(\theta)$
> Với $\tilde{x}_2 = -x_1\sin(\theta) + x_2\cos(\theta)$
> Từ đó :

$$d(O,P) = \sqrt{a_{11}x_1^2 + 2a_{12}x_1x_2 + a_{22}x_2^2}$$
> Với $a$ là số sao cho khoảng các là **không âm** cho tất cả các giá trị của $x_1$ và $x_2$. Ở đây $a_{11}, a_{12}, a_{22}$ được xác định bằng góc $\theta$ và $s_{11},s_{12},s_{22}$ được tính từ dữ liệu.  Thiệt ra, công thức tính cho $a_{11}, a_{12}, a_{22}$ không quan trọng. Điểm quan trọng ở đây là sự xuất hiện của [cross-product](https://en.wikipedia.org/wiki/Cross_product) $2a_{12}x_1x_2$ yêu cầu bởi một hệ số tương quan $r_{12}$ khác không.

> Khoảng cách từ $P(x_1,x_2)$ đến $Q(y_1,y_2)$ :

$$d(P,Q) = \sqrt{a_{11}(x_1-y_1)^2 + 2a_{12}(x_1-y_1)(x_2-y_2) + a_{22}(x_2-y_2)^2}$$
> $a_{11},a_{12}, a_{22}$ đã biết. Trường hợp đặc biệt, $a_{11} = \frac{1}{s_{11}}, a_{22} = \frac{1}{s_{22}}, a_{12} = 0$

>Khoảng cách này là 1 hằng số .

$$a_{11}(x_1-y_1)^2 + 2a_{12}(x_1-y_1)(x_2-y_2) + a_{22}(x_2-y_2)^2 = c^2$$

> Các trường hợp đặc biệt khác :

<center><img src="https://i.imgur.com/C8cFFoa.png"/></center>

> Với $Q = (y_1,y_2,\cdots,y_p)$, $P=(x_1,x_2,\cdots,x_p)$ thì khoảng cách là :

<center><img src="https://i.imgur.com/e3zw0s6.png"/></center>

> Chú ý rằng khoảng cách ở trên được xác định bởi hệ số (trọng số) $a_{ik}, i = 1, 2, \cdots, p$, $k=1,2,\cdots,p$.  

$$\begin{bmatrix}a_{11} & a_{12} & \cdots a_{1p} \\a_{12} & a_{22} & \cdots a_{2p} \\ \vdots & \vdots & \ddots & \vdots \\ a_{1p} & a_{2p} & \cdots a_{pp} \\ \end{bmatrix}$$
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MzUwODIyMjcsMTE3MDIzMzYsMTA5OT
UxMTc1MywyMTEwMjQyMDIzLDkxMjM2NDU5MCwtODY5NTUyMTcy
LDE5OTk0ODE1NjksLTc4MzM5OTA1LDQzMjUzMzE4NF19
-->