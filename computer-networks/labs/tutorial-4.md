<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Explain which ARQ protocol, **selective reject** or **go-back-N**, would be less burdensome for a heavily trafficked World Wide Web server. The server is designed to receive relatively small messages from its clients, but may transmit much larger messages to them](#explain-which-arq-protocol-selective-reject-or-go-back-n-would-be-less-burdensome-for-a-heavily-trafficked-world-wide-web-server-the-server-is-designed-to-receive-relatively-small-messages-from-its-clients-but-may-transmit-much-larger-messages-to-them)
- [Explain the process of **frame encapsulation** and the role of the **Ethernet protocol** in **Local Area Networks** (LANs). (100 words)](#explain-the-process-of-frame-encapsulation-and-the-role-of-the-ethernet-protocol-in-local-area-networks-lans-100-words)
- [Describe the key differences between **routing** and **forwarding packets** in a network, and explain how **routers use routing tables** to determine the best path for forwarding data. (100 words)](#describe-the-key-differences-between-routing-and-forwarding-packets-in-a-network-and-explain-how-routers-use-routing-tables-to-determine-the-best-path-for-forwarding-data-100-words)
- [Compare IPv4 and IPv6 addressing schemes, highlighting the main differences in terms of address space, structure, and features. (100 words)](#compare-ipv4-and-ipv6-addressing-schemes-highlighting-the-main-differences-in-terms-of-address-space-structure-and-features-100-words)
- [Differentiate between static and dynamic routing protocols, and provide examples of each. What are the advantages and disadvantages of each approach? (100 words)](#differentiate-between-static-and-dynamic-routing-protocols-and-provide-examples-of-each-what-are-the-advantages-and-disadvantages-of-each-approach-100-words)
- [Explain the principles of **link-state** and **distance-vector routing algorithms**, and discuss their impact on **network performance** and **route management** (100 words)](#explain-the-principles-of-link-state-and-distance-vector-routing-algorithms-and-discuss-their-impact-on-network-performance-and-route-management-100-words)
- [Explain the role of the Transmission Control Protocol (TCP) in ensuring reliable data delivery, and describe how ports are used to identify specific processes or services in a network. (100 words)](#explain-the-role-of-the-transmission-control-protocol-tcp-in-ensuring-reliable-data-delivery-and-describe-how-ports-are-used-to-identify-specific-processes-or-services-in-a-network-100-words)
- [Compare the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP) in terms of reliability, connection, and speed. In what scenarios would one protocol be preferred over the other? (100 words)](#compare-the-transmission-control-protocol-tcp-and-the-user-datagram-protocol-udp-in-terms-of-reliability-connection-and-speed-in-what-scenarios-would-one-protocol-be-preferred-over-the-other-100-words)

<!-- markdown-toc end -->


# Explain which ARQ protocol, **selective reject** or **go-back-N**, would be less burdensome for a heavily trafficked World Wide Web server. The server is designed to receive relatively small messages from its clients, but may transmit much larger messages to them


* Selective reject AQR protocol is better as it lets receiver to selectively request retransmission if only these packets are not received correctly.
* AQR requires an acknowledgement from the receiver. After a timeout period, if the acknowledgement is not received then it means it failed.
* go-back-N ARQ protocol requires the send to transmit all the packages if there is an error.
  * This increases network congestion and delay the delivery of the correct packets to their destination


In the context of a heavily trafficked World Wide Web server that is designed to receive relatively small messages from its clients, but may transmit much larger messages to them, the selective reject ARQ protocol would be less burdensome compared to the go-back-N ARQ protocol.

The selective reject ARQ protocol, also known as selective repeat, allows the receiver to selectively request retransmission of only those packets that were not received correctly, instead of requesting the retransmission of all the packets starting from the erroneous one as in the case of go-back-N ARQ protocol. This means that the sender will only need to retransmit the corrupted or missing packets, reducing the amount of redundant data transmitted and thus saving network bandwidth.

ARQ (Automatic Repeat Request) is a protocol used in data communication to ensure the reliable delivery of data over an unreliable communication channel, such as the internet. It is a method of error control that involves the detection and retransmission of corrupted or lost data packets.

The ARQ protocol works by transmitting a block of data and then waiting for an acknowledgment from the receiver that the data has been received correctly. If the sender does not receive an acknowledgment or receives an acknowledgment indicating that the data was corrupted, it will retransmit the data block until it receives a correct acknowledgment.

There are several types of ARQ protocols, including Stop-and-Wait, Go-Back-N, and Selective Repeat. Each protocol has its own characteristics and advantages, depending on the specific application and requirements.

Overall, the ARQ protocol is an essential component of modern data communication systems, as it ensures the reliable and efficient transmission of data over unreliable communication channels, providing a high level of data integrity and reliability.

In contrast, the go-back-N ARQ protocol requires the sender to retransmit all the packets from the erroneous one, even if only one packet is lost or corrupted. This results in a significant amount of redundant data being transmitted, which can increase the network congestion and delay the delivery of the correct packets to their destination.

Therefore, the selective reject ARQ protocol is better suited for a heavily trafficked World Wide Web server, where bandwidth efficiency and low latency are crucial factors for maintaining the server's performance and user satisfaction.


# Explain the process of **frame encapsulation** and the role of the **Ethernet protocol** in **Local Area Networks** (LANs). (100 words)

* Add a header and trailer to a block of data to make a frame.
  * So that can be transmitted over a network.

* In LANs, ethnernet protocol, the header and trailer contains:
  * The source and destination **MAC addresses**.
  * Type of data being transmitted.
  * Error-checking information.

* Ethernet protocol allows data packets between devices to be transmitted.
  * Gives each device an **unique identifier** so data can be delivered to the right target.
  * Provide **error-checking** mechanisms to ensure interity of the data being transmitted.

Frame encapsulation is the process of adding a header and a trailer to a block of data to create a frame that can be transmitted over a network. In Local Area Networks (LANs), the Ethernet protocol is commonly used for frame encapsulation.

The Ethernet protocol defines the format of the header and trailer of the frame, which includes the source and destination MAC addresses, the type of data being transmitted, and error-checking information. The data block is then encapsulated in the frame, and the resulting frame is transmitted over the LAN.

The Ethernet protocol plays a crucial role in LANs by providing a standardized method for transmitting data packets between devices on the network. It allows devices to communicate with each other by providing a unique identifier for each device, ensuring that data is delivered to the correct recipient. Additionally, Ethernet provides error-checking mechanisms to ensure the integrity of the data being transmitted.

# Describe the key differences between **routing** and **forwarding packets** in a network, and explain how **routers use routing tables** to determine the best path for forwarding data. (100 words)

Routing:
* Determine the best path for data to travel from the source to the destination.
* Use **routing tables** to determine the best path for forwarding data.
* Routing table portrays the topology of the networks.

Forwarding:
* The actual transmission of data packets along the determined path.

* Routers use routing tables to determine the best path for forwarding data.

Routing and forwarding are two key processes involved in data transmission over a network. Routing involves the process of determining the best path for data to travel from the source to the destination, while forwarding involves the actual transmission of data packets along the determined path.

Routers use routing tables to determine the best path for forwarding data. Routing tables contain information about the network topology, including the available paths to different destinations and the associated costs or metrics for each path. The router examines the destination address in the incoming packet and uses the routing table to determine the best path for forwarding the packet to its destination. The router then forwards the packet along the determined path.

# Compare IPv4 and IPv6 addressing schemes, highlighting the main differences in terms of address space, structure, and features. (100 words)
IPv4 and IPv6 are two versions of the Internet Protocol that are used for addressing devices on the Internet.

* IPv4:
  * IPv4 uses a 32-bit address space, which can have up to approx. 4 billion unique addresses
  * requires 8 bit numbers
  * Separated by periods
  * Requires additional protocols for security.

* IPv6
  * IPv6 uses a 128-bit address space, which can have up to approx. 3.4 * 10^38 unique address.
  * Requires eight groups of 4 hexadecimal digits.
  * Separated by colons
  * Has built-in security
  * Supports **multicast traffic**.


# Differentiate between static and dynamic routing protocols, and provide examples of each. What are the advantages and disadvantages of each approach? (100 words)

* Static Routing Protocols
  * Manually configure the routes in the routing table by a network admin.
  * Has **routing information protocol version 1** (RIP v1) and **border gateway protocol** (BGP)
  * Pro: It is simple to configure and requries little maintenance
  * Con This is not suitable for large networks.

* Dynamic Routing Protocols
  * Automatcally update the routing table based on changes in the network topology.
  * e.g. **Routing information protocol version 2** (RIP v2), **open shortest path first**, and **enhanced interior gateway routing protocol**.
  * Pros: Very scalable.
  * Cons: Has high maintainance than static routing protocols.
    * Can be vulnerable to security attacks.


# Explain the principles of **link-state** and **distance-vector routing algorithms**, and discuss their impact on **network performance** and **route management** (100 words)

* Link State
  * Open shortest path first
  * Build a complete map of the netowrk to determine the shortest path between nodes.
  * Pros: More accurate routing decisions and faster convergence times.
  * Cons: Distance-vector routing procols can be slower to converge and less accurate than link-state routing procols.

* Distance-over routing algorithm
  * Determine the best path based on the distance or cost of the path.
  * Pros: Simplier routing decisions and **less memory usage**.
  * Cons: Distance-vector routing procols can be slower and less accurate.
  * e.g. Includes routing information protocol (RIP)

Choice depends on the complexity and performance of the network.


# Explain the role of the **Transmission Control Protocol** (TCP) in ensuring reliable **data delivery**, and describe how ports are used to identify specific processes or services in a network. (100 words)


* Tranmission control protocol
  * Used in computer networking to ensure reliable data delivery.
  * Set ups a connection between 2 devices and ensures data is tranissmitted in order.

* Ports
  * Identify specific process or services in a network.
  * Can be numbered anywhere from 0 - 65535
  * Some fixed ports are reserved for specific services.
  * e.g. port 80 for HTTP traffic, 22 for ssh traffic.
  * Included inside the pack header to indentify the specific process or service to which data is being sent.


The Transmission Control Protocol (TCP) is a transport layer protocol used in computer networking to ensure reliable data delivery. TCP establishes a connection between two devices and guarantees that data is transmitted correctly and in order. It also manages congestion control to prevent network congestion and ensure efficient data transfer.

Ports are used to identify specific processes or services in a network. Ports are numbered from 0 to 65535, with well-known ports being reserved for specific services. For example, port 80 is used for HTTP traffic, while port 22 is used for Secure Shell (SSH) traffic. When data is sent over a network, the port number is included in the packet header to identify the specific process or service to which the data is being sent.

# Compare the **Transmission Control Protocol** (TCP) and the **User Datagram Protocol** (UDP) in terms of **reliability**, connection, and speed. In what scenarios would one protocol be preferred over the other? (100 words) 

* TCP has better reliability but lower speed since it needs an acknowlegement from the receiver.
  * TCP is more connection-oriented data tranfer with error checking, flow control and congestion control

* UDP has higher performance compared to TCP because it does not require an acknowledgement
  * Does connectionless data transfer without any of the complexities of TCP.

* Scenario: reliaibility is critical
  * e.g. file transfers, emails, web browsing
  * TCP is preferred.

* Scenario: reliability is not as critcal but performance is critical
  * e.g. real-time voice and video streaming, gaming.
  * UDP is preferred.
  * UDP is also used for non-critical data transfers such as DNS queries or Simple Network Management Protocol SNMP

## Sources
[what is arq automatic repeat request](https://www.geeksforgeeks.org/what-is-arq-automatic-repeat-request/ )

[Link Text](https://www.cloudflare.com/learning/network-layer/what-is-routing/ )
https://kinsta.com/blog/ipv4-vs-ipv6/
