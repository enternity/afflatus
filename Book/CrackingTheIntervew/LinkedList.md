# LINKED LIST
```java
class Node {
	Node next = null;
	int value;
	public Node(int value) {
		this.value = value;
	}
	public void appendNode(Node node) {
		if (node == null) {
			throw new RunTimeException();
		} else {
			Node tmp = this.next;
			if (tmp == null) {
				this.next = node;
			} else {
				while (tmp != null) {
				
				}
			}	
		}
	}
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNjQwMDQ3ODZdfQ==
-->