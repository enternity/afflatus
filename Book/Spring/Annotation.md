# ANNOTATION
1.  **Configuration Annotations**

|   |   |   |   |   |
|---|---|---|---|---|
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
## Component 
-   _@Component_  is a _**generic**_ stereotype for any Spring-managed component.
-   _@Service_  annotates classes at the _**service layer**_.
-   _@Repository_  annotates classes at the _**persistence layer**_, which will act as a database repository.
- _@Configuration_ is _**configuration class**_ and method with annotations _@Bean_ that are called directly by the Spring IoC container to instantiate the beans. The bean name will be the same as the name of the method used to create it
- _@ComponentScan_ : we can tell Spring where to search for these annotated classes as not all of them must become beans in this particular run. **Only the location of the configuration class matters, as component scanning starts from its package by default**
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTQ5NTQ5Mzg4LDkzODQwNTAzMywtMjA2Mj
U3MTMwNCw0MTkxNDQ2ODEsMjQxMzMzNDU0XX0=
-->