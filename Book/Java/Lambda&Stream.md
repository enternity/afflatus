# Lambda
### There are four types of method references available.

-   Static method reference.
-   Instance Method (Bound receiver).
-   Instance Method (UnBound receiver).
-   Constructor reference.
### **Prefer lambdas to anonymous classes.**

> Don't do this
```java
 // Anonymous class instance as a function object - obsolete! 

 Collections.sort(words, new Comparator<String>() {
       public int compare(String s1, String s2) { 
			 return Integer.compare(s1.length(), s2.length());
       } 
});
```

> We should do like this
```java
 // Anonymous class instance as a function object - obsolete! 

 Collections.sort(words, (s1, s2) ->  Integer.compare(s1.length(), s2.length()));
});
```
### **Prefer method references to lambdas**
```java
 map.merge(key, 1, (count, incr) -> count + incr);
```

```java
 map.merge(key, 1, Integer::sum)
```
###  ***Favor the use of standard functional interfaces.***

# Stream
### Use streams judiciously
1. Three primitive types are supported: int, long and double.
2. Stream pipelines are evaluated lazily: evaluation doesn’t start until the terminal operation is invoked, and data elements that aren’t required in order to complete the terminal operation are never computed. This lazy evaluation is what makes it possible to work with infinite streams. Note that a stream pipeline without a terminal operation is a silent no-op, so don’t forget to include one.
### Prefer Collection to Stream as a return type 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg5MDc0NjU2LDM3NjExNzk1NiwzMzUyND
ExMDIsLTUyMzYyMjE2NV19
-->