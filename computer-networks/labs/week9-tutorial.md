## Question 1:
Explain the **core concepts of routing protocols**, including their purpose in computer networks and
their **role in route discovery** and route management. Provide a brief overview of the key functions
these protocols perform to ensure efficient and reliable communication between devices.

* Routing protocols ensures efficient and reliable communication between devices.
* Their purpose is to determine the optimal path for traversing one network to the other

* Key functions of routing protocol
  * Path determination
  * Route aggregation.
  * Discovery of network topology.
  * Routing propagation

## Question 2:
Discuss the advantages **SCTP** and **QUIC** offer in terms of **performance**, **reliability**, and **security** for **network communications**.

* SCTP
  * Provides reliable connection while being faster compared to TCP.
  * Can handle multiple streams of data within a single connection.
  * Practical for application needing high reliability and low latency.

* Quic
  * Faster compared to TCP.
  * Built-in security features for data transmission.
  * Built-in congestion control and error correction.
  * Has high reliability.
  * Supports multiplexing

## Question 3
Explain primary functions of **SMTP**, **IMAP** and **POP** in the context of email communication and highlight the main differences between IMAP and POP in terms of email retrieval and management.

* Simple Mail Transfer Protocol (SMTP)
  * For transferring emails between email servers
  * Mail first arrives to the mail server after being sent, then it is handled by either IMAP or POP to retrieve the message and deliver it to the recipient.
  

* Internet Message Access Protocol (IMAP)
  * Allows user to access email from multiple devices as the mail remain on the server.
 
* Post Office Protocol (POP)
  * Download email from server to user's address and delete the email from the server.

| IMAP                                | POP                                                      |
|:-----------------------------------:|:--------------------------------------------------------:|
| Mail will remain on the server      | Once downloaded from server, mail is deleted from server |
| Multiple devices can download email | Only one device can download email                       |

Question 4:
Explain the relationship between the **World Wide Web** (WWW), **Hypertext Transfer Protocol (**HTTP), and **Hypertext Transfer Protocol Secure** (HTTPS) in the context of **internet communication**. 
P
rovide a brief overview of their respective roles and how they work together to enable secure and efficient web browsing. Highlight the main differences and advantages of using HTTPS over HTTP.


* `www` is a system of interconnected documents and resources that can be accessed via the internet.
