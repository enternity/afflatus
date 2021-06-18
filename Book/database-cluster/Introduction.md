# Motivation

- Với những driver như JDBC hay hibernate thì luôn sẽ có một connection pool để quản lý connection tới database vật lý (MySQL, PostgreSQL,...)
- Nếu muốn scale-up hệ thống lên. thì nếu chỉ nghĩ đơn thuần là scale các service chứa các JDBC thì nên nhớ rằng, database cũng nằm trên một server vật lý. Sẽ có giới hạn số lượng connection tới nó. 
- Ví dụ, số lượng connection tới database là 100. Một connection pool là 10 => tối đa có 10 service có thể connect tới database.

<!--stackedit_data:
eyJoaXN0b3J5IjpbNjcyNTQyNTczXX0=
-->