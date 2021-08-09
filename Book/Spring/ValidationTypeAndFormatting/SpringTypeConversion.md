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
eyJoaXN0b3J5IjpbLTE2NjE1Njg2NjYsLTE4MDgzMzc4NTNdfQ
==
-->