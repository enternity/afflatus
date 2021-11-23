# Arrays and String
## Hash Tables 
In simple implementation, we do the following :
1. First, compute the key's hash code. Note that two different keys could have the same hash code.
2. Map the hash code to an index in the array.
3. At this index, there is a linked list of key and values. Store the key value in this index. We _**must**_ use _linked list_ because collisions.
> We can implement the hash table with a balanced binary search tree. And give us `O(logN)` lookup time.
## ArrayList & Resizable Array
To resizable array approach :
- First capacity increase : 1 element copy
- Second capacity increase : 2 element copy
- Third capacity increase : 4 element copy
....
- Previous capacity increase : $n/16$ element copy
- Previous capacity increase : $n/8$ element copy
- Previous capacity increase : $n/4$ element copy
- Final capacity increase : $n/2$ element copy
> Roughly : $\frac{N}{2} + \frac{N}{4} + \cdots + 2 + 1 \simeq 1$
> Inserting N elements takes $O(N)$ work total.
## StringBuilder

## Interview Questions 
1. Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures? (if string is include only alphabet character)
Hint : use one variable 32 bit (int) to check.
2. Given two strings, write a method to decide if one is a permutation of the other.
3. Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
	EXAMPLE
	Input: "Mr John Smith ", 13
	 Output: "Mr%20John%20Smith" 
4. Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­ drome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

	EXAMPLE

	Input: Tact Coa  
	Output: True (permutations: "taco cat", "atco eta", etc.)
5. One Away: There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.
	EXAMPLE

	pale, ple -> true pales, pale -> true pale, bale -> true 		pale, bake -> false
6. String Compression: Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return

the original string. You can assume the string has only uppercase and lowercase letters (a - z).
7. Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
8. Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
9. String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one call to isSubstring (e.g.,"waterbottle" is a rotation of"erbottlewat").


|Problem| Algorithm|Solved|
|:---|:---|:---| 
|Finding element with the appearance more than $\frac{N}{2}$ time|https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/||
|Prime number|https://www.geeksforgeeks.org/sieve-of-eratosthenes/||

# Leet code complete problem tag [Array](https://leetcode.com/problemset/all/?page=3&topicSlugs=array)

|Link|Difficult| Completed| Source|
|:---|:---:|:---:|:---:|
|[Remove duplicate from sort array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)|Easy|:white_check_mark:|
|[Is anagram](https://leetcode.com/problems/valid-anagram/submissions/)|Easy|:white_check_mark:|[here](https://github.com/tdnhduc/afflatus/blob/master/Book/CrackingTheIntervew/source_leetcode/String_IsAnagram_easy.py)|
|[Is palindrome](https://leetcode.com/problems/valid-palindrome/)|Easy|:white_check_mark:| |[here](https://github.com/tdnhduc/afflatus/blob/master/Book/CrackingTheIntervew/source_leetcode/2Pointers_isPalindrome_easy.py)|
|[intersection-of-two-arrays](https://leetcode.com/problems/intersection-of-two-arrays/)|Easy|:white_check_mark:|[here](https://github.com/tdnhduc/afflatus/commit/78b7acacd2fa3a35c1a9fc3c193e3c06635beb00)
|[sum_range](https://leetcode.com/problems/summary-ranges/)|Easy|:white_check_mark:|[here](https://github.com/tdnhduc/afflatus/commit/ee5bed65af45f340675316022b9521a46ec1af49)|
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjMzMTYxNzc4LDE2MTUzNTExMDksODczMz
E4NzIzLC0yODMwNjA3NzQsMTg4NTgyOTc3NiwtNDczNjg1NTAw
LDU1MTQ4OTA2NywtNjIzNzE4NzU1LDEzMjg1NzIyOTEsMTQxOT
IxNTkzMiw1MDUxNzY0MiwtMTUxOTk1NzAwOCwtMjYyNjY3NzQ0
LC0xMzA0Mjk4OTczLC0xOTIxNTg1NTMsLTMyODA4NDM1OV19
-->