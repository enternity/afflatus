1. ```__init__(self)```  : được gọi khi instance được tạo.
2. ```__del__(self)``` : gọi khi instance phải bị huyr. Hay gọi là *destructor*. Nếu lớp cha có method ```__del__()``` thì lớp con phải định nghĩa rõ ràng để chắc chắn xóa đúng.
> continue ... Vì hơi khó hiểu.

3. ```__repr__(self)``` : built-in function và tạo ra 1 chuỗi để mô tả về đối tượng. Nó *"official"* cho các đối tương thuộc cùng một lớp

4. ```__str__(self)``` :  cũng như ```__repr__()``` tuy nhiên nó không có *"offical"*. Hiểu đơn giản hơn nó định nghĩa cho từng đối tượng trong cùng 1 lớp.
5. ```___cmp__(self,other)``` : So sánh tất nhiên rồi. Trả về số âm nếu ```self < other```. Số dương nếu ```self > other```. 0 nếu ```self == other```. Nếu không định nghĩa ```__cmp__()``` thì sẽ so sánh *object identity*(id - aka địa chỉ)  của đối tượng.
6. ```__hash__(self)``` : 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI5NzE2MTMwMSwtOTU0NjY0NjIyXX0=
-->