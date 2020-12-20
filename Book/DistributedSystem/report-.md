### <center>ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH<br/>ĐẠI HỌC KHOA HỌC TỰ NHIÊN</center>
<center><img src="https://truyenthongdaiphuc.files.wordpress.com/2015/09/dai_hoc_khoa_hoc_tu_nhien_dhqg-hcm.png" width="360" height="290"/></center>

# <center>BÁO CÁO ĐỒ ÁN MÔN HỌC : CONSENSUS</center>
## <center>CHUYÊN ĐỀ HỆ THỐNG PHÂN TÁN</center>

> ### Thành viên : 
> 1712357 : Nguyễn Huỳnh Đức
> 1712405 : Nguyễn Trường Giang

> Mã nguồn : [https://github.com/tdnhduc/consensus-gRPC/tree/master](https://github.com/tdnhduc/consensus-gRPC/tree/master)

## Yêu cầu chung và môi trường cài đặt.
1. Ngôn ngữ lập trình: ```Java8```
2. Quản lí dự án và các dependencies : ```Apache Maven 3.6.3```
3. Các dependencies đường liệt kê tại [đây](https://github.com/tdnhduc/consensus-gRPC/blob/master/pom.xml)
## Cách chạy demo:
- Để chạy được chương trình đầu tiên ta cần có các cấu hình cho từng node. Các cấu hình cần phải có được liệt kê ở [đây](https://github.com/tdnhduc/consensus-gRPC/blob/master/consensus/src/main/resources/application.properties)
- Lần lượt config từng node. Sau đó chạy :
```mvn clean package -DskipTests```

## Work follow
- Tại mỗi node, với các node bình thường thì sau khoảng thời gian [fixRated](https://github.com/tdnhduc/consensus-gRPC/blob/ad603b4758c0fdab724424fcc965ef56cecd70a3/consensus/src/main/resources/application.properties#L16) thì sẽ gửi cho tất cả các node.
- Sau đó các node sẽ _**validate**_ node đó có hợp lệ hay không. Sau đó tiến hành broadcast lại cho tất cả các node. Và sau đó trả về ```ack``` cho node đã gửi trước đó.
<center><img src="https://i.imgur.com/OGWsXbP.png" /></center>

## Ưu điểm :
1. Có log file, config dễ dàng.
2. Làm việc với multithreads. 
3. Chạy asynchronous.
# Hạn chế :
1. Config cứng. Số lượng node được config cứng trong file [pr]
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzkyNDY5NzE5LDU3NTYxNTM2MiwtMTU5Nz
k5OTAyMF19
-->