# INTERNATIONALIZATION WITH MESSAGE RESOURCE

> Be familiar with Internationalization(_i18n_) in java : [here](https://docs.oracle.com/javase/8/docs/technotes/guides/intl/enhancements.8.html)

> Spring provides three _MessageResource_ implementations.

1.  **ResourceBundleMessageSource**
2.  **ReloadableResourceBundleMessageSource**
3.  **StaticMessageSource**

> The _StaticMessageSource_ implementation should not be used in a production application because you can’t configure it externally, and this is generally one of the main requirements when you are adding i18n capabilities to your application.
> _ResourceBundleMessageSource_ loads messages by using a Java _ResourceBundle_. _ReloadableResource BundleMessageSource_ is essentially the same, except it supports scheduled reloading of the underlying source files.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjU1ODU1MjIwLDE2NzUyMDI3NV19
-->