# RETRIEVING RECORD 
> _Main responsibility_ : Focus on **SELECT** statement.

## Retrieving All Rows and Columns from a Table
```sql
SELECT * FROM studentinfo
```
> However, when writing program code, it’s _**better to specify each column individually**_. The performance will be the same, but by being explicit you will always know what columns you are returning from the query. Likewise, such queries are easier to understand by

```sql
SELECT name, grade, gender
FROM studentinfo
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNTI0NDA1NzUsLTExNTEyMDk4MTZdfQ
==
-->