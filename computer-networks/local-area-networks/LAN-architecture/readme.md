# LAN Architecture

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [LAN Architecture](#lan-architecture)
    - [Key points on LANs](#key-points-on-lans)
    - [Protocol Architecture](#protocol-architecture)
        - [Physical Layer](#physical-layer)
    - [Topologies](#topologies)
        - [Cable Lan Topologies](#cable-lan-topologies)
        - [Wired LAN toplogies](#wired-lan-toplogies)
    - [Media Access Control](#media-access-control)
        - [Different Protocols of MAC](#different-protocols-of-mac)
    - [Logical Link Control](#logical-link-control)

<!-- markdown-toc end -->

## Key points on LANs
* **High bandwidth** and **low cost** is the key advantage since the first ethernetl.
* Most LANs maintains **backward capability**.
* CMSMA based LANs now dominate the market.
  * 802.3 and 802.11
* LAN technology is now a commodity product devices like routes, repeaters, calbes can be purchased in department stores.
* Wireless LANs are popular (802.11)
  * Even though poor performance and reliability.
  * Cabled LANs is the benchmark for performance.
* LAN technology is now a **commodity product**.
  * Devices like routers, repeaters cables can be purchase in department stores

## Protocol Architecture
    * Most LAN standars define both the **physical layer** and the **datalink layer** for the LAN.
    * IEEE 802 reference model
    * Physical Layter
    * Data link control (LLC)
    * Media access control (MAC)
    * Responsible for **lower layers of OSI Model**

### Physical Layer
    * LAN does the folllowing
      * Encoding and decoding
      * Preamble generation/removal
      * Bit transmission/reception
      * Transmission medium and topology.

## Topologies

### Cable Lan Topologies

* Bus Topology

```
  Tap
   |
   v    <---- Flow of data ---->                Terminating resistnace
▉---------------------------------------------------------▉
   |         |         |         |         |         |
 -----     -----     -----     -----     -----     -----
|     |   |     |   |     |   |     |   |     |   |     |
|     |   |     |   |     |   |     |   |     |   |     |
 -----     -----     -----     -----     -----     -----
```

* Ring topology

▉ = Repeater

```
 -----                           -----
|     |                         |     |
|     |<->▉-----------------▉<->|     |
 -----    |                 |    -----
          |                 |
          |                 |
          |                 |
          |                 |
          |                 |
 -----    |                 |    -----
|     |   |                 |   |     |
|     |<->▉-----------------▉<->|     |
 -----                           -----

```

* Headend topology


```
              -------------------------------------$
             /
            /   ^          ^           ^
           /   --         --          --
          /   |  |       |  |        |  |
         /     --         --          --
        /       v          v           v
       /                <------------->
▉------------------------------------------$
     \           ^           ^
      \          --          --
       \        |  |        |  |
        \        --          --
         \                   v
          \   <------------->
          -----------------------------------$
```

* Star
    * Centeral Hub, Switcher or Repeaster (master-slave) topology
```
  -----------------------------------
 | Central Hub, Switcher or Repeater |
  -----------------------------------
  ^        ^       ^       ^       ^
  |        |       |       |       |
  v        v       v       v       v
 ----     ---     ---     ---     ---
|    |   |   |   |   |   |   |   |   |
|    |   |   |   |   |   |   |   |   |
 ----     ---     ---     ---     ---

```

### Wired LAN toplogies
    * Infrastructure Wireless LAN
    * Ad Hoc Lan (aka. Wireless hotspot)

## Media Access Control
    * MAC exists in the datalink layer.
    * Provides aaddressing and channel access control mechanisms allowing multiple devices to share a common communication channel.
    * IN LAN, MAC layer protocols can be **ethernet**, **WIFI** and **token rings**.
    * **Ensuring reliable transmission** of data packets over a medium.

    * Assemble data into frames with address and **error detection fields**.
    * Disassembly of frame
      * Address recognition
      * Error detection
    * Govern access to transmission medium
      * This is not found in typical layer 2 data link control

### Different Protocols of MAC
    * For the same Logical Link control, several MAC options may be avalaible.
      * Provides difference trade-offs between factors such as **network throughput**, **latency** and **reliability** and cost.
      * Allows designers to choose the best option on specific needs of their network.
      * Example
        * Ethernet often use MAC protocol that offer higher throughput and low latency.
        * Wifi often use MAC procotol to reduce interface but offer lower throughput compared to wired ethernet.

    * Token Rings
      * Mostly Legacy systems may still rely on these MAC protocols
      * Variants
        * FDDI
    * Ethernet
      * Each has different data rates and physical media requirement.
      * Variants
        * 10Base-T
        * 100Base-Tx
        * 10000Base-T


## Logical Link Control
    * Interface to higher levels
    * Folow control
    * Error control
