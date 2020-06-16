# Class versus Object:

1. **Class** : là một ***mô hình*** chi tiết tạo ra Object. Định nghĩa tất cả các thuộc tính, phương thức cần có của một đối tượng.
2. **Object**: phải thuộc 1 class nào đó. Object là một ***thể hiện*** của một class.
# Các đặc tính của OOP :

## **I. Encapsulation** (*Tính đóng gói*) :
1. ***Định nghĩa*** :  là để che dấu đi xử lý bên trong của đối tượng. Những đối tượng khác không thể tác động trực tiếp và thay đổi trạng thái của đối tượng. Chỉ có thể tác động qua các *method public* của đối tượng.
## **II. Inheritence** (*Tính kế thừa*) :
1. ***Định nghĩa*** : kế thừa từ lại những tính năng của đối tượng khác đã có. Nhằm giảm tránh lặp code. Chú ý : Giả sử có 3 đối tượng: phương tiện, xe, chim. Đối tượng **xe** sẽ được **kế  thừa** từ đối tượng **phương tiện**, chứ không kế thừa từ lớp chim. Phải đảm bảo tính **đúng đắn** khi kế thừa.

## **III. Polymorphism** (*Tính đa hình*) :
1. ***Định nghĩa*** : Các lớp *khác nhau* có thể hiểu thông điệp khác nhau. Ví dụ có 3 lớp : ***động vật, chó, mèo***. Lớp ***chó, mèo*** cùng kế thừa phương thức ***kêu()*** của lớp ***động vật*** . Tuy nhiên, ***chó*** kêu khác,  ***mèo*** kêu khác.

## **IV.  Abstraction** (*Tính trừu tượng*) :
1. ***Định nghĩa*** : Là phương pháp trừu tượng hóa định nghĩa lên những hành động, tính chất của loại đối tượng nào đó cần phải có
# Interface versus Abstract class.
1. **Interface**:
	- Không phải là một *class*.
	- Chỉ chứa những *method/properties* nhưng không thực thi.
	- Như một khuôn mẫu, một khung để *implement* và *follow.*
	- Các lớp có thể *implement* nhiều *interface*.
	- Là một *contract*, các class *implement* phải triển khai method theo như các interface định nghĩa.
2. **Abstract**:
	- Khá giống *interface* nhưng làm được nhiều thứ hơn. 
	- Có 2 loại *method* là *abstract method* và *normal method*:
		- *Abstract Method* : là method ***trống*** không có thực thi (*implement*).
		- *Normal Method* : là một method có *implement*.
	- Các lớp chỉ kế thừa từ **1** *abstract class*.
	- Hướng đến tính năng và những tính năng có thực thi được sử dụng làm hàm chung cho các class extend.
3. **Lợi, hại** :

|         | Interface           | Abstract class  |
| ------------- |-------------| -----|
| Ưu       | - Kế thừa nhiều interface <br/>- Xây dựng bộ khung mẫu và tuân theo <br/>- Quản lý, nắm bắt các chức năng dễ dàng  | - Linh động các method <br/>- Các extend method có thể *overide* hoặc không|
| Nhược      | - Định nghĩa thêm tính năng, cần implement tất cả, khả năng cao sẽ không có xử lý gì. | - Không thể *extend* nhiều abstract class|

4. **Khi nào dùng cái nào**:
	- *Interface* : tạo dựng một bộ khung chuẩn, gồm những chức năng và module mà project này buộc phải có.
	- *Abstract class* : khi định nghĩa một đối tượng có những chức năng A,B,C trong đó tính năng A,B chắc chắn sẽ thực thi theo cách nào đó, còn tính năng C phải tùy thuộc vào đối tượng cụ thể là gì.

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA5NDMxMTI5Ml19
-->