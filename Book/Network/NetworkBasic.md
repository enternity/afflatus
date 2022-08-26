# Mô hình OSI
1. **Physical Layer**
- It is responsible for the actual physical connection between devices. It is responsible for transmitting individual bits from one node to the next. When receiving data, this layer will get the signal received and convert it into 0s and 1s and send them to the Data Link layer, which is put the frame back together.
- The functions of the physical layer are as follows:
	- _Bit synchronization_ : the physical layer provides the synchronization of the bits by providing a clock. (???)
	- _Bit rate control_ : defines the transmission rate. example: the number of bits sent per second.
	- _Physical topologies_ :  specifices the way in which the different, devices/nodes are arranged in a network. i.e bus, star, or mesh topology.
	- _Transmission mode_ : defines the way in which the data flows between the two connected devices. Transmission modes possible are : `Simplex, Half-Duplex, Full-Duplex.` [Transmission mode](https://www.geeksforgeeks.org/difference-between-simplex-half-duplex-and-full-duplex-transmission-modes/#:~:text=Simplex%20mode%20is%20a%20uni,two%2Dway%20directional%20communication%20simultaneously.)
2. **Data Link Layer**
- It is responsible for the `node-to-node` delivery of the message. The main function of this layer is to make sure data transfer is `error-free` from one node to another, over the physical layer. When a package arrives in a network, it is the responsibility of DDL to transmit it to the Host using its MAC address.
- Data Link Layer is divided into two sublayers:
	- Logical Link Control (LLC)
	- Media Access Control (MAC)
- DDL encapsulates Sender and Receiver's MAC address in the header. 
- The functions of the Data Link Layer are:
	- _Framing_ : provides a way for a sender to transmit a set of bits that are meaningful to the receiver.
	- _Physical addressing_ : After creating frames, DDL adds physical address (MAC) of the sender and/or receiver in the header of each frame.
	- _Error control_ : provides the mechanism of error control in which it detects and retransmits damaged or lost frames.
	- _Flow control_ : coordinates the amount of data that can be sent before receiving ack.
	- _Access Control_ : When a single communication channel is shared by multiple devices, the MAC sub-layer of the data link layer helps to determine which device has control over the channel at a given time.
3. **Network Layer**
- The network layer works for the transmission of data from one host to the other located in different networks. Takes care of package routing. The sender & receiver's IP addresses are placed in the header by the network layer.
- The functions of the Network layer are:
	- _Routing_ : Determine which route is suitable from source to destination.
	- _Logical Addressing_ : Identify each device on internet work uniquely, the network layer defines an addressing scheme.

4. **Transport Layer**
- Provides services to the application layer and takes services from the network layer. It is responsible for the End to End delivery of the complete message. The transport layer also provides the acknowledgment of the successful data transmission and re-transmits the data if an error is found.
- _**At sender's side**_ : formatted data from the upper layers, performs **Segmentation**, also  implement **Flow & Error control** to ensure proper data transmission. It also adds Source and Destination port numbers in its header and forwards the segmented data to the Network Layer.
- - _**AT receiver's side**_: Transport Layer reads the port number from its header and forwards the Data which it has received to the respective application. It also performs sequencing and reassembling of the segmented data.
- The functions of the transport layer are as follows:
	- _**Segmentation and Reassembly**_: accepts the message from the session layer, and breaks the message into smaller units. Each of the segments produced has a header associated with it. At the destination station reassembles the message.
	- _**Service Point Addressing**_ : Make sure the message is delivered to the correct process.
	- The services provided by the transport layer:
		- **Connection-Oriented Service**
			- Connection establishment.
			- Data transfer.
			- Termination / Disconnection.
			> The receiving device sends an acknowledgment, back to the source after packet or group packets is received. More reliable & secure.
		- **Connectionless Service** : it is a one-phase process and includes Data Transfer. The receiver does not acknowledge receipt of a packet. Much faster communication between devices.
5. **Session Layer** :
	- Session establishment, maintenance, and termination.
	- Synchronization : Add checkpoints which are considered synchronization points into data. helps to identify the error so that data is re-synchronized properly.
	- Dialog Controller : Allows two systems to start communication with each other in half-duplex or full-duplex.
6. **Presentation Layer**
- The data from the application layer is extracted here and manipulated as per the required format the required format to transmit over the network.
	- Translation: I.e ASCII, EBCDIC.
	- Encryption / Decryption : data encryption translates the data into another form or code.
	- Compression : reduces the number of bits that need to be transmitted on the network.
7. **Application Layer**
- Produced data.

> **OSI model in a nutshell**
<img src= "https://media.geeksforgeeks.org/wp-content/uploads/20220511230638/OSImodelakhilabhilash01.png"/>
#  TCP in a nutshell :
## Features of TCP/IP 
1. **Segment Numbering System**
- TCP keeps track of the segments being transmitted or being received by assigning numbers ti each and every single one of them.
- A specific `ByteNumber` is assigned to data bytes that are to be transferred while segments are assigned `sequence number`.
- `Acknowledgment Numbers` are assigned to received segments.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/tcp1-2.png"/>

> In this example we see that A sends acknowledgement number1001, which means that it has received data bytes till byte number 1000 and expects to receive 1001 next, hence B next sends data bytes starting from 1001. Similarly, since B has received data bytes till byte number 13001 after the first data transfer from A to B, therefore B sends acknowledgement number 13002, the byte number that it expects to receive from A next.

2. **Flow Control** :
- Limit s the rate at which a sender transfers data. This is done to ensure reliable delivery.
- The receiver continually hints the sender on how much data can be received.
3. **Error control** :
- Implements an error control mechanism.
- Error control is byte-oriented.
- Segments are checked for error detection.
4. **Congestion Control**
- The level of congestion in the network.
- Congestion level is determined by the amount of data sent by a sender.

# Differences between 


|   |   |   | 
|---|---|---|
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMDc1ODg2NDYsMTM1ODc5OTI0OSwtMj
EwNDU1MDE1Nl19
-->