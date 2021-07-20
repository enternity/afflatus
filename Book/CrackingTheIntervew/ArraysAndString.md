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
> Roughly : $\frac{N}{2} + \frac{N}{4} + \cdots + 2 + 1 \simeq 1$
> Inserting N elements takes $O(N)$ work total.
## StringBuilder

## Interview Questions 
1. Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
2. Given two strings, write a method to decide if one is a permutation of the other.
3. Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
	EXAMPLE
	Input: "Mr John Smith ", 13
	 Output: "Mr%20John%20Smith" 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMDQyOTg5NzMsLTE5MjE1ODU1MywtMz
I4MDg0MzU5XX0=
-->