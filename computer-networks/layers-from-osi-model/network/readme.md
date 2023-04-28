# Network Layer

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Network Layer](#network-layer)
    - [10 Principals](#10-principals)
    - [Components of Network Layer](#components-of-network-layer)
    - [The Network Layer in the internet](#the-network-layer-in-the-internet)
    - [Types of networks](#types-of-networks)
    - [Prefix and a Subnet Mask](#prefix-and-a-subnet-mask)
    - [Subnets](#subnets)
    - [Classless Interdomain Routing (CIDR)[#network]() [#cidr]()](#classless-interdomain-routing-cidrnetwork-cidr)
    - [References](#references)

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

* Divide a network into two or more networks.
* Divide the host identifier portion of an IP address into two or more parts using a subnet mask.
* e.g. Sub netting address range of 192.168.1.0 - 192.168.1.255 into 4 smaller subnets.
    * Subnet mask is 255.255.255.192
    * CIDR Notation is /26
    * 192 is chosen because it allows us to create 4 subnets with 64 values each.
    * First Subnet
        * 255.255.255.192 bitwise AND 192.168.1.0 = 192.168.1.0
    * Second Subnet
        * 192.168.1.0 Bitwise OR 0.0.0.63
        
```
00000000
AND
11000000
=
00000000
```

```
00000000
AND
11000000
=
00000000
```

## Classless Interdomain Routing (CIDR)[#network]() [#cidr]()
* Method for allocating IP addresses and routing traffic.
* Slow the growth of routing tables on routers across the internet and help slow the rapid exhaustion of IPv4 addresses.
* Uses suffix to represent number of bits in the network prefix.
* Uses variable length IP prefixing
  * Allows more efficient use IP addresses.
  * Flexible allocation of IP address blocks.
  
* A set of IP Address Assignments
![](yj8+.png) 

* Aggregation of IP prefixes
![](R+G5.png) 

* Longest matching prefix routing at the New York router.
![](XGnb.png) 

### CIDR Notation

e.g. /19 means first 19 bits of IP address is used to represent the network and remaining bits is used to identify the host.

## CIDR vs Subnet
* Generally mean the same thing
* CIDR is referred at ISP level
* Subnet is referred to at organizational level.


## Workshop Questions

A network administrator is given the IP address block 192.168.0.0/21 for a local area network. The network needs to be divided into four equal sized subnets. What will be the new subnet mask and range of IP address for each subnet? 

2^2 = 4

11000000 = 2^6 + 2^7 = 192

255.255.255.192

range = 64

* You are given the IP address block 192.168.10.0/24

## The purpose of subnets is to:

Minimize traffic: Subnets split a large network into smaller, interconnected networks to help reduce traffic, allowing data to flow through fewer routers and increasing network speeds 

Improve address allocation efficiency: Subnetting improves the allocation of IP addresses by subdividing large networks into smaller segments 

Reallocate IP addresses: Subnets enable network administrators to use a single block of addresses on multiple physical networks, reducing the need for additional address blocks 

Relieve network congestion: Placing frequently communicating devices on the same subnet can reduce network traffic 

Improve network security: Subnetting allows administrators to quarantine compromised sections of the network and make it more difficult for trespassers to move around the network 

Efficient data routing: Subnets segregate broadcast domains into smaller sections, which results in fewer nodes for broadcast traffic to interact with, making data routing efficient and direct 

Enhanced network security: Subnets help secure larger networks by isolating compromised segments and controlling access to devices running on the entire network 

Subnet masks play a crucial role in these purposes by ensuring that traffic remains within the defined subnet, reducing congestion, and enhancing overall network performance and speed 

## References
[cidr](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) 
[Link Text](https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references/) 
