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

2. Example 2
```java
String one = "one";
String oneInt = new Integer(1).toString();

if (one == oneInt) {
     System.out.println("Yup, both are the same");
} else {
    System.out.println("They are not the same");
}
```
> When we run above code, we will have 
```They are not the same```

> But when we do like this
```String oneInt = new Integer(1).toString().intern()```  we will have the same result as a example 1.
## Garbage Collection Process 
To go a bit deeper into the details, let’s mention a few things first:

-   This process is triggered automatically by Java, and it is up to Java when and whether or not to start this process.
    
-   It is actually an expensive process. When the garbage collector runs, all threads in your application are paused (depending on the GC type, which will be discussed later).
    
-   This is actually a more complicated process than just garbage collecting and freeing up memory.

### **Tips and Tricks**

-   To minimize the memory footprint, limit the scope of the variables as much as possible. Remember that each time the top scope from the stack is popped up, the references from that scope are lost, and this could make objects eligible for garbage collecting.
    
-   Explicitly refer to  `null` obsolete references. That will make objects those refer to eligible for garbage collecting.
    
-   Avoid finalizers. They slow down the process and they do not guarantee anything. Prefer phantom references for cleanup work.
    
-   Do not use strong references where weak or soft references apply. The most common memory pitfalls are caching scenarios,when data is held in memory even if it might not be needed.
    
-   JVisualVM also has the functionality to make a heap dump at a certain point, so you could analyze, per class, how much memory it occupies.
    
-   Configure your JVM based on your application requirements. Explicitly specify the heap size for the JVM when running the application. The memory allocation process is also expensive, so allocate a reasonable initial and maximum amount of memory for the heap. If you know it will not make sense to start with a small initial heap size from the beginning, the JVM will extend this memory space. Specifying the memory options with the following options:
    
    -   Initial heap size  `-Xms512m`  – set the initial heap size to 512 megabytes.
        
    -   Maximum heap size  `-Xmx1024m`  – set the maximum heap size to 1024 megabytes.
        
    -   Thread stack size  `-Xss1m`  – set the thread stack size to 1 megabytes.
        
    -   Young generation size  `-Xmn256m`  – set the young generation size to 256 megabytes.
        
-   If a Java application crashes with an `OutOfMemoryError`  and you need some extra info to detect the leak, run the process with the `–XX:HeapDumpOnOutOfMemory`  parameter, which will create a heap dump file when this error happens next time.
    
-   Use the `-verbose:gc`  option to get the garbage collection output. Each time a garbage collection takes place, an output will be generated.
# Minimize mutability
- To make class immutable, we have 5 rules:
1. Don't provide methods that modify objects state
2. Ensure that the class can't be extended (make class final)
3. Make all fields final
4. Make all fields private
5. Ensure exclusive access to any mutable components


# Generics problem
## Don't use `RawType` 
> Example : `List a = ...;`

- In short, if you like `List` . When you try to **cast** of element in this `List`, maybe will throw `CastClassException`
- Instead of above example we should like the following :
`List<User> users = ...;`

> When compiling, compiler will throw error if we make a mistake when to try cast illegal class.

> _**If we use raw types, we lose all the safety and expressiveness benefits of generics**_

# Overloading vs Overriding
1. Overloading is a term used to describe when two methods have the same name but differ type in the type or number of arguments.
2. Overriding, however, occurs when a methods share the same name and function signature as another methods in its super class
# Collections Framework
1. ArrayList is a dynamic resizing array. 
2. Vector similar with 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY3MTMzMDA4MSwxNTMzMDU0OTc3LDE5OD
IxNjEwNzksNDgxMzcwNzczLC0xMDA3MjQ5MTg4LC0xNDQ2NTg0
MjEzLC0xNTMyODgwMTg1XX0=
-->