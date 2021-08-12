> https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/validation.html#validator
# SPRING VALIDATION
> We should use interface 
```java
package org.springframework.validation;  
  
public interface Validator {  
    boolean supports(Class<?> var1);  
  
 void validate(Object var1, Errors var2);  
}
```
> And class `ValidationUtils` in `package org.springframework.validation;` to validate field.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAzNTUzNDA5NCwxNzY4ODc5NDgxXX0=
-->