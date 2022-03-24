 How to do distributed locking
 - Trong hệ thống microservices, các service được chạy song song với nhau. Tuy nhiên trong một số trường hợp đặc biệt, chúng ta cần các service phải chạy tuần tự, do đó cần một cơ chế đảm bảo sự tuần tự giữa các service với nhau. 
 - Tác giả **[Martin Kleppmann](https://martin.kleppmann.com/ "Home")** đã giới thiệu tổng quan về khái niệm distributed locking và mục đích sử dụng nó.  Bên cạnh đó tác giả đã phân tích các vấn đề hạn chế của một hiện thực distributed locking là Redis Lock.
 - Từ đó đưa ra các lưu ý khi sử dụng distributed locking:
	 - Nếu sử dụng trong việc tối ưu hoá thời gian thực hiện có thể dùng Redis single node.
	 - Nếu sử dụng trong việc tính chính xác của hệ thống có thể dùng một hệ thống có thuật toán đồng thuận như ZooKeeper. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjU2OTA2MjcsMjI0NzkyMTkzLC0xNDA3Nz
gxMTEyLC0yMDg4NzQ2NjEyLDE1ODAxNDc3NDgsLTE3MjE4ODg0
MDBdfQ==
-->