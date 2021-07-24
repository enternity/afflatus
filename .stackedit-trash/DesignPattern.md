> Bài viết này được phiên dịch và hiểu theo người dịch. Nên đôi khi có nhiều lúc hiểu sai, hoặc không đủ. Mong góp ý
> Dựa theo cuốn : **"Design Patterns : Elements of Reusable Object-Oriented Software"**

> prototype for this article
> #.#.#.# : cho các lời khuyên
> Màu $\color{blue}blue$ : cho nên làm
> Màu $\color{red}red$ : cho nên tránh
> 

# Design patterns là cái chi chi ?
[Christopher Alexander](https://en.wikipedia.org/wiki/Christopher_Alexander)  đã nói rằng : _"Mỗi pattern diễn đạt vấn đề xảy ra lặp đi lặp quanh chúng ta và sau đó diễn đạt ý chính để giải quyết vấn đề ấy theo cách bạn có thể dùng cách giải quyết ấy cho hàng triệu lần khác mà không làm lại lần hai."_

Về cơ bản **Design Pattern** có 4 thứ thiết yếu :

1. **Pattern name** là cái dùng để ta diễn tả vấn đề về thiết kế. Nó là giải pháp kết quả trong một vài từ (eg : _singleton, factory_). Nói chung nó là một cái convention để cho ai đọc cũng hiểu và áp dụng.
2. Vấn đề được diễn đạt khi chung ta áp dụng một pattern nào đó. Nó giải thích vấn đề và bối cảnh hiện tại của nó. Nó có thể diễn đạt một thiết kế để giải quyết vấn đề đặc biệt ( có thể hiểu là làm sao để diễn đạt một thuật toán như một object). Nó cũng có thể diễn tả một class hoặc một object structures là chúng có nguy cơ là một trường hợp không linh động (nguyên văn : It might describe class or object structures that are symptomatic of an inflexible design. Và vẫn không hiểu :smile:). Đôi khi vấn đề sẽ được bảo gồm một danh sách các điều kiện rằng phải gặp trước khi nó hợp lý để áp dụng một pattern.
3. Giải pháp được diễn đạt thành các yếu tố tạo nên thiết kế như : mối quan hệ, trách nhiệm và sự hợp tác. Giải pháp không phải là nghiệm cụ thể của bài toán. Mà nó nên được hiểu là các bước làm để giải bài toán đấy :wink: :wink:
4. Áp dụng một design pattern nào đó thì nên nghĩ tới *trade-offs*(chi phí và kết qủa). 

> Túm váy lại : _"Design Patterns trong sách này là diễn tả cách thức giao thiếp giữa các objects và classes và tùy chỉnh lại để giải quyết vấn đề thiết kế chung trong một ngữ cảnh cụ thể :wink: :wink:"_

# Class verus Interface Inheritant
1. Object's class xác định object được thể hiện như thế nào. Class xác định trạng thái bên trong của đối tượng và thể hiện các hoạt động của chính nó. 
2. Ngược lại Object's type chỉ đề cập tới một list các yêu cầu mà nó có thể handle. Một object có thể có nhiều kiểu, object của nhiều classes có thể có cùng một loại.
> Dừng tại trang 32
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk0NzM5ODEzOF19
-->