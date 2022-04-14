### <center>ĐẠI HỌC QUỐC GIA THÀNH PHỐ HỒ CHÍ MINH<br/>ĐẠI HỌC KHOA HỌC TỰ NHIÊN</center>
<center><img src="https://truyenthongdaiphuc.files.wordpress.com/2015/09/dai_hoc_khoa_hoc_tu_nhien_dhqg-hcm.png" width="360" height="290"/></center>

# <center>BÁO CÁO ĐỒ ÁN MÔN HỌC : CONSENSUS</center>
## <center>CHUYÊN ĐỀ HỆ THỐNG PHÂN TÁN</center>

> ### Thành viên : 
> **1712357 : Nguyễn Huỳnh Đức**
> **1712405 : Nguyễn Trường Giang**

> Mã nguồn của nhóm : [https://github.com/tdnhduc/consensus-gRPC/tree/master](https://github.com/tdnhduc/consensus-gRPC/tree/master)

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

## Kết quả
1. **Trường hợp đầu tiên** : 2 nodes là byzantine. 
- Theo thứ tự nhận tin là node 1 và node 3.
- Log file của 2 node byzantine lần lượt được ghi nhận sau 5 phút. 

- Node 1 :
<center><img src= "https://i.imgur.com/eNHojkd.png"></center>

	- Node 3: 
<center><img src="https://i.imgur.com/jGZNJmJ.png"></center>

- Các node còn lại :
<center><img src="https://i.imgur.com/QrupovP.png"/></center>

> Từ đây ta rút ra kết luận là: kết quả 5 node trung thực kia không có gì khác nhau.

2. **Trường hợp thứ 2** : 5 nodes là byzantine.

- 5 nodes byzantine là: node 0, node 1, node 3, node 5, node 6.
- Log file của 2 node trung thực :

- Node 2:

<center><img src="https://i.imgur.com/7ln8WY2.png"/></center>

- Node 4:

<center><img src="https://i.imgur.com/i2Jduzs.png"></center>

> Có thể thấy kết quả 2 file log này là khác nhau. Sự khác nhau nằm ở sự kiện thứ 4 của Node 2. Tại sự kiện thứ 4, Node 2 đã tiến hành lưu vào file log khi Node 6 đạt đủ điều kiện gửi đúng thời điểm, đúng pid của mình và nhận được >= 4 trả lời “true”. Nhưng ở Node 4 lại không tiến hành ghi nhận điều này vào file log của mình.

## Ưu điểm :
1. Có log file, config dễ dàng.
2. Làm việc với multithreads. 
3. Chạy asynchronous.
## Hạn chế :
1. Config cứng. Số lượng node được config cứng trong file [properties](https://github.com/tdnhduc/consensus-gRPC/blob/ad603b4758c0fdab724424fcc965ef56cecd70a3/consensus/src/main/resources/application.properties#L8) nên một node mới mà không xuất hiện trong config thì cũng không được validate.

## Tham khảo :
1. https://grpc.io/docs/guides/
2. https://stackoverflow.com/
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU0NDYzNjM2M119
-->