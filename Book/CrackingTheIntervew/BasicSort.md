
# Compare Sort Methods :
| Names        | Average           |  Memory |Note|
|:------------- |:-------------:| -----:|:-------------|
|    **Quick sort**   | $n\log{n}$ | $\log{n}$ ||
| **Merge Sort**| $n\log{n}$| $n$|Best-Average-Worst is the same|
| **Heap Sort** |$n\log{n}$|$1$||
|**Insertion Sort**|$n^2$|1|Worst-case when array is inverse, best case O(n)|
|**Selection Sort**|$n^2$|1||
|**Bubble Sort**|$n^2$|1|Few code|
|**Tree Sort**|$n\log{n}$|$n$|Worst-case is $n\log{n}$ when it's balanced tree|
# Code 
1. **Quick sort**
> Idea: It picks an element as a pivot and partitions the given array around the picked pivot. There are many different versions of quickSort that pick pivot in different ways.
```python
def partition(arr, low, high):
	i = low - 1 # index of smaller element
	pivot = arr[high]
	for j in range(low, high):
	if arr[j] <= pivot:
		i += 1
		arr[i],arr[j] = arr[j],arr[i]
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i+1

def quickSort(arr, low, high):
	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi - 1)
		quickSort(arr, pi + 1, high)
# example : quickSort(arr, 0, len(arr) - 1)
```
2. **Merge Sort**:
> Idea: So, in this algorithm, the array is **initially divided into two equal** halves and then they are combined in a sorted manner. We can think of it as a recursive algorithm that continuously splits the array in half until it cannot be further divided. This means that if the array becomes empty or has only one element left, the dividing will stop, i.e. it is the base case to stop the recursion. If the array has multiple elements, we split the array into halves and recursively invoke the merge sort on each of the halves. Finally, when both the halves are sorted, the merge operation is applied. Merge operation is the process of taking two smaller sorted arrays and combining them to eventually make a larger one.
```python
def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m
	# Create temp arrays
	L = [0] * n1
	R = [0] * n2 
	# Copy data to temp arrays
	for i in range(n1):
		L[i] = arr[l+i]
	for j in range(0, n2):
		R[j] = arr[m + 1 + j]
	# Merge back into array
	i = 0
	j = 0
	k = l
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1
	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1
def mergeSort(arr, l, r):
	if l < r:
		m = (l + (r - 1)) // 2
		mergeSort(arr, l, m)
		mergeSort(arr, m + 1, r)
		merge(arr, l, m, r)
# example : mergeSort(arr, 0, len(arr) - 1)
```
3. **Heap Sort**
```python
def heapify(arr, n, i):
	largest = i
	l = 2 * i + 1
	r = 2 * i + 2
	if l < n and arr[i] < arr[l]:
		largest = l
	if r < n and arr[largest] < arr[r]:
		largest = r
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest)
def heapSort(arr):
	n = len(arr)
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)
	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)
# source : https://www.geeksforgeeks.org/python-program-for-heap-sort/
```
4. **Insertion Sort**:
> continue ...
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNzE5NTg2OTUsLTc5NzgyNjM2NCwtOD
U5MTc3Mzg5LC0xNTMzOTc2OTg0XX0=
-->