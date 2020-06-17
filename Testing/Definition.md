# Unit test
1. **Khái niệm** :
	- Là một thành phần PM nhỏ nhất mà ta có thể kiểm tra được như các *Function, Procedure, Class, Method*.
	- Mỗi Unit Test(UT) sẽ gửi đi một thông điệp và kiểm tra câu trả lời nhận được đúng hay không, bao gồm :
		- Kết quả trả về mong muốn.
		- Exception
2. **Các khái niệm thường thấy khi làm Unit Test**:
	- ***Assertion*** : mô tả các công việc kiểm tra cần tiến hành. Ví dụ: ```AreEqual(), IsTrue(), IsNotNul(),etc``` Mỗi UT gồm nhiều assertion kiểm tra dữ liệu đầu ra, tính chính xác của các lỗi ngoại lệ ra và các vấn đề phức tạp khác như : Sự tồn tại của một đối tượng - Điều kiện biên - Thứ tự thực hiện các luồng dữ liệu.
	- ***Test Point*** : chứa đơn giản một assertion nhằm khẳng định tính đúng đắn của một chi tiết mã nào đó. 
	- ***Test Case*** : tập hợp các test point kiểm tra một chức năng cụ thể.
	- ***Test Suite***: tập hợp các test case định nghĩa cho từng module hoặc hệ thống con.
	- ***Regression Testing*** (*Automated Testing*) : Phương pháp kiểm nghiệm tự động . Kết hợp Regression Testing và Unit testing đảm bảo các đoạn mã mới sẽ tốt.
	- ***Production Code***: mã nguồn của ứng dụng chuyển giao cho khách hàng.
	- ***Unit Testing Code***: Không chuyển giao cho khác hàng.
3. **Vòng đời của Unit Test**:
	- ***Trạng thái***:
		- Fail.
		- Ignore.
		- Pass
	- 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ2MjA4NjE1NV19
-->