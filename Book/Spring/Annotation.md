# ANNOTATION
##  **Configuration Annotations**

|  Annotation |  Definition |   
|---|---|
|  _@Configuration_ |   _**configuration class**_ and method with annotations _@Bean_ that are called directly by the Spring IoC container to instantiate the beans. The bean name will be the same as the name of the method used to create it |
| _@ComponentScan_  |  we can tell Spring where to search for these annotated classes as not all of them must become beans in this particular run. **Only the location of the configuration class matters, as component scanning starts from its package by default** | 

## **Component Annotations**

| Annotation  | Definition  | 
|---|---|
|_@Component_|is a _**generic**_ stereotype for any Spring-managed component.|
|_@Service_|annotates classes at the _**service layer**_.|
|_@Repository_|annotates classes at the _**persistence layer**_, which will act as a database repository.|
| _@ComponentScan_  |  we can tell Spring where to search for these annotated classes as not all of them must become beans in this particular run. **Only the location of the configuration class matters, as component scanning starts from its package by default** | 

## **Injection Annotations**
#### _**@Resource**_ **annotation** : (Jakarta EE)
- This annotation has the following execution paths, listed by precedence:
	- Match by _**name**_
	- Match by _**type**_
	- Match by _**qualifier**_

1. _**Field Injection**_ :
- _Match by name_
	- This configuration will resolve dependencies using the **match-by-name** execution path. We must define the bean _namedFile_ in the _ApplicationContext_ application context.
> Example
```java
@Resource("student-A7")
private StudentInfo studentInfo;
```
- _Match by Type_ 

> Example 
```java
@Resource  
private File defaultFile;
```

- _Match by qualifier_ 

Example from [baeldung.com](https://www.baeldung.com/spring-annotations-resource-inject-autowire)
```java
@Configuration  public  class 
ApplicationContextTestResourceQualifier { 
@Bean(name="defaultFile")  public File defaultFile() { 
    File defaultFile = new File("defaultFile.txt"); 
    return defaultFile; 
} 
@Bean(name="namedFile")  public File namedFile() { 
        File namedFile = new File("namedFile.txt"); 
        return namedFile; 
    } 
}
```

```java
@Resource  
@Qualifier("defaultFile")  
private File dependency1; 

@Resource 
@Qualifier("namedFile")  
private File dependency2;
```

2. _**Setter Injection**_
- Just like _Field Injection_ but inject via setter function
> Example
```java
 protected void setDefaultFile(File defaultFile) {
    this.defaultFile = defaultFile; 
 }
```
#### _**@Inject**_  Annotation : (javax)
- This annotation has the following execution paths, listed by precedence:
	- Match by _**type**_
	- Match by _**qualifier**_
	- Match by _**name**_

> Do the same thing like _@Resource_ but the precedence is different
#### _**@Autowired**_ Annotation : (Spring Framework)
- Do the same thing like _@Resource, @Inject_ but the precedence if different 
- Listed in order of precedence:
	- Match by Type
	- Match by Qualifier
	- Match by Name






<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0ODg2MTgxNjYsLTcxNDY5MTI4NywtMT
AzNTQzOTIwOSwtMTU2MjY1NDY5OCwxMjA0Njg0NTM5LDkzODQw
NTAzMywtMjA2MjU3MTMwNCw0MTkxNDQ2ODEsMjQxMzMzNDU0XX
0=
-->