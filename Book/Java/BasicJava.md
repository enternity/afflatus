> This article reference from dzone.com
# Stack Memory 
> _Stack memory is responsible for holding references to heap objects and for storing value types (also known in Java as primitive types), which hold the value itself rather than a reference to an object from the heap._

> _In addition, variables on the stack have a certain visibility, also called  **scope**. Only objects from the active scope are used. For example, assuming that we do not have any global scope variables (fields), and only local variables, if the compiler executes a method’s body, it can access only objects from the stack that are within the method’s body. It cannot access other local variables, as those are out of scope. Once the method completes and returns, the top of the stack pops out, and the active scope changes._

This due to the fact that the stack memory in Java is allocated per Thread. Therefore, each time a Thread is created and started, it has its own stack memory — and cannot access another thread’s stack memory. 

# Heap Memory
> _This part of memory stores the actual object in memory. Those are referenced by the variables from the stack._

> The `new` keyword is responsible for ensuring that there is enough free space on heap

1. There exists _**only one**_ heap memory for each running JVM process. Therefore, this is a shared part of memory regardless of how many threads are running.  The heap itself is divided into a few parts, which facilitates the process of garbage collection.

# Reference Type 
1. _**Strong Reference**_ 

```java
StringBuilder build = new StringBuilder();
```
At the above, we actually hold a strong reference to an object from the heap. The object on the heap it is not garbage collected while there is a strong reference pointing to it, or if it is strongly reachable through a chain of strong references.
2. _**Weak Reference**_
```java
WeakReference<StringBuilder> reference = new WeakReference()<new StringBuilder()>;
```
In simple terms, a weak reference to an object from the heap is most likely to not survive after the next garbage collection process

3. _**Soft Reference**_

These types of references are used for more memory-sensitive scenarios, since those are going to be garbage collected only when your application is running low on memory. Therefore, as long as there is no critical need to free up some space, the garbage collector will not touch softly reachable objects. Java guarantees that all soft referenced objects are cleaned up before it throws an `OutOfMemoryError`

4. _**Phantom Reference**_

Used to schedule post-mortem cleanup actions, since we know for sure that objects are no longer alive. Used only with a reference queue, since the `.get()` method of such references will always return `null`**.** These types of references are considered preferable to **finalizers.**

## How `Strings` are referenced
1. Example 1 
```java
String myExName = "Idiot! You don't have gf";
String myGirlFriendName = "Idiot! You don't have gf";

if (myExName == myGirlFriendName) {
     System.out.println("Yup, both are the same");
} else {
    System.out.println("They are not the same");
}
```
> When we run above code, we will have 
```Yup, both are the same```

Strings are immutable, meaning that each time you do something with a string, another object is actually created on the heap. For strings, Java manages a string pool in memory. This means that Java stores and reuse strings whenever possible. This is mostly true for string literals

2. Example

# Minimize mutability
- To make class immutable, we have 5 rules:
1. Don't provide methods that modify objects state
2. Ensure that the class can't be extended (make class final)
3. Make all fields final
4. Make all fields private
5. Ensure exclusive access to any mutable components



<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0NDY1ODQyMTMsLTE1MzI4ODAxODVdfQ
==
-->