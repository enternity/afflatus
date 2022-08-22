# Definition
## Distributed System Models :
1. **Architectural Model**
- _Client-server model_ : 
	- The client-server is usually based on a simple request/reply protocol, implemented with send/receive primitives or using Remote Procedure Call(RPC) or Remote Method Invocation (RMI)
<img src= "https://i.imgur.com/GYRg4d5.png" >
- _Peer-to-peer_ :
	- All processes play similar role.
	- Processes interact without particular distinction between clients and servers.
	- The pattern of communication depends on the particular application.
	- A large number of data objects are shared; any individual computer holds only a small part of the application database.

<img src="https://i.imgur.com/jgu31t5.png" />

2. **Interaction Model**
- Interaction model are for handling time i.e. for process execution, message delivery, clock drifts etc.
- _**Synchronous Distributed Systems**_
	- _Main feature_ :
		- Lower and upper bounds on execution time of processes can be set.
		- Transmitted messages are received within a known bounded time.
		- Drift rates between local clocks have a known bound.
	- _Important consequences_:
		- There is a notion of global physical time
		- Only synchronous distributed systems have a predictable behavior in terms of timing. 
		- It is possible and safe to use timeouts in order to detect failures of a process or communication link
	- It is difficult and costly to implement synchronous distributed systems.
- _**Asynchronous Distributed Systems**_
	- _Main feature_: 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNzU4OTI0NzAsMTQyMDUzMzkzMSwxMj
M3MjMyOTkyXX0=
-->