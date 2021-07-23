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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NTI1NzMwNzNdfQ==
-->