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
	List<Integer> values = new ArrayList<>();
	for (int i = 0; i < values.size() - 1; i++) {
		for (int j = i + 1; j < values.size() - i - 1; j++) {
			if (values.get(j) > values.get(j + 1)) {
				doSwap(values, j, j + 1);
			}
		}
	}
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MTgwMjY0MjJdfQ==
-->