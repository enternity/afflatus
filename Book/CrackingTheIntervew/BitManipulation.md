# BIT MANIPULATION

## Bitwise Operators
| Operator  |  Syntax | Example| 
|:---|:---:|:---|
|  **OR** | `|`  |   `1101 | 0110 = 1111` (13 | 6 = 15)
|  **AND** | `&`  |  `1101 & 0110 = 0100` (13 & 6 = 4)|  
| **XOR**  | `^`  |  `1101 ^ 0110 = 1011` (13 ^ 6 = 11)|
|**NOT**| `~`| `~1101 = 0010` (~13 = 2)|

 
## Bitwise Shift Operators
|Operator| Syntax| Example|Describe|
|:---|:---:|:---|:---|
|Signed right shift|`>>`|1. `4 >> 2 = 2`  <br/> 2. `-2 >> 1` (2)|1. `0100 -> 0010`  (`4 /= 2`) <br/> 2. `1010 -> 1001` <br/> _**Keep bit signed**_|
|Unsigned right shift|`>>>`| `-4 >> 2`| `1100 -> 0011` <br/> _**Ignore big signed**_|
|Left shift|`<<`| `2 << 2`| `0010 -> 1000` ()|
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjYxMjg2MywtMzg2NDA3MDQ4LC05MDMyNj
gwMzBdfQ==
-->