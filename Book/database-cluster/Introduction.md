# Motivation

- Với những driver như JDBC hay hibernate thì luôn sẽ có một connection pool để quản lý connection tới database vật lý (MySQL, PostgreSQL,...)
- Nếu muốn scale-up hệ thống lên. thì nếu chỉ nghĩ đơn thuần là scale các service chứa các JDBC thì nên nhớ rằng, database cũng nằm trên một server vật lý. Sẽ có giới hạn số lượng connectio
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ2NTcwODg1N119
-->