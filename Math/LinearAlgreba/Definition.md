<script type="text/javascript"  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">  
</script>
# Các tính chất của định thức (determinants): 
<br/>

1. $det(A) = det(A^T)$: Một ma trận bất kỳ và chuyển vị của nó có định thức như nhau 
<br/>

2. $A = diag(a_1,a_2,...,a_n) \Rightarrow det(A) = a_1a_2...a_n$: Định thức của một ma trận đường chéo (và vuông) bằng tích cách phần tử trên đường chéo chính
<br/>

3. Định thức của ma trận đơn vị bằng 1.
<br/>

4. $det(AB) = det(A)det(B)$
<br/>

5. Nếu ma trận có một hàng hoặc một cột là một vector 0 thì định thức của ma trận đó bằng 0.
<br/>

6. Ma trận khả nghịch khi và chỉ khi định thức nó khác 0
<br/>

7. $det(A^{-1}) = \frac{1}{det(A)}$  vì  $det(A^{-1})det(A) = det(A^{-1}A) = det(I_n) = 1$
# Conjugate Transpose(chuyển vị liên hợp)
### 1. Định nghĩa : 
> Chuyển vị liên hợp của 1 ma trận A có kích thước $m\times n$ là là 1 ma trận có kích thước $n\times m$ với : 
> 
$$A^H \equiv A^{-T}$$

> Với $A^T$ là ma trận chuyển vị của A và $\bar{A}$ là ma trận liên hợp. Nghĩa là :

$$A^H \equiv A^{-T} = \bar{A^T}$$
# Tích Hadamard (element wise) .
1. **Định nghĩa** : tích hadamard của 2 ma trận cùng kích thước $A, B \in \mathbb{R}^{m\times n}$, ký hiệu là $C = A \odot B \in \mathbb{R}^{m \times n}$ trong đó : 
$$C_{ij} = A_{ij}B_{ij} $$

# Tổ hợp tuyến tính, độc lập tuyến tính, phụ thuộc tuyến tính.
1. **Định nghĩa**
> **Cho các vector khác không $a_1, ..., a_n \in \mathbb{R}^m$ và các số thực $x_1, x_2, ..., x_n \in \mathbb{R}$, vector:**
$$b = x_1a_1 + x_2a_2 + ... + x_na_n$$

   Được gọi là **tổ hợp tuyến tính (linear combination)** của $a_1, .., a_n$. Xét ma trận $A = [a_1,a_2,...,a_n] \in \mathbb{R}^{mn}$ và $x = [x_1,x_2,...,x_n]^T$, biểu thức trên được biết thành $b = Ax$. Ta nói rằng b là một tổ hợp tuyến tính các cột của A
Xét phương trình : 
$$0 = x_1a_1 + x_2a_2 + ... + x_na_n$$
> Nếu có 1 nghiệm duy nhất $x_1=x_2=...=x_n=0$ ta nói rằng hệ ${a_1,a_2,...,a_n}$ là một hệ **độc lập tuyến tính (linear independence)**
> Ngược lại nếu : $\exists x_i \ne 0$ sao cho phương trình trên thỏa mãn, thì là một hệ **phụ thuộc tuyến tính (linear dependence)**

2. **Tính chất**
    - Với mỗi $a_i$ sẽ là tổ hợp tuyến tính của các vector còn lại
    - Tập hợp con khác rỗng của hệ độc lập tuyến tính là một hệ độc lập tuyến tính
    - Tập hợp các cột của một ma trận khả nghịch tạo thành một hệ độc lập tuyến tính.
    - Nếu A là một ma trận cao (cột>hàng), thì tồn tại 1 vector b sao cho Ax=b vô nghiệm.
    - Nếu hàng > cột thì n(hàng) vector bất kỳ trong không gian m(cột) chiều tạo thành một hệ phụ thuộc tuyến tính.

# Phương trình đặc trưng (Characteristic Equation) : 
1. **Định nghĩa** : Cho A là một ma trận $k \times k$  và một ma trận đơn vị $I_k$ và một tập các hệ số $\lambda_1, \lambda_2,...,\lambda_k$ thỏa mãn phương trình đa thức (tính định thức )
$$|A -\lambda I| = 0$$ được gọi là **eigenvalues/characteristic roots (aka gốc đặc trưng  ???)** của ma trận A.

<br/>

> Phương trình $|A -\lambda I| = 0$ được gọi là phương trình đặc trưng 

*Vd: page119 sách Appli Multivariate Statistical Analysis*
# Vector đặc trưng (characteristic vector):
1. **Định nghĩa** : Cho A là một ma trận $k \times k$  và một tập các hệ số $\lambda_1, \lambda_2,...,\lambda_k$. Nếu x là một vector khác không mà:
$$Ax = \lambda x$$

> Thì x được gọi là một vector đặc trưng của A với giá trị riêng là $\lambda$

### Tìm vector đặc trưng của ma trận :
1. Giải **eigen equation**.
2. Từ các **eignvalues**  chọn 1 để giải.
3. Kết quả 1 tập tổ hợp tuyến tính. 
*vd: page119-120 Apply Multivariate Statistical Analysis*

>  Nếu $Ax = \lambda x$ ta lấy $e = x / \sqrt{x.x^{'}}$ tương ứng với eigenvector với $\lambda$
>
### Dạng bậc 2 của $Q(x)$ trong $k$ biến là $Q(x) = x^{'}Ax$ (trong đó $x^{'}$ là ma trận chuyển vị của x, điều kiện là A là ma trận vuông).

## **Bất kì một ma trận vuông nào cũng có thể được reconstructed lại bởi eigenvalues và eigenvectors**
*Vd : page121 Apply Multivariate Statistical Analysis 6th*

## Ma trận trực giao :
1. **Định nghĩa **: hiểu đơn giản là một ma trận vuông nếu và chỉ nếu $A^T = A^{-1}$
2. **Định thức : LUÔN BẰNG** $\pm 1$
## Singular - Value Decomposition (SVD):
1. Cho $A$ là một ma trận $m \times k$. Tồn tại một ma trận trực giao $U$ $ m \times m$ và ma trận trực giao $V $ $k \times k$ sao cho:
$$A = U \Sigma V^{'}$$
> Với ma trận $m \times k$ $\Sigma$ có $(i,i)$ có $\lambda_i \geq 0$ với $i = 1,2,3,..., min(m,k)$ và các giá trị khác đều bằng 0. Các hằng số $\lambda > 0$ được gọi là **singular values** của A.
<br/>

2. SVD có thể được thể hiện như là một ma trận mở rộng tùy thuộc vào $rank(A)$. Đặc biệt, tồn tại một hằng số dương $r$ $\lambda_1, \lambda_2,..., \lambda_r$, $r$ trực giao với $m \times 1$ vectors đơn vị $u_1,u_2,..., u_r$. Và $r$ trực giao với $k \times 1$ vector đơn vị $v_1, v_2,...,v_r$ như sau :
$$A = \sum_{i=1}^{r}\lambda_i u_i v_i$$
$$\Leftrightarrow A = U_r \Sigma V_r^{'}$$
> Với $U_r = [u_1,u_2,...,u_r]$, $V_r^{'} = [v_1, v_2,..., v_r]$ và $\Sigma_r$($r \times r$ đ) là ma trận đường chéo, với các phần tử trên đường chéo chính là $\lambda_i$

*Vd : page122 apply multivariate 6th*

#### **Chú ý : Nếu 1 ma trận  $m \times k$ A là xấp xỉ bởi B, có cùng kích thước nhưng có rank thấp hơn, thì tổng bình phương sai lệnh khác nhau là :**
$$ \sum_{i = 1}^{m} \sum_{j = 1}^{k} (a_{ij} - b_{ij})^2 = tr[(A-B)(A-B)^{'}] $$
[định nghĩa ký hiệu "tr" trong linear algebra](https://en.wikipedia.org/wiki/Trace_(linear_algebra))

3. Cho ma trận $m \times k$ A là ma trận với các phần tử là số thực với $ m \geq k $ và **SVD** $U \Sigma V^{'}$. Cho $ s < k = rank(A)$ sau đó:
$$B = \sum_{i=1}^{s}\lambda_i u_i v_i^{'}$$ là hạng là tổng bình phương xấp xỉ của A . Là 
$$tr[(A-B)(A-B)^{'}]$$

Ta có bình phương độ lỗi khi xấp xỉ là :
$$\sum_{i = s  + 1}^{k}\lambda_i^{2}$$

Khi đó ta có :

$$tr[(A-B)(A-B)] = trc[(\Sigma - C)(\Sigma - C)^{'}] \sum_{i=1}^{m}(\lambda_i - c_{ii}^2) + \sum_{i \neq j}\sum_{i \neq j}c_{ij}^2$$
với $C = U^{'}BV$
### Ma trận xác định :

1. Ma trận đối xứng ($A = A^T$) gọi là ma trận xác định dương (xác định âm) nếu mọi vector khác 0 $x \in R^n$ dạng toàn phương (các biến bình phương) được xác định bởi : $Q(x) = x^TAx$ chỉ nhận các giá trị dương (tương tự nhận các giá trị âm). Ma trận đối xứng là xác định dương nếu mọi giá trị riêng của nó là dương(tương tự với xác định âm). Nếu không thỏa điều kiện thì được gọi là ma trận bán xác định dương hoặc âm.

### Maximum likelihood estimation:

1. Ý tưởng : Giả sử có các điểm dữ liệu $\mathbf{x_1, x_2, ..., x_N}$. Giả sử thêm rằng ta đã biết các điểm dữ liệu này tuân theo một phân phối nào đó được mô tả bởi bộ tham số $\theta$. Maximum likelihood estimation là việc đi tìm bộ tham số $\theta$ sao cho xác suất sau đây đạy giá trị lớn nhất:

$$\theta = \max_{\theta} p(\mathbf{x_1,...,x_N} | \theta)$$.

2. Giải thích công thức trên: Giả sử đã biết dạng của mô hình, và mô hình được mô tả bởi bộ tham số $\theta$. Như vậy, $p(x_1|\theta)$ chính là xác suất xảy ra sự kiện $\mathbf{x_1}$ biết rằng mô hình được mô tả bởi bộ tham số $\theta$ (xác suất có điều kiện). Và $p(\mathbf{x_1,...,x_N} | \theta)$ là xác suất để toàn bộ sự kiện $\mathbf{x_1,x_2,...x_N}$ đồng thời xảy ra nên được gọi là **likelihood**. 

3. Ta có hàm phân phối chuẩn với dữ liệu nhiều biến : 

$$p(\mathbf{x | \mu,\Sigma}) = \frac{1}{(2\pi)^{p/2}|\Sigma|^{{n/2}}}\exp({\frac{-1}{2}\sum_{j=1}^{n}(x_j-\mu)^T\Sigma^{-1}(x_j - \mu)})$$

> Biến đổi (Chỗ này chuyển từ tích sang tổng, dùng logarit) :

$$-\log[(2\pi)^{p/2}|\Sigma|^{n/2}] - \frac{-1}{2}\sum_{j=1}^{n}(x_j-\mu)^T\Sigma^{-1}(x_j - \mu)$$

> Khai triển theo logarit bình thường : 

$$-\log{(2\pi)^{p/2}} - \frac{n}{2}\log{|\Sigma|} - \frac{1}{2}\sum_{j=1}^{n}(x_j-\mu)^T\Sigma^{-1}(x_j - \mu))$$

> Dao ham theo bien $\mu$

$$\nabla_{\mu} = (\Sigma^{-1} + (\Sigma^{-1})^T)(x_j - \mu) = 0$$

> Thu được :
$$\mu = \frac{\sum_{j=1}^{n}x_j}{n}$$

> Đạo hàm theo biến $\Sigma$

$$\nabla_{\Sigma} = -\frac{n}{2}(\Sigma^{-1})^T - \frac{1}{2} (\Sigma^{-1})^T(x_j - \mu)(x_j - \mu)^T (\Sigma^{-1})^T$$

> Chia cho 2:
$$\nabla_{\Sigma} = -n(\Sigma^{-1})^T + (\Sigma^{-1})^T(x_j - \mu)(x_j - \mu)^T (\Sigma^{-1})^T = 0$$

> Đơn giản 2 bên  $(\Sigma^{-1})^T$, ta có :

$$\sum_{j=1}^{n}(x_j - \mu)(x_j - \mu)^T (\Sigma^{-1})^T = n$$

> Ta có $(\Sigma^{-1})^T = (\frac{1}{\Sigma})^T = \frac{1}{\Sigma^T}$
> Cho nên:
$$\sum_{j=1}^{n}(x_j - \mu)(x_j - \mu)^T = n\Sigma^T$$
> Vì $\Sigma^T = \Sigma$ (Ma trận đối xứng), nên :

$$\Sigma = \frac{\sum_{j=1}^{n}(x_j - \mu)(x_j - \mu)^T }{n}$$

*_ Link tính đạo hàm ma trận : https://goo.gl/JKg631_*
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAzMzE5MDczMl19
-->