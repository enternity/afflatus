# Resource Profiles
> Depending on whether you specify the requests, the limits, or both, the platform offers a different kind of Quality of Service (QoS).

1. **Best Effort**
	- Pods that does not have any requests and limits set for its containers. Such a Pod is considered as the lowest priority and is most likely killed first when the node where the Pod is placed runs out of impressible resources (CPU, memory).
2. **Burstable** 
	- Pod that has requests and limits defined, buy they are not equal (and limit is larger than requests as expected). pods that willing to consume more resources up to its limit when available. These pod are likely to be killed if no Best-Effort Pods remain in case the node is under incompressible.
3. **Guaranteed**
	- Pod that has an equal amount of request a
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4MjAwMTk1MjAsLTE5NjAyNzkyNzNdfQ
==
-->