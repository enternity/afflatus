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
# Python Object Inheritance:
1. Dùng cho các lớp con ***extend, overide*** các chức năng.
````python
class Animal:
	legs = 0
	def __init__(self):
		pass
class Dog(Ani)
````
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNzM4ODY1OV19
-->