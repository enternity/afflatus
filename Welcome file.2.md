 How to do distributed locking
 - Trong hệ thống microservices, các service được chạy song song với nhau. Tuy nhiên trong một số trường hợp đặc, chúng ta cần các service cần phải chạy tuần tự với nhau, do đó cần một cơ chế đảm bảo sự tuần tự giữa các service với nhau. 
 - Tác giả **[Martin Kleppmann](https://martin.kleppmann.com/ "Home")** đã giới thiệu tổng quan về khái niệm distributed locking và mục đích sử dụng nó.  Bên canh đó tác giả đã phân tích các vấn đề hạn chế của một hiện thực của distributed locking là Redis Lock.
 - Trong bài viết tác giả đưa ra các lưu ý khi sử dụng distributed locking:
	 - Nếu sử dụng trong việc tối ưu hoá thời gian thực hiện có thể dùng Redis single node.
	 - Nếu cần 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMzMzOTIxNiwtMTQwNzc4MTExMiwtMj
A4ODc0NjYxMiwxNTgwMTQ3NzQ4LC0xNzIxODg4NDAwXX0=
-->