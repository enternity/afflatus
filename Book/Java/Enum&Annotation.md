# ENUM
#### Advice 1 : Use enum instead of int constants
1. Enum is _**constant variables**_ that mean we need to recompile the program if enum variable have been changed. The enum make program don't run incorrect state which we want.
2. Enum constants make readable string output.
3. Provide compile-time type safety.
4. Enum is singleton.
5. **To associate data with enum constants, declare instance fields and write a constructor that takes the data and stores it in the fields.**
6. Some behaviors associated with enum constants may need to be used only from within the class or package in which the enum is defined. Such behaviors are best implemented as private or package-private methods.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMDY5MDM1ODldfQ==
-->