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
#### _**@Resource**_ **annotation** :
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






<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwMzU0MzkyMDksLTE1NjI2NTQ2OTgsMT
IwNDY4NDUzOSw5Mzg0MDUwMzMsLTIwNjI1NzEzMDQsNDE5MTQ0
NjgxLDI0MTMzMzQ1NF19
-->