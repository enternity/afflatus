# Multiple Inheritance :
```python
class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass
```
<center><img src="https://cdn.programiz.com/sites/tutorial2program/files/MultipleInheritance.jpg"></center>

> Một lúc kế thừa từ nhiều thằng (always phức tạp).

# Multi-level inhertance :
```python
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass
```
<center><img src="https://cdn.programiz.com/sites/tutorial2program/files/MultilevelInheritance.jpg"></center>

> Gia đình phả hệ, nghĩa là: con kế thừa cha, cha kế thừa từ ông nội,

## Hierarchical Inheritance :
> Một lớp cha có thể được kế thừa từ nhiều lớp con khác nhau.

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
1. ```super()``` có thể có 2 *params*. Param đầu tiên là lớp con, param thứ hai instance của lớp con
# ```super()``` trong Đa Kế Thừa :
<center><img src="https://files.realpython.com/media/multiple_inheritance.22fc2c1ac608.png"></center>

# Resolution order in  Python Inheritance:
<center><img src="https://media.geeksforgeeks.org/wp-content/uploads/220px-diamond_inheritance-svg.png"></center>
<center><i>class D -> class B -> class C -> class A</i></center>

> Dùng function ```__mro__``` hay ```mor()``` để  tìm thứ tự kế thừa.

# Metaclasses 
## MetaPrograming
[https://stackoverflow.com/questions/514644/what-exactly-is-metaprogramming](https://stackoverflow.com/questions/514644/what-exactly-is-metaprogramming)

> Python hỗ trợ một form của metaprogramming cho classes gọi là **metaclasses**

## Old-Style Classes
Với old-style classes, class và type không phải là 1 thứ giống nhau. Instance của old-style class luôn được implemented từ *built-in* được gọi là *instance*. Nếu đối tượng là một instance của old-style class, ```obj.__class__``` được chỉ định bởi lớp, tuy nhiên ```type(obj)``` luôn là một instance. Python2.7 :
```python
class Foo:
	pass
x = Foo()
x.__class__
# <class __main__.Foo at 0x00000abcd>
type(x)
# <type 'instance'>
```
## New-style Classes
Với new-style classes thống nhâts concepts của class và type. Nếu đối tượng là 1 instance của new-style class, ```type(obj)``` sẽ như ```obj.__class__```
```python
class Foo:
	pass
obj = Foo()
obj.__class__
# <class '__main__.Foo'>
type(obj)
# <class '__main__.Foo'>
obj.__class__ is type(obj)
# True
```
```python
n = 5
d = {'x':1, 'y'"2}
class Foo:
	pass
x = Foo()
for obj in (n,d,x):
	print(type(obj) is obj.__class__)

# True
# True
# True
```
## Type and Class
Trong Python3, tất cả các class đều là new-style classes. Do đó, trong python3 objects'type và lớp của object đó có thể hoán đổi cho nhau.

Nên nhớ, tất cả mọi thứ trong Python đều là object. Class cũng là object. Vì thế, class cũng phải có type. Vậy type của class là gì ?
```python
class Foo:
	pass
x = Foo()
type(x)
# <class '__main__.Foo'>
type(Foo)
# <class 'type'>
```
Type của x là lớp ```Foo```.  Type của ```Foo``` cũng chính là nó luôn. Nhìn chung, type của bất kì new-style class là type. :smile:
```python
type(type)
# <class 'type'>
```
:joy::joy::joy::joy::joy::joy::joy::joy::joy:

<center><img src="https://files.realpython.com/media/class-chain.5cb031a299fe.png"></center>

Đại khái là :
- x là instance của class Foo.
- Foo là instance của type metaclass
- type cũng chính là instance của type metaclass, vậy nên gọi là instance của chính nó.

## Định nghĩa Class một các linh động hơn.
Có thể gọi ```type()``` với 3 tham số. ```(<name>,<bases>,<dct>)``` :
- ```<name>``` : tên của class. Nó sẽ trở thành thuộc tính ```__name__```  của lớp.
- ```<bases>``` : một tuple class mà nó sẽ kế thừa.
- ```<dct>``` : định nghĩa class body. Nó sẽ trở thành thuộc tính ```__dict__``` của lớp.

Khi gọi ```type()``` đơn giản nó sẽ tạo ra một lớp mới theo các chỉ định như ở trên.

1. Ví dụ 1:
```python
Foo = type('Foo',(),{})
x = Foo()
x
# <__main__.Foo object at 0x04ABCD>
```
2. Ví dụ 2:
```python
Bar = type('Bar',(Foo,), dict(attr=100))
x = Bar()
x.attr
# 100
x.__class__
# <class '__main__.Bar'>
x.__class__.__bases__
# (<class '__main__.Foo'>,)
```
## Custom Metaclasses
```python
class Foo:
	pass
f = Foo()
```
Khi tạo ra instance của lớp ```Foo``. Trình tự khởi tạo sẽ là :
- Phương thức ```__call__()``` lớp cha của ```Foo``` được gọi. Lúc này Foo là new-style class. Lớp cha của nó là metaclass, nên type của phương thức```__class__()``` được viện dẫn.
- Phương thức ```__call__()```  viện dẫn theo kiểu :
	- ```__new__()```
	- ```__call__()```
Nếu Foo không định nghĩa ```__new__(),__init__()```, thì nó sẽ được kế thừa từ lớp cha của nó. Tuy nhiên nếu Foo có định nghĩa thì nó sẽ override.
```python
def new(cls):
	x = object.__new__(cls)
	x.attr = 100
	return x
Foo.__new__ = new
f = Foo()
f.attr
# 100
g = Foo()
g.attr
# 100
```
Định nghĩa metaclass xuất phát từ type.
```python
class Meta(type):
	def __new__(cls, name, bases, dct):
		x = super().__new__(cls, name, bases, dct)
		x.attr = 100
		return x
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyODM1MTcwNjIsMTc5MzM2NTkzMiwtMT
Q2MzU3NzQ5MCw4OTM3ODI3ODcsMzI3OTA0MTEzXX0=
-->