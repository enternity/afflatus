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
3. 1.  Now that the beans exist and the dependencies were provided, the pre- initialization BeanPostProcessor infrastructure beans are consulted  
    to see whether they want to call anything from this bean. These are Spring-specific infrastructure beans that perform bean modifications after they are created. The @PostConstruct annotation is registered by

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcwODgzNjE5NCwzMDgwOTA3NjQsLTU5Nz
I1NTQ0OCw3MDExODE0NjQsLTE4MDk2Mzg0MzJdfQ==
-->