# Dependency Injection
- Đại khái là tao cần thì gọi mày, mày cần thì gọi tao. Không phụ thuộc lẫn nhau
Ví dụ :
```java
public class People {
	private Outfit outfit;
	public People(Outfit outfit) {
		this.outfit = outfit;
	}
}
```
# Inversion Control :
- Dependency Injection thì một đối tượng sẽ không phụ thuộc vào đối tượng khác và đối tượng khác cũng vậy. Khi cần đối tượng này sẽ gọi tới đối tượng kia và ngược lại. Và mình đã hỏi các bạn, các đối tượng sẽ được tạo ra và nằm ở đâu để khi cần chúng có thể gọi lẫn nhau. Câu trả lời là chúng ta **phải có một khung chứa**, và **khung chứa đó chính là một phần của IoC**.
- **IoC** có mục đích là cung cấp một cơ chế đơn giản để chứa các đối tượng phụ thuộc và quản lý các đối tượng phụ thuộc đó thông qua chu trình sống của chúng. Một đối tượng bị phụ thuộc sẽ yêu cầu một số lượng nhất định các đối tượng phụ thuộc được quản lý bởi **IoC**. **IoC** sẽ cung cấp những cách để các đối tượng bị phụ thuộc có thể truy cập và tương tác được các đối tượng phụ thuộc
- **oC**  được phân chia thành hai loại khác nhau, đó là:

-   Dependency Lookup
-   Dependency Injection

và chúng sẽ có hai kiểu hiện thực khác nhau.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQzNTg0OTc0OF19
-->