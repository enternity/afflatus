# SCOPE 
>The latest version of the Spring framework defines 6 types of scopes:
> -   singleton
> -   prototype
>-   request
>-   session
>-   application
>-   websocket

1. **Singleton Scope**
- Create singleton instance when initialize Bean.
- Choosing an Instantiation Mode :
	- _Shared object with node state_ : obviously
	- _Shared object with read-only state_ : obviously just read-only state so we do not need create too much instance.
	- High-throughput objects with writable state : obviously if state can change, but create more instance instead of synchronized is better performance
2. **Prototype**
- Will return a different instance every time it is requested from the container
- Choosing an Instantiation Mode :
	- _Objects with writable state_ : the cost of create instance is lower than try to synchronized object.
	- _Object with private state_ : we do not actually how state of object change, so we should use non-singleton.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyNDEwMDA1NzQsLTkzOTM3MjI0Nl19
-->