# CREATIONAL DESIGN PATTERN 

> These design patterns are all about class _**instantiation or object creation**_. 


> Creational design patterns are the _**Factory Method, Abstract Factory, Builder, Singleton, Object Pool, and Prototype.**_

## Factory Method 

> View on: [https://refactoring.guru/design-patterns/factory-method](https://refactoring.guru/design-patterns/factory-method)

1. **Application** :
- Use the Factory Method when you _**don’t know beforehand the exact types and dependencies**_ of the objects your code should work with.
- Use the Factory Method when you want to _**provide users of your library or framework with a way to extend its internal components**_.
- Use the Factory Method when you want to _**save system resources by reusing existing objects**_ instead of rebuilding them each time.

> Example [here](https://refactoring.guru/design-patterns/factory-method/java/example)

|Pros|Cons|
|---|---|
|- Avoid tight coupling between the creator and the concrete products. <br/> - _Single Responsibility Principle_ <br/> - _Open-Close Principle_| - The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern.|
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc3NjcwNTEwMV19
-->