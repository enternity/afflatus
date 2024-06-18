# Memory allocation of primitive,  non-primitive data types

> https://www.scientecheasy.com/2020/06/memory-allocation-primitive-nonprimitive.html/#:~:text=%E2%9E%B2%20In%20Java%2C%20all%20data,the%20object%20on%20the%20heap.




1. Primitive Type: `int, byte, short, long, float, double, boolean, char`

- Store directly on the stack
2. Non-primitive type: 

- The stack holds a pointer to the object on the heap. When setting a reference type variable euqal to another reference type variable, a copy of only the pointer is made.

![img](https://www.scientecheasy.com/wp-content/uploads/2018/06/memory-allocation.png)

