> Read Clean Architecture (68/364)
# Event Sourcing
> Definition [here](https://martinfowler.com/eaaDev/EventSourcing.html)
- A strategy wherein we store the transactions, but not the state. When state is required, we simply apply all the transactions from the beginning of time.

# SOLID PRINCIPLE

## SRP : The Single Responsibility Principle

1. A Module should be responsible to one, and only one, actor.

## OCP : The Open-Closed Principle

## LSP : The Liskov Substitution Principle

## ISP : The Interface Segregation Principle

## DIP : The Dependency Inversion Principle

1. _**Don't refer to violate concrete classes**_ : Refer to _abstract interface_ instead. 
2. _**Don't derive from violate concrete classes**_ : in statically typed languages (C/C++, Java, etc). _Inheritance_ is the strongest, and most rigid, of all the source code relationships; consequently,  it should be use with great care. In dynamic typed languages (Python, etc), inheritance, 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMTI5OTQ4MzEsNTgwNTY3MTIsLTEwNT
U1Nzg1NDAsMTc1MjMyNDUyOSwyMTEwOTQ1MjY1XX0=
-->