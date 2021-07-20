# Arrays and String
## Hash Tables 
In simple implementation, we do the following :
1. First, compute the key's hash code. Note that two different keys could have the same hash code.
2. Map the hash code to an index in the array.
3. At this index, there is a linked list of key and values. Store the key value in this index. We _**must**_ use _linked list_ because collisions.
> We can implement the hash table with a balanced binary search tree. And give us `O(logN)` lookup time.
## ArrayList & Resizable Array
To resizable array approach :
- First capacity increase : 1 element copy
- Second capacity increase : 2 element copy
- Third capacity increase : 4 element copy
....
- Previous capacity increase : $n/16$ element copy
- Previous capacity increase : $n/8$ element copy
- Previous capacity increase : $n/4$ element copy
- Final capacity increase : $n/2$ element copy
> Roughly : $\frac{N}{2} + \frac{N}{4} + \cdots + $
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTAyNDk5MDE1MCwtMzI4MDg0MzU5XX0=
-->