# Arrays and String
## Hash Tables 
In simple implementation, we do the following :
1. First, compute the key's hash code. Note that two different keys could have the same hash code.
2. Map the hash code to an index in the array.
3. At this index, there is a linked list of key and values. Store the key value in this index. We _**must**_ use _linked list_ because collisions.
> We can implement the hash table with a balanced binary search tree. And give us `O(logN)` lookup time.
## ArrayList & Resizable Array
To resizea
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzAyNzk0MDAxLC0zMjgwODQzNTldfQ==
-->