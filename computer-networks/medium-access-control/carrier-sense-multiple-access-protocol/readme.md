# Carrier Sense Multiple Access

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Carrier Sense Multiple Access](#carrier-sense-multiple-access)
    - [Persistent Carrier Sense Multiple Access](#persistent-carrier-sense-multiple-access)
    - [1-persistent CSMA](#1-persistent-csma)
    - [Non-Persistent Carrier Sense Multiple Access](#non-persistent-carrier-sense-multiple-access)
    - [Persistent vs Non-persistent CSMA](#persistent-vs-non-persistent-csma)
    - [CSMA wiwth Colision Detection Protocol](#csma-wiwth-colision-detection-protocol)
        - [Transmission in CSMA with Collision Detection (CSMA/CD)](#transmission-in-csma-with-collision-detection-csmacd)
        - [Binary Exponential Back off](#binary-exponential-back-off)

<!-- markdown-toc end -->


* An attempt to improve from 'Alohas'
* Make termianls listen to the common channel when they are ready for transmission
* Make sure the common channel is clear before they can transmit
* Many unnecessary collisions may be avoided.

## Persistent Carrier Sense Multiple Access
* Define the rules , they will that how a terminal should react when it is ready but sense a busy channel.
* When channels turns idle with probability of 'p', the terminals transmit their data frames at the start of the next timeslot.
* Probability of '1-p', stations define one more timeslot.

## 1-persistent CSMA
* A special case of p-persistent where p = 1

## Non-Persistent Carrier Sense Multiple Access
* When terminals sense a busy channel as they are ready:
  * backoff for a while and return back to sense the channel some time later.

## Persistent vs Non-persistent CSMA

| 1-persistent                                                 | non-persistent                                                                       | p-persistent csma                                                                                                  |
|:------------------------------------------------------------:|:------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------:|
| If medium is busy, keep sensing the medium until it is free. | If medium is busy, keep sensing the medium until it is free                          | If medium is busy, wait for a random amount of time then check again.                                              |
| Once medium is free, transmit data immediately.              | Once medium is free, waits for a random amount of time before transmitting the data. | Once the medium is free, start transmitting the data if random value p <= 1 else wait for a random amount of time. |



## CSMA wiwth Colision Detection Protocol

* CSMA/CD can be inside the following modes
  * Transmission period
  * contention period
  * idle state

```
 ------------------------ - - - -------- - - - - -------       - -------
|         Frame          | | | | Frame  | | | | | Frame |     | | Frame |
 ------------------------ - - - -------- - - - - -------       - -------
   Transmission Period      \                        idle Period
                             \
                             Contention period
```

* Enhancement from CSMA protocol
* Can detect collisions during their transmission.
* As soon as a collision is detected, abort the transmission immediately so that the common channel can be freed for next use.

* Transceiver will read the channel and compare the detected signals against the transmitted signals.
* If `detected signal strength != transmitted signal strength`, signal interference has occurred probably.

### Transmission in CSMA with Collision Detection (CSMA/CD)
* Improvement from `CSMA`
* The terminals choose a future random slot for re-transmission of the packet

### Binary Exponential Back off

* Binary Exponential Backoff

backoff_time = 2^k - 1

```
   Collision
     ___
    |   |
----|---|----|---|----|----> Time
  n  n+1 n+2  n+3  ...
```

| Number of continuous collisions experienced in the past `c` | Possible Slots for Retransmission |
|:-----------------------------------------------------------:|:---------------------------------:|
| 1-9                                                         | [n+1, n+2^c]                      |
| 10-16                                                       | [n+1, n+2^10]                     |
| >16                                                         | =ABORT=                           |

## CSMA/CA
TODO


## Examples

1. A network has **5 devices** connected to it, and they are all using **CSMA/CD** with **Binary Exponential Backoff**. Device A experiences a collision when trying to transmit data. Calculate the minimum and maximum backoff times (in microseconds) for Device A after **each collision**, up to the **3rd collision**. Assume that the network is using Ethernet with a slot time of 51.2 microseconds.

BEA = 2^k - 1

* First collision
BEA  = 2^1 - 1 = 1
Time  = 51.2 * 1 = 51.2 microseconds
Range = [0, 51.2]

* Second collison
BEA = 2^2 - 1 = 3
Time = 51.2 * 3 = 153.6 microseconds
Range = [0, 153.6]

* Third Collison
BEA = 2^3 - 1 = 7
Time = 51.2 * 7 = 358.4 microseconds
Range = [0, 358.4]

2. Calculate the total time taken for device to transmit a data frame using CSMA/CA in a wireless network, given the following paramters?
* Dataframe size: 1500 bytes
* Data rate: 1Mbps
* Distributed inter-frame  space: 50 microseocnds
* Short inter-frame space: 20 microseconds
* Contention window size: 16
* Ack frame size: 20 bytes
* Assume the device has to wait for the average backoff time. Use slot time 20 microseconds.

avg_backoff_time = (cw - 1) * slotted_time/2
avg_backoff_time = (16 - 1) * 20/2 = 150 microseconds

data_frame_transmittion_time = (1500*8)/(1*10^6) = 1.2 * 10^4 microseconds

ack_frame_transmission_time = (20*8)/(1*10^6) = 1.6 * 10^2 microseconds seconds

Total = 150 + 1.2*10^4 + 1.6*10^2 + 50 + 20  = 12380 ms

 C:\enett\Applications\ph-web
or D:\eNett\Applications\ph-web


2. You are given the IP block `192.168.1.0\24` and you need to subnet it into 3 smaller networks with the following host requirements.

* Network A: 60 hosts
* Network B: 30 hosts
* Network C: 10 hosts

Calculate the subnet masks for each of the 3 networks.


* Network A
  * 2^6 = 64 hosts which can hold enough
  * 1100000 = 2^6 + 2^5 = 96
  * Subnet mask is therefore 255.255.255.96
  * CIDR format is \26
