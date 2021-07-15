# Stack memory 
> _Stack memory is responsible for holding references to heap objects and for storing value types (also known in Java as primitive types), which hold the value itself rather than a reference to an object from the heap._

> _In addition, variables on the stack have a certain visibility, also called  **scope**. Only objects from the active scope are used. For example, assuming that we do not have any global scope variables (fields), and only local variables, if the compiler executes a method’s body, it can access only objects from the stack that are within the method’s body. It cannot access other local variables, as those are out of scope. Once the method completes and returns, the top of the stack pops out, and the active scope changes._

This due to the fact that the stack memory in Java is allocated per Thread. Therefore, each time a Thread is created and started, it has its own stack memory — and cannot access another thread’s stack memory. 
# Minimize mutability
- To make class immutable, we have 5 rules:
1. Don't provide methods that modify objects state
2. Ensure that the class can't be extended (make class final)
3. Make all fields final
4. Make all fields private
5. Ensure exclusive access to any mutable components



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NTgwNzc2OTgsLTE1MzI4ODAxODVdfQ
==
-->