# SOME SORT ALGORITHM

1. **SELECTION SORT** :
```java
public class SelectionSort {
	List<Integer> values = new ArrayList<>();
	for (int index = 0; index < values.size(); index ++) {
		int minValueIndex = index;
		for (int j = index + 1; j < values.size(); j++) {
		if (values.get(j) < values.get(minValueIndex)) {
			minValueIndex = j;
			}
		}
		doSwap(values, index, minValueIndex);
	}
}
```

2. **BUBBLE SORT** :

```java
public class BubbleSort {

}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk2NTc0NDI5NF19
-->