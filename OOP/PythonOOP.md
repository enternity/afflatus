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
# ```super()``` in Single Inheritance :
```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
```
# What can ```super()``` do for you :
```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
```
> Nói dễ hiểu là tính toán từ lớp cha, xong rồi lấy kết quả đấy để tính toán tiếp.
# A ```super()``` Deep Live :
1. ```super()``` 
<!--stackedit_data:
eyJoaXN0b3J5IjpbODk0NDU0MzUwXX0=
-->