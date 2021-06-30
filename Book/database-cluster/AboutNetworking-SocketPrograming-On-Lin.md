# PgBouncer connect to PostgreSQL : 
- Link : [https://www.postgresql.org/docs/current/protocol-flow.html](https://www.postgresql.org/docs/current/protocol-flow.html) at the startup.

# Multi Statements In A Simple Query : 
```psql
INSERT INTO MY_TABLE VALUES(1);
SELECT 1/0;
INSERT INTO MY_TABLE VALUES(2);
```

> Gonna force roll back of the first ```INSERT```.  Cuz of the message is abandoned at the first error, the second ```INSERT``` is never attempted at all.

```
BEGIN;
INSERT INTO mytable VALUES(1);
COMMIT;
INSERT INTO mytable VALUES(2);
SELECT 1/0;
```

> Because of we ```COMMIT``` after the first ```INSERT``` so will roll back the second ```INSERT```, but not the first one.


# Message define :
```python
PSQL_FE_MESSAGES = {

'p': "Password message",

'Q': "Simple query",

'P': "Parse",

'B': "Bind",

'E': "Execute",

'D': "Describe",

'C': "Close",

'H': "Flush",

'S': "Sync",

'F': "Function call",

'd': "Copy data",

'c': "Copy completion",

'f': "Copy failure",

'X': "Termination",

}
```
# Regular package :

> Starts with an ASCII identifier
> A 32 bit message length follows 

|  char tag | int32 len  |  payload |
|---|---|---|---|---|

> The exception is the startup package, which starts with the length followed

|  int32 len| int32 protocol  |  payload |
|---|---|---|

> Cancellation

|  'E'| int32 len  |  char code |  str value | \0| char code | str value | \0 | ... | \0
|---|---|---|---|---|---|---|---|---|---|

> Handling Errors :

|  int32 len| int32 cancel code  |  int32 pid |  int32 secret|
|---|---|---|---|

# Detecting transaction status

- The ReadyForQuery message includes transaction status.

# Setup connection 

# reference :
- [https://www.pgcon.org/2014/schedule/attachments/330_postgres-for-the-wire.pdf](https://www.pgcon.org/2014/schedule/attachments/330_postgres-for-the-wire.pdf)

> This is include notice request + authenticate request.

<img src="https://i.imgur.com/vCp28Nb.png">


> Simple query  (select  query)
> In simple query mode, the format of retrieved values is always text
<img src="https://i.imgur.com/PNAIY0l.png" />


<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg0NzE3ODI2MCwtMTgxODA4NjM4OCwyMD
UyMjQwMDMyLDE3NDYzMzQzMDksMTg5MjM1NzM5NSwtMTc1Njk3
MzksLTMwNjQxMjI1Miw1ODI5NTQ4NDcsNzMwOTk4MTE2XX0=
-->