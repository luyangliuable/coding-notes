# Carrier Sense Multiple Access

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

## CSMA wiwth Colision Detection Protocol
* Enhancement from CSMA protocol
* Can detect collisions during their transmission.
* As soon as a collision is detected, abort the transmission immediately so that the common channel can be freed for next use.

* Transceiver will read the channel and compare the detected signals against the transmitted signals.
* If `detected signal strength != transmitted signal strength`, signal interference has occurred probably.

## Transmission in CSMA with Collision Detection
* The terminals choose a future random slot for re-transmission of the packet
