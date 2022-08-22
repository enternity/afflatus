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
- _**Asynchronous Distributed Systems (ADS)**_
	- _Main feature_:
		- No bound on process execution time.
		- No bound on message transmission delays.
		- No bounds on drift rates between local clocks.
	- 
	- _Important consequences_:
		- In an asynchronous distributed system there is no global physical time. Reasoning can be only in terms of logical time.
		- ADS are unpredictable in terms of timing.
		- No timeouts can be used
		- In practice timeouts are used with asynchronous systems for failure detection.
		- However, additional measures have to be applied in order to avoid duplicated messages, duplicated execution of operations, etc.
3. **Fault Models**:
- Can occur both in processes and communication channels.
- Needed in order to build systems with predictable behavior in case of faults.
- Such a system will function according to the predictions, only as long as the real faults behave as defined by the "fault model"

## Properties
## Safety
- _"There are no bad reachable configurations"_.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwOTkxMzYzNzAsMTQyMDUzMzkzMSwxMj
M3MjMyOTkyXX0=
-->