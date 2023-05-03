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

## Question 4:
Explain the relationship between the **World Wide Web** (WWW), **Hypertext Transfer Protocol (**HTTP), and **Hypertext Transfer Protocol Secure** (HTTPS) in the context of **internet communication**. 

Provide a brief overview of their respective roles and how they work together to enable secure and efficient web browsing. Highlight the main differences and advantages of using HTTPS over HTTP.


* `www` is a system of interconnected documents and resources that can be accessed via the internet.
* `http` is used to transfer data between web servers and clients.
* `https` is a secure version that uses encryption to protect transmitted data over the internet.

| https                                  | http                  |
|:--------------------------------------:|:---------------------:|
| Enhanced security, prevent MITM attack | minimal security      |
| Improves SEO                           | lowers ranking in SEO |
| better user trust                      | not trustworthy       |


## Question 5:
Explain the concept of **dynamic web pages**, highlighting their purpose and how they differ from **static web pages**. Provide a brief overview of the **technologies used to generate dynamic content** and the advantages they offer in terms of user experience and content management. 

* Dynamic web pages
  * Generated continuously by updating new content into the frontend (client) from the backend (server).
  * Technologies
    * Any server-side script like PHP, node or python
  * Advantages
    * Stores state onto the backend
    * Allows greater interactivity and data retention hence better user satisfaction.
    * Easier for web devs to update content
    * Reduce the amount of effort to maintain web site.
* Static web pages
  * Often generated from a single http request

## Question 6
Explain the concept of a **Content Delivery Network** (CDN), focusing on its purpose and how it helps improve the **delivery of content over the Internet**. Briefly discuss the key components of a CDN and the techniques it employs to reduce latency, **increase availability**, and ensure **efficient distribution** of data to end users.

* Content Delivery Network
  * System of geographically distributed servers that work together to improve content delivery over the internet.
  * Purpose
    * Increase avalaiblity
    * Allow data to be distributed to end user efficiently
    * Reduce latency
  * Key components
    * Edge servers
      * Severs that are closest to the end user.
      * Cache and deliver content to user.
    * Origin servers
      * Servers that Store the original content
      * Generate and deliver content to edge servers
    * Load balancers
      * Distributing user request among edge servers, ensuring request is handled efficiently and effectively.
  * Techniques
    * Routing optimization
    * Compression
    * Caching


## Question 7:
Provide an explanation of **Voice over IP** (VoIP) and **Video over IP** technologies, focusing on their purpose and how they enable multimedia communication over the Internet. Briefly discuss the role of codecs in these technologies and their impact on quality and bandwidth requirements.

* Voice over IP
  * Transmit real-time voice over the internet.
  * Convert analog waves (voice) into packets that can be transmitted over the internet using IP protocols.
* Voice over IP
  * Transmit real-time video over the internet.
  * Convert video into packets that can be transmitted over the internet using IP protocols.

* Codecs
  * Allow compression and decompressing the voice and video data.
  * Reduces size of data needed to be transmitted over the internet and bandwith requirements.
  * However, it can reduce the quality of voice and video data.
  * Higher compression ratio leads to high loss of data.


## Question 8:
Explain the concept of **sockets** in **computer networks**, including their purpose and how they enable communication between devices. Provide a brief overview of the **socket types** and their **roles in network communication**.

* Sockets
  * Enable two way communication between devices.
  * Represented by an IP address and a port number
  * Types
    * Stream sockets
      * reliable
      * data is in orginal order
    * Datagram sockets
      * unreliable
      * connectionless
      * For application that require fast transmission
  * Sockets
      

    
