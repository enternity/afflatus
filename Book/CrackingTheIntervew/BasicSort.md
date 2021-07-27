# SOME SORT ALGORITHM

1. **SELECTION SORT** :
```java
public void doSelectionSort() {
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
public void doBubbleSort() {
	List<Integer> values = new ArrayList<>();
	for (int i = 0; i < values.size() - 1; i++) {
		for (int j = 0; j < values.size() - i - 1; j++) {
			if (values.get(j) > values.get(j + 1)) {
				doSwap(values, j, j + 1);
			}
		}
	}
}
```
3. **MERGE SORT**
```java
public static void doMerge(List<Integer> values, int leftIndex, int rightIndex, int middleIndex) {  
    List<Integer> leftArrays = new ArrayList<>();  
    List<Integer> rightArrays = new ArrayList<>();  
    // copy value to left arrays  
    for (int i = leftIndex; i <= middleIndex; i++) {  
        leftArrays.add(values.get(i));  
    }  
      // copy value to right arrays  
    for (int i = middleIndex + 1; i <= rightIndex; i++) {  
        rightArrays.add(values.get(i));  
  }  
  
    int sizeLeftArrays = leftArrays.size();  
    int sizeRightArrays = rightArrays.size();  
    int indexLeft = 0;  
    int indexRight = 0;  
    int indexMergedArray = leftIndex;  
    while (indexLeft < sizeLeftArrays && indexRight < sizeRightArrays) {  
        if (leftArrays.get(indexLeft) <= rightArrays.get(indexRight)) {  
            values.set(indexMergedArray, leftArrays.get(indexLeft));  
            indexLeft++;  
        } else {  
            values.set(indexMergedArray, rightArrays.get(indexRight));  
            indexRight++;  
  }  
        indexMergedArray++;  
  }  
  
    while (indexLeft < sizeLeftArrays) {  
        values.set(indexMergedArray, leftArrays.get(indexLeft));  
  indexMergedArray++;  
  indexLeft++;  
  }  
  
    while (indexRight < sizeRightArrays) {  
        values.set(indexMergedArray, rightArrays.get(indexRight));  
  indexMergedArray++;  
  indexRight++;  
  }  
}  
  
public static void doMergeSort(List<Integer> values, int begin, int end) {  
    if (begin >= end) {  
        return;  
  }  
    int middle = begin + (end - begin) / 2;  
	doMergeSort(values, begin, middle);  
	doMergeSort(values, middle + 1, end);  
	doMerge(values, begin, end, middle);  
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAwMzc0NjM3MiwtODU5MTc3Mzg5LC0xNT
MzOTc2OTg0XX0=
-->