# 1) Class Loader Subsystem

The  **JVM resides on the RAM**. During execution, using the Class Loader subsystem, the class files are brought on to the RAM. This is called Java’s  **dynamic class loading**  functionality.  It loads, links, and initializes the class file (.class) when it refers to a class for the first time at runtime (not compile time).

## 1.1) Loading

Loading compiled classes (.class files) into memory is the major task of Class Loader. Usually, the class loading process starts from loading the main class (i.e. class with  `static main()`  method declaration). All the subsequent class loading attempts are done according to the class references in the already-running classes as mentioned in the following cases:

-   When bytecode make a static reference to a class (e.g.  `System.out`)
-   When bytecode create a class object (e.g.  `Person person = new Person("John")`)

There are 3 types of class loaders (connected with inheritance property) and they follow 4 major principles.

**_1.1.1) Visibility Principle_**

This principle states that Child Class Loader can see the class loaded by Parent Class Loader, but a Parent Class Loader cannot find the class loaded by Child Class Loader.

**_1.1.2) Uniqueness Principle_**

This principle states that a class loaded by parent should not be loaded by Child Class Loader again and ensure that duplicate class loading does not occur.

**_1.1.3) Delegation Hierarchy Principle_**

In order to satisfy above 2 principles, JVM follows a hierarchy of delegation to choose the class loader for each class loading request. Here, starting from the lowest child level, Application Class Loader delegates the received class loading request to Extension Class Loader and then Extension Class Loader delegates the request to Bootstrap Class Loader. If the requested class found in Bootstrap path, the class is loaded. Otherwise the request again transfers back to Extension Class Loader level to find the class from Extension path or custom-specified path. If it also fails, the request comes back to Application Class Loader to find the class from System class path and if Application Class Loader also fails to load the requested class, then we get the run time exception —  `java.lang.ClassNotFoundException`  .

**_1.1.4) No Unloading Principle_**

Even though a Class Loader can load a class, it cannot unload a loaded class. Instead of unloading, the current class loader can be deleted, and a new class loader can be created.

![](https://miro.medium.com/max/1280/0*MCf4PciEbMGwOL6L)

_Java Class Loaders — Delegation Hierarchy Principle (Image: StackOverflow.com)_

-   **Bootstrap Class Loader**  loads standard JDK classes from rt.jar such as core Java API classes present in the bootstrap path — $JAVA_HOME/jre/lib directory (e.g. java.lang.* package classes). It is implemented in native languages like C/C++ and acts as parent of all class loaders in Java.
-   **Extension Class Loader**  delegates class loading request to its parent, Bootstrap and if unsuccessful, loads classes from the extensions directories (e.g. security extension functions) in extension path — $JAVA_HOME/jre/lib/ext or any other directory specified by the java.ext.dirs system property. This Class Loader is implemented in Java by the sun.misc.Launcher$ExtClassLoader class.
-   **System/Application Class Loader** loads application specific classes from system class path, that can be set while invoking a program using -cp or -classpath command line options. It internally uses Environment Variable which mapped to java.class.path. This Class Loader is implemented in Java by the sun.misc.Launcher$AppClassLoader class.

_NOTE: Apart from the 3 major Class Loaders discussed above, a programmer can directly create a_ **_User-defined Class Loader_** _on the code itself. This guarantees the independence of applications through class loader delegation model. This approach is used in web application servers like Tomcat to make web apps and enterprise solutions run independently._

Each Class Loader has its  **namespace**  that stores the loaded classes. When a Class Loader loads a class, it searches the class based on  **FQCN**  (**Fully Qualified Class Name**) stored in the namespace to check whether or not the class has been already loaded. Even if the class has an identical FQCN but a different namespace, it is regarded as a different class. A different namespace means that the class has been loaded by another Class Loader.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM2NTU1MzAzMV19
-->