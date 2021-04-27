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
- **IoC**  được phân chia thành hai loại khác nhau, đó là:

	-   Dependency Lookup
	-   Dependency Injection

Và chúng sẽ có hai kiểu hiện thực khác nhau.

**Dependency Lookup**  sẽ tìm kiếm đối tượng phụ thuộc trong khung chứa  **IoC** và sau đó các bạn có thể dùng code để đưa đối tượng phụ thuộc vào trong đối tượng bị phụ thuộc trong khi đó  **Dependency Injection**  sẽ đưa luôn đối tượng phụ thuộc vào đối tượng bị phụ thuộc.

### Dependency Lookup

Dependency Lookup được chia thành hai kiểu khác nhau đó là:

-   Dependency Pull
-   Contextualized Dependency Lookup (CDL)
Với **Dependency Pull**, các đối tượng phụ thuộc sẽ được lấy ra từ một nơi mà các đối tượng phụ thuộc đã được đăng ký chứ không phải lấy trực tiếp từ khung chứa.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM0MjY5OTQ4NF19
-->