# Medium Access Control (MAC)

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Medium Access Control (MAC)](#medium-access-control-mac)
    - ['In queuing terms'](#in-queuing-terms)
    - [Strategies for Multi-access problekm](#strategies-for-multi-access-problekm)
        - [Free-for-all](#free-for-all)
            - [Collisions](#collisions)
        - [Perfectly Scheduled](#perfectly-scheduled)
        - [Techniques](#techniques)
            - [Slotted Time](#slotted-time)
            - [Carrier Sense](#carrier-sense)
        - [Multi-access methods/algorithms](#multi-access-methodsalgorithms)
        - [Widely used Multi-access Media](#widely-used-multi-access-media)

<!-- markdown-toc end -->

* Allows sharing of a communication channel between **nodes/stations/users** where each has **different service requirements**.

* Allocates a single channel among competing users.

* This problem arises in LANs, MANs, Satellite networks and various types of wireless radio networks.

* Belongs to a **sublayer of data link layer** called the "Medium Access Control" sublayer.

## 'In queuing terms'
* Muti-access systems in a sense is like a **distributed queue**.

* Each node has a **queue** of packets of be tranmitted,
* Multi-access channel is a common server.
* MAC should view all waiting packets as one combined queue to be served by **queuing discpline**.
* MAC does not know which node contains packets and nodes are unaware of packets of other nodes.

## Strategies for Multi-access problekm

```
                  ----------------------
                 | Multi-access sharing |
                  ----------------------
                  /                  \
                 /                    \
 ----------------------            -------------
| Collision Resolution |          | Reservation |
 ----------------------            -------------
    e.g. Purse Aloha               /            \
                        ------------------      --------------------
                       | Fixed Allocation |    | Dynamic Allocation |
                        ------------------      --------------------
                        e.g. FDM and TDM       e.g. CSMA/CD, token ring

```

* Dynamic Allocation
  * Use of collion resolution
    * Implicity reservation
    * e.g. Ethernet (CSMA/CD)
  * Round robin ordering
    * Token ring
    * Token bus

### Free-for-all
* Nodes normally send new packets immediately hoping for no interference from other nodes.

#### Collisions
* When two frames are transmitted simultaneously.
* Must manage **collisions** when packets are transmitted simultaneously.
* Results in signal to be distorted.

### Perfectly Scheduled
* Nodes received **reserved interval** for channel use.
* What determines **scheduling order**?
* How long can a **reserved interval last**?
* How are nodes **informed** of their oder?

### Techniques

#### Slotted Time
* Time is divided into discrete intervals called slots.
* Frame transmission delays behin at the start of a slot.
* Slot often contain 0 or 1 transmission or a collision respectively.

#### Carrier Sense
* Station can tell if the channel is in use before trying to use it.
* If the channel is sense as busy then no station will use it until it goes idle.


### Multi-access methods/algorithms
* Reduce delay
* Increase avalaible throughput
* Maintain stable operation

### Widely used Multi-access Media
* Satellite channel
* Packet radio networks
* Multitapped bus
