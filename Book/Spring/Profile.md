# PROFILE
> Profiles are a core feature of the framework — **allowing us to map our beans to different profiles** — for example, _dev_, _test_, and _prod_.

```java
@Component  
@Profile("dev")  
public  class DevDatasourceConfig
```

> Profile names can also be prefixed with a NOT operator

### How to set profile?
1. **Programmatically via  _WebApplicationInitializer_  Interface** (reference [here](https://www.baeldung.com/spring-profiles#1-programmatically-via-webapplicationinitializer-interface))
```java
@Configuration  
public  class MyWebApplicationInitializer implements WebApplicationInitializer { 
	@Override  public void onStartup(ServletContext servletContext) throws ServletException { 
		servletContext.setInitParameter( "spring.profiles.active", "dev"); 
		} 
}
```
2. **Programmatically via  _ConfigurableEnvironment_** (reference: [here](https://www.baeldung.com/spring-profiles#2-programmatically-via-configurableenvironment))

```java
@Autowired  
private ConfigurableEnvironment env; 
... 
env.setActiveProfiles("someProfile");
```
3. **Context Parameter in  _web.xml_** (skip this part)
4. **JVM System Parameter**
`-Dspring.profiles.active=dev`
5. **Environment Variable**
`export spring_profiles_active=dev` in Unix environment.
6.  **Maven Profile**
7. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjE2MDUwNzI4XX0=
-->