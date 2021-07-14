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
2. _**Don't derive from violate concrete classes**_ : in statically typed languages (C/C++, Java, etc). _Inheritance_ is the strongest, and most rigid, of all the source code relationships; consequently,  it should be use with great care. In dynamic typed languages (Python, etc), inheritance is less of a problem, but it is still a dependency - and caution is always the wisest choice.
3. _**Don't override concrete function**_ : often require source code dependencies. When override those functions, we do not eliminate 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk3MTM2MjQwMiwtMTExMjk5NDgzMSw1OD
A1NjcxMiwtMTA1NTU3ODU0MCwxNzUyMzI0NTI5LDIxMTA5NDUy
NjVdfQ==
-->