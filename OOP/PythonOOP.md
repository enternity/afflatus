# Instance Attributes
1. Dùng ```__init__(self, *args, **kwargs)``` để khởi tạo.  Khởi tạo bằng ```__init__()``` thì cho để dành riêng cho mỗi đối tượng cùng 1 lớp.
# Class Attributes:
1. Khai báo ngoài ```__init__()``` . Ví dụ :
```python
class Dog:
	# Class Attribute
	legs = 4
	def __init__(self, name, age):
		self.name = name
		self.age  = age
```
> Thuộc tính lớp dùng cho **tất cả** các đối tượng thuộc cùng một lớp.
# Instantiating Objects:
1. Khi bắt đầu bằng khởi tạo ```Dog()```. Tạo ra 2 objects khác nhau.
# ```super()``` in Python :
1. **Để làm gì** : cho bạn truy cập các method trong lớp cha từ lớp con kế thừa nó. ```super()``` return một đối tượng tạm của lớp cha cho phép bạn gọi methods lớp cha. Cho phép trao đổi method với số lượng thay đổi code bé nhất.
2. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAwODkxODk2N119
-->