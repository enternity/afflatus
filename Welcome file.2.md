 How to do distributed locking
 - Trong hệ thống microservices, các service được chạy song song với nhau. Tuy nhiên trong một số trường hợp, chúng ta cần các service cần phải chạy tuần tự với nhau, do đó cần một cơ chế đảm bảo sự tuần tự giữa các service với nhau. 
 - Tác giả **[Martin Kleppmann](https://martin.kleppmann.com/ "Home")** đã giới thiệu tổng quan về khái niệm distributed locking và mục đích sử dụng nó.  Đồng thời tác giả đã phân tích sự hạn chế của một hiện thực của distributed locking là Redis. Từ đó đưa ra giải pháp nếu m
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA2MzE2MDczMiwtMjA4ODc0NjYxMiwxNT
gwMTQ3NzQ4LC0xNzIxODg4NDAwXX0=
-->