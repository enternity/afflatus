# PROFILE
> Profiles are a core feature of the framework — **allowing us to map our beans to different profiles** — for example, _dev_, _test_, and _prod_.

```java
@Component  
@Profile("dev")  
public  class DevDatasourceConfig
```

> Profile names can also be prefixed with a NOT operator

### How to set profile?
1. **Programmatically via  _WebApplicationInitializer_  Interface** (refer [here](https://www.baeldung.com/spring-profiles#1-programmatically-via-webapplicationinitializer-interface))
```java
@Configuration  
public  class MyWebApplicationInitializer implements WebApplicationInitializer { 
	@Override  public void onStartup(ServletContext servletContext) throws ServletException { 
		servletContext.setInitParameter( "spring.profiles.active", "dev"); 
		} 
}
```
2. **Programmatically via  _ConfigurableEnvironment_** (reference: [here](https://www.baeldung.com/spring-profiles#2-programmatically-via-configurableenvironment)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NjMzNDgwNjJdfQ==
-->