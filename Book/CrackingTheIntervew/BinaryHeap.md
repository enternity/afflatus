# Binary Heap
## Binary heap is a Binary Tree with following properties
1. It's a complete tree.
2. A binary heap is either Min heap or Max heap. In a Min Binary Heap, the key at root must be a minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binary Tree. Max Binary Heap is similar to Min Heap.
## How is Binary Heap represented?
- The root element will be at `Arr[0]`

|`Arr[(i - 1) /2 ]`|Returns the parent node|
|---|---|---|
|**`Arr[(2 * i) + 1]`**|**Returns the left child node**|
|**`Arr[(2 * i) + 2]`**|**Returns the right child node**|
## Applications of Heaps:
1. Heap sort: `O(nlogn)`
2. Priority Queue
3. Graph algorithms : the priority queues are especially used in Graph algorithms like D
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ5NjEzMTg1Myw0MDk4MTQ2NDJdfQ==
-->