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

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU5NzI1NTQ0OCw3MDExODE0NjQsLTE4MD
k2Mzg0MzJdfQ==
-->