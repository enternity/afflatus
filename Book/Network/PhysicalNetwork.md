# Mô hình OSI
## Hardware Layer :
1. **Physical Layer**
- It is responsible for the actual physical connection between devices. It is responsible for transmitting individual bits from one node to the next. When receiving data, this layer will get the signal received and convert it into 0s and 1s and send them to the Data Link layer, which is put the frame back together.
- The functions of the physical layer are as follows:
	- _Bit synchronization_ : the physical layer provides the synchronization of the bits by providing a clock. (???)
	- _Bit rate control_ : defines the transmission rate. example: the number of bits sent per second.
	- _Physical topologies_ :  specifices the way in which the different, devices/nodes are arranged in a network. i.e bus, star, or mesh topology.
	- _Transmission mode_ : defines the way in which the data flows between the two connected devices. Transmission modes possible are : `Simplex, Half-Duplex, Full-Duplex.` [Transmission mode](https://www.geeksforgeeks.org/difference-between-simplex-half-duplex-and-full-duplex-transmission-modes/#:~:text=Simplex%20mode%20is%20a%20uni,two%2Dway%20directional%20communication%20simultaneously.)
2. **Data Link Layer**
- It is responsible for the `node-to-node` delivery of the message. The main function of this layer is to make sure data transfer is `error-free` from one node to another, over the physical layer. When a package arrives in a network, it is the responsibility of DDL to tran


# Different TCP  and UDP protocol
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMxNjY1Mjc3LDE3MDcyNTU0MTksLTEzMT
U3MTgzNjAsLTE0MDk4NjM2OTldfQ==
-->