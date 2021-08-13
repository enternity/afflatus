|Article| Link|
|:--|:--|
|**Must Read** Dynamic Programing Pattern|https://patterns.eecs.berkeley.edu/?page_id=416|
|Overlapping subproblems property in DP|https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/|
|Optimal substructure property|https://www.geeksforgeeks.org/optimal-substructure-property-in-dynamic-programming-dp-2/|


# Long common sequence
> With string $a = (a_0,a_1, \ldots, a_x)$ and $b= (b_0,b_1, \ldots, b_x)$

$lcs(a_i, b_j) =  
  \begin{cases}
 0 & \quad  \text{if } i \text{ or} j \text{ equal }0\\
  lcs(a_{i-1}, b_{j-1}) & \qua \text{if } 
  \end{cases}$

# Leet code complete problem tag [Dynamic Programing](https://leetcode.com/problemset/all/?page=2&topicSlugs=dynamic-programming)

|Link|Difficult| Completed|
|:---|:---|:---:|
|[Is subsequence](https://leetcode.com/problems/is-subsequence/)|Easy|:white_check_mark:|
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg0NTY3MTQyLC0yMDk5NDMyMjgsLTE0Nz
Q4MjU3NiwxMzIwMzM0NDA2LDE0MzEwMjU3NTNdfQ==
-->