# LINKED LIST
```java
class Node {
	Node next = null;
	int value;
	public Node(int value) {
		this.value = value;
	}
	public Node getNext() {
		return this.next;
	}
	public void appendNode(Node node) {
		if (node == null) {
			throw new RunTimeException();
		} else {
			Node tmp = this.next;
			while (tmp != null) {
				tmp = tmp.next;
			}
			tmp = node;
		}
	}
}
```
# Problem
1. **Remove duplicates from an unsorted linked list**
- Solution 1 : two loops.
- Solution 2 : sorted list and do remove.
- Solution 3 : use hashing.

|Link|Difficult| Completed| Source|
|:---|:---:|:---:|:---:|
|[Has Cycle](https://leetcode.com/problems/linked-list-cycle/)|Easy|:white_check_mark:|[here](https://github.com/tdnhduc/afflatus/blob/master/Book/CrackingTheIntervew/source_leetcode/2Pointers_hasCycleLinkedList_easy.py)|
|[Get intersection node](https://leetcode.com/problems/intersection-of-two-linked-lists/)|Easy|:white_check_mark:|[here](https://github.com/tdnhduc/afflatus/blob/master/Book/CrackingTheIntervew/source_leetcode/2Pointers_getIntersectionNode_easy.py)|
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NzUwODc0MDMsLTE4NTI1NzMwNzNdfQ
==
-->