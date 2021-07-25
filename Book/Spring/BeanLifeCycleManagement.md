# BEAN LIFE-CYCLE MANAGEMENT

> In general, two life-cycle events are particularly relevant to a bean: _**post-initialization and pre-destruction**_.

> Spring provides three mechanisms a bean can use to hook into each of these events and perform some additional processing: _**interface-based, method-based, and annotation-based mechanisms**_.


## Life cycle of Bean

<img src="https://i.imgur.com/EUE39GW.png"/>

## Implementing the `IntializingBean` Interface, `DisposableBean`

```java
class BeanInstance implements InitializingBean, DisposableBean {
	@Override
	public void afterPropertiesSet() {}
	@Override
	public void destroy() {}
}
```
## Understand Order Of Initialization Mechanisms Resolution 
1. The _**constructor**_ is called first to create bean.

2. The _**dependencies**_ are injected (setters are called).

3. Now that the beans exist and the dependencies were provided, the pre- initialization `BeanPostProcessor` infrastructure beans are consulted  to see whether they want to call anything from this bean. These are Spring-specific infrastructure beans that perform bean modifications after they are created. The `@PostConstruct` annotation is registered by `CommonAnnotationBeanPostProcessor`, so this bean will call the method found annotated with `@PostConstruct`. _**This method is executed right after the bean has been constructed and before the class is put into service**_, before the actual initialization of the bean (before `afterPropertiesSet` and `init-method`).

4.  The InitializingBean’s after `PropertiesSet` is _**executed right after**_ the dependencies are injected. The `afterPropertiesSet()` method is invoked by a BeanFactory after it has set all the bean properties supplied and has satisfied `BeanFactoryAware` and `ApplicationContextAware`.
5. The init-method attribute is executed last because this is the actual initialization method of the bean.
   
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDQ1MjUwMTIsMzA4MDkwNzY0LC01OTcyNT
U0NDgsNzAxMTgxNDY0LC0xODA5NjM4NDMyXX0=
-->