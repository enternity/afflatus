 Bài viết này được phiên dịch và hiểu theo người dịch. Nên đôi khi có nhiều lúc hiểu sai, hoặc không đủ. Mong góp ý
> Dựa theo cuốn : **"Clean Code : A Handbook of Agile Software Craftmanship"**

> prototype for this article
> #.#.#.# : cho các lời khuyên
> Màu $\color{blue}blue$ : cho nên làm
> Màu $\color{red}red$ : cho nên tránh
> 
# Giới thiệu :
Phần giới thiệu được cover hết trong một tấm ảnh 
<center><img src="https://mk0osnewswb2dmu4h0a.kinstacdn.com/images/comics/wtfm.jpg"></center>

# Chapter 1: Clean code
Chapter này chủ yếu nói về việc vì sao nên "Clean Code". Được dẫn chứng rất nhiều các "best-programer" như Uncle Bob, etc. Nếu thích thì có thể đọc thêm. 
# Chapter 2: Meaningful Names
Một lý do cực kì đơn giản để giải thích vì sao nên viết một biến, một class có nghĩa là có ai có thể chịu được cách viết như sau để mô khai báo lớp Dog không?

*Ví dụ 1:*
```java
public class X{
	private String a;
	private int b;
	public void setName(String name){
		this.a = name;
	}
	public void setB(int c){
		this.b = c;
	}
}
```
Ai có thể chịu được đoạn code trên thì tại hạ cũng xin quỳ.
Vì thế chú ý quan trọng đầu tiên :
#### $\color{blue}\text{Hãy dùng một cái tên có liên quan.}$
Ở ví dụ trên, chúng ta sẽ sửa lại như sau
Sửa ví dụ 1:
```java
public class Dog{
	private String dogBreed;
	private int age;
	public void setDogBreed(String dogBreed){
		this.dogBreed = dogBreed;
	}
	public void setAge(int age){
		this.age = age;
	}
}
```
> Dễ đọc hơn liền :smile:

#### $\color{blue}\text{Tránh dùng thông tin sai lệch}$
	
Có nghĩa là ví dụ bạn có một danh sách các ```accounts``` thì đừng đặt tên là ```accountList``` nếu nó không phải là một ```List```. Đôi khi sẽ bị confuse đấy :smile: . Thay vào đó chúng ta sẽ đặt tên là ```accountGroup```, ```bunchOfAccount``` hoặc ```accounts``` sẽ tốt hơn.

Và đừng dùng những kí tự tượng tự như số như ```0, l``` để đặt tên nhé. Ai mà đọc cho được.

Ví dụ 2:
```java
int O = 1;
if(O == 1){
	LOGGER.info("Duc dep trai")
} else{
	LOGGER.info("Duc xau trai")
}
```

Bạn xem đoạn code trên và tự rút ra nhận xét nhé :smile:

####  $\color{blue}\text{Phân biệt có ý nghĩa :}$
Ví dụ như trong một scope, thì không thể cùng một tên. Vì thế nhiều người sẽ cố ý gõ sai một biến và sau đó run. Đương nhiên sẽ chạy được. Tuy nhiên, sẽ khó khăn hơn trong việc debug và đọc code gây dễ lẫn lộn.

#### $\color{red}\text{Number-series naming - legend lỗi của sinh viên.}$
Cho một đoạn code sau.
```python
a1 = [5,6,7,8,9,10,10,2,3,4,5]
a2 = [6,7,5,3,1,3,5,1,3,5,6,2]
print(f"Sum of score in two semesters = {} ", a1 + a2)
```
Thay vào đó :
```python
scoreFirstSemester =  [5,6,7,8,9,10,10,2,3,4,5]
scoreSecondSemester = [6,7,5,3,1,3,5,1,3,5,6,2]
print(f"Sum of score in two semesters = {} ", scoreFirstSemester + scoreSecondSemester)
```

> Cái nào dễ đọc hơn và dễ hiểu hơn, hãy để lương tâm bạn tự trả lời nhé :heart: :heart: :heart:

Và đừng dùng những từ như ```Info, Data``` cho cùng một biến, class, hàm. Đại loại như ```PersonalInfo``` hay ```PersonalData```, vì thiệt chất ```info, data``` nó gần như cùng một nghĩa. Nên để hiểu đúng thì phải vô đọc code. Thế thì không tốt đâu nhé :wink: :wink:

#### $\color{blue}\text{Dùng những cái tên dễ search}$
Ví dụ bạn muốn định nghĩa số lượng tối đa học sinh trong một lớp. Thì thay vì định nghĩa thế này
```java
class public Class{
	private final int numberOfStudent = 21;
}
```
Hãy làm thế này :
```java
class public ConfigClass{
	public static final int MAX_STUDENTS_PER_CLASS = 7;
}
```
Và class ```Class``` này sẽ là
```java
class public Class{
	private final int numberOfStudent = MAX_STUDENTS_PER_CLASS;
}
```
> Việc search hay gì đó sẽ trở nên dễ dàng hơn. Còn làm mất đi **magical number**
#### $\color{blue}\text{Class name phải là danh từ}$ 
Không còn gì phải bàn cãi nữa. :smile: :wink:
#### $\color{blue}\text{Method phải là động từ}$ 
Đương nhiên rồi :smile: :wink:

# Function:
## Luật đầu tiên : Hàm càng ngắn càng tốt (don't hit miss my idea)
## Luật thứ hai : Do one thing.
## Luật ba : [step down](https://dzone.com/articles/the-stepdown-rule#:~:text=The%20Stepdown%20Rule%20tells%20us,we're%20writing%20unit%20tests.)

## Function Argument :
- Lý tưởng nhất vẫn là function say no với tham số :wink: :wink:. Ba tham số trở lên là điều thực sự không nên làm một miếng nào cả. Làm khó khăn hơn cho việc testing hơn. Dùng tổ hợp để xác định mức độ phức tạp hơn đi nào =))).
- Thực sự không nên dùng flag argument. Mình đã từng làm thế và nó work, nhưng code xấu xí vcl :smile: :smile:

# DON'T REPEAT YOURSELF. Nhắc lại DON'T REPEAT YOURSELF :smile:
Bị trùng lắp có thể là nguồn gốc của tất cả các vấn đề của software. Rất nhiều nguyên tắc được tạo để chỉ duy có mục đích kiểm soát hoặc loại bỏ việc trùng lặp. 


> Dừng tại trang 53

<!--stackedit_data:
eyJoaXN0b3J5IjpbNjc5MzYxMzYzXX0=
-->