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
	- High-throughput objects with writable state : obviously if state can change, but we need
2. **Prototype**
- Will return a different instance every time it is requested from the container
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjI2MjAzNTU1LC05MzkzNzIyNDZdfQ==
-->