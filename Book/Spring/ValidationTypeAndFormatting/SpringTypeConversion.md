> Official reference : https://docs.spring.io/spring-framework/docs/3.2.x/spring-framework-reference/html/validation.html#core-convert
# SPRING TYPE CONVERSION
## Implementing a Custom Converter
```java
class StringToDateTim implements Converter<String, DateTime> {  
    private static final String DEFAULT_DATE_PATTERN = "yyyy-mm-dd";  
	private DateTimeFormatter dateTimeFormatter;  
  
	public StringToDateTim() {  
        this.dateTimeFormatter = DateTimeFormat.forPattern(DEFAULT_DATE_PATTERN);  
	}  
  
    @Override  
    public DateTime convert(String s) {  
        return this.dateTimeFormatter.parseDateTime(s);  
    }  
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTc5NTYzMTA0LC0xNjYxNTY4NjY2LC0xOD
A4MzM3ODUzXX0=
-->