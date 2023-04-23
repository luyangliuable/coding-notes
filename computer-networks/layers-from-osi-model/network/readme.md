# Network Layer

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Network Layer](#network-layer)
    - [10 Principals](#10-principals)
    - [Components of Network Layer](#components-of-network-layer)
    - [The Network Layer in the internet](#the-network-layer-in-the-internet)

<!-- markdown-toc end -->

## 10 Principals

1. Make sure it works
2. Keep it simple
3. Make clear choices
4. Exploit modularity
5. Expect heterogeneity
6. Avoid static options with parameters
7. Look for a good design; it need not be perfect
8. Be strict when sending and tolerant when receiving
9. Think about scalability
10. Consider performance and cost

## Components of Network Layer
1. IP Version 4 Protocol
2. IP Addresses
3. IP Version 6 Protocol
4. Internet control Protocols
5. Label switching and MPLS

## The Network Layer in the internet

![](a8Of.png )

## Types of networks
* Subnets
* Prefixes
  * A contiguous block of IP address space
* CIDR
  * Classless interDomain Routing
* Classful and special addressing
* NAT
  * Network Address Translation

## Prefix and a Subnet Mask

```
                                32 bits
            <------------------------------------------------>
                        L bits                   32 - L bits
            <---------------------------------><------------->
             -------------------------------------------------
            |             Network             |      Host     |
             -------------------------------------------------
Subnet mask  111111111111111111111111111111111 0 0 0 0 0 0 0 0
```
    * Both prefixes and subnet masks are used to defining the boundaries of a network.
      * Important for routing traffic and ensuring that packets are delivered to their intended desintations.

e.g. Prefix is 24 and subnet mask is a 32-bit value.
    * Subnet mask is set to 1.
    * 1 bits represent network portion
    * 0 bits represent the host portion
    * 255.255.255.0

## Subnets
![Alt Text](YU0.png ) 
