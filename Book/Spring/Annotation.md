# ANNOTATION
1.  **Configuration Annotations**

|  Annotation |  Definition |   
|---|---|
|  _@Configuration_ |   _**configuration class**_ and method with annotations _@Bean_ that are called directly by the Spring IoC container to instantiate the beans. The bean name will be the same as the name of the method used to create it |
| _@ComponentScan_  |  we can tell Spring where to search for these annotated classes as not all of them must become beans in this particular run. **Only the location of the configuration class matters, as component scanning starts from its package by default** | 

2. **Component Annotations**

| Annotation  | Definition  | 
|---|---|
|_@Component_|is a _**generic**_ stereotype for any Spring-managed component.|
|_@Service_|annotates classes at the _**service layer**_.|
|_@Repository_|annotates classes at the _**persistence layer**_, which will act as a database repository.|
| _@ComponentScan_  |  we can tell Spring where to search for these annotated classes as not all of them must become beans in this particular run. **Only the location of the configuration class matters, as component scanning starts from its package by default** | 

3. **Injection Annotations**





<!--stackedit_data:
eyJoaXN0b3J5IjpbNTQ1NDI2NDcwLC0xNTYyNjU0Njk4LDEyMD
Q2ODQ1MzksOTM4NDA1MDMzLC0yMDYyNTcxMzA0LDQxOTE0NDY4
MSwyNDEzMzM0NTRdfQ==
-->