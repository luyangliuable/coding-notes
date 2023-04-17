# Aloha Protocol

* Wireless access from a **mainframe** invented and demonstrated in Hawaii.

## Pure Aloha
* In pure Aloha, frames are transmitted at **completely arbitrary times**.

User
    ---------------------------------------------------------
A         |     |
    ---------------------------------------------------------
B             |     |
    ---------------------------------------------------------
C                 |     |
    ---------------------------------------------------------
D   |    |
    ---------------------------------------------------------
              |<-collison->|
                        Time ---->

### Steps
1. Terminals will start transmitting immediate hoping for no collision.
2. Sender will realise its transmission failed by not receiving an **acknowledgement** some time after the completion of its tranmission.

### Why pure Aloha at all?

* Early days: the hardware was not advanced. Complicated protocols were both difficult and expensive to implement.
* Each terminal only transmits a very small amount of information and the total number of terminals at the time was small hence the chances of transmission were very small.


## Slotted Aloha
* An attempt to improve from `pure Aloha`
* All terminals are somewhat synchronous when they are ready.
* Only transmit at the beginning of a time slot.

```

Master Timebase
     ---
    | T |
     ---

User
    ---------------------------------------------------------
A   |     |
    ---------------------------------------------------------
B         |     |
    ---------------------------------------------------------
C                        |     |
    ---------------------------------------------------------
D   |     |
    ---------------------------------------------------------
    |<-collison->|
                        Time ---->


```
