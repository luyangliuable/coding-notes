# Remember

## Difference between Send, Ssend, ISend, Issend, Ibsend, Bsend.

### Requirements of sending a message
* There must be a corresponding ready receive from the other process.
* Needs enough space from buffer attached to MPI. MPI_Buffer_attach()
* The user must not attempt to reuse the buffer until the message is passed to the buffer attecheed to MPI.

* Send
  * Will issue either a MPI_Bsend (buffered send) or MPI_Ssend (synchronous blocking send).
  * If the buffer attached to MPI has enough space then MPI_Bsend.
  * If the buffer attached to MPI don't have enough space then MPI_Ssend.

* Ssend (S stands for synchronous)
    * Synchronous blocking send.
    * Guarantees thats the buffer passed can be safely recused once MPI_Ssend returns.

* Isend
    * non-unblocking send where I stands for immediate return
    * will issue asynchronous non-blocking send Ibsend if there is enough space in the buffer attached to MPI. Otherwise will issue MPI_Issend.

* Ibsend (I stands for immediate return)
    * Asynchronous non-blocking send will not wait until the copy of the buffer is delivered to the recipient.
    * Opposite to Bsend.

* MPI_Bsend (B stands for buffered)
        * Asynchronous blocking send will wait until a copy of the buffer is passed to the recipient.

* Issend (I stands for immediate return)
    * Synchronous non-blocking send

* Nonblocking unsynchous send

## Difference between features of MMX, SSE, SSE2, SSE3, SS4 and AVX.
| 1997                                          | 1999                                                                   | 2000                                                                                       | 2003                   | 2007                                          | 2011                                   |
|:---------------------------------------------:|:----------------------------------------------------------------------:|:------------------------------------------------------------------------------------------:|:----------------------:|:---------------------------------------------:|:--------------------------------------:|
| MMX                                           | SSE                                                                    | SSE2                                                                                       | SSE3                   | SSE4                                          | AVX                                    |
| 8 64-bit registers                            | 8 128 bit registers expandable to 16 registers for 64 bit architecture | Enabled both integer and floating based operations to be performed using the XMM registers | Horizontal operations. | Additional instructions for vector operations | 16 256 bit registers                   |
| MM0 -> MM7                                    | XMM0 -> XMM8, to XMM15                                                 |                                                                                            | Asymmetric processing  |                                               | YMM0 -> YMM15                          |
| Only performs integer based vector operations | Performs floating point based vector operations                        |                                                                                            |                        |                                               | New instructions for vector operations |
| Shares registers with x87 FPU                 |                                                                        |                                                                                            |                        |                                               |                                        |
| Cannot perform integer and FPU                |                                                                        |                                                                                            |                        |                                               |                                        |
