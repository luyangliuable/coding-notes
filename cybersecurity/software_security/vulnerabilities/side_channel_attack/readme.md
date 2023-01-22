# Side Channel Attacks

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Side Channel Attacks](#side-channel-attacks)
    - [Side-channel Attacks Methods](#side-channel-attacks-methods)
        - [Prime+Probe Attack](#primeprobe-attack)
        - [Flush+Reload Attack](#flushreload-attack)
        - [Page Fault Attack](#page-fault-attack)
        - [Adversary (Hardware level)](#adversary-hardware-level)
        - [Meltdown on Out of Order Execution (OOE)](#meltdown-on-out-of-order-execution-ooe)
            - [Steps to Out of Order Execution](#steps-to-out-of-order-execution)
            - [Meltdown Attack](#meltdown-attack)
            - [Difficulties](#difficulties)
        - [Foreshadow](#foreshadow)
        - [Difference between Meltdown Attack and Prime and Probe](#difference-between-meltdown-attack-and-prime-and-probe)

<!-- markdown-toc end -->

## Side-channel Attacks Methods
A type of attack that aims to extract sensitive information from a system by **analysing low-level information** such as **power consumption**, **electromagnetic emissions**, or **timing**. These attacks can be used to extract sensitive information such as encryption keys or other secret data.

* can be used to extract sensitive information from an enclave.

### Prime+Probe Attack
* Analyse the behaviour or the cache.
    * Attacker load large number of data chosen in a way to cause sensitive data to be loaded in the cache.
* Based on the fact that **accessing a memory location that is currently in the cache is much faster** than accessing a memory location that is not in the cache.

1. Prime phase: In this phase, the attacker loads a large number of data into the cache. This data is chosen in a way that it will cause the **sensitive data that the attacker wants to extract to also be loaded into the cache**.

2. Probe phase: In this phase, the attacker repeatedly accesses a large number of memory locations. By measuring the access time for each memory location, the attacker can determine **which memory locations are currently in the cache, and therefore which memory locations contain the sensitive data**.

```
1. Access to Memory to               2. Victim runs normal    3. Access memory again and measure
  fill all cache lines                code with dependent     the access time
                                      access patterns
         --------------             -------------               -------------
        | Cache Line 1 |           | Cache Line 1 |            |             | <- time this
         --------------             --------------              -------------
        | Cache Line 2 |           | Cache Line 2 |            |             | <- time this
         --------------             --------------              -------------
cache   | ....         |           | ...          |            |             | <- time this
         --------------             --------------              -------------
        |              |           |              |            |             | <- time this
         --------------             --------------              -------------
        | Cache Line n |           | Cache Line n |            |             | <- time this
         --------------             --------------              -------------
```

### Flush+Reload Attack
* Analyse the behaviour of cache similar to flush and reload that aims to extract sensitive information from a system by analysing the behaviour of the cache.

* Based on the fact that **accessing a memory location that is currently in the cache is much faster** than accessing a memory location that is not in the cache.

1. **Flush Phase**: The attacker uses a special instruction (such as CLFLUSH on x86 process) to flush a memory location out of the cache.
2. **Reload Phase**: In this phase, the attacker repeatedly accesses a large number of memory locations.
    * Then measuring the access time for each memory location, the attacker can determine which memory locations are currently in the cache and therefore which memory location contains the sensitive data.

```
1. Flush the cache lines         2. Victim runs normal        3. Access memory again and measure
  of interested address          code with dependent                the access time
                                    access patterns
         --------------             -------------               -------------
        | Cache Line 1 |           | Cache Line 1 |            |             | <- time this
         --------------             --------------              -------------
        | Cache Line 2 |           | Cache Line 2 |            |             | <- time this
         --------------             --------------              -------------
cache   | ....         |           | ...          |            |             | <- time this
         --------------             --------------              -------------
        |              |           |              |            |             | <- time this
         --------------             --------------              -------------
        | Cache Line n |           | Cache Line n |            |             | <- time this
         --------------             --------------              -------------
```

### Page Fault Attack
* Extract sensitive information by measuring the time it takes for a long fault to occur.
    * Occurs when memory page does not reside on physical memory so OS retrieves from disk.
* Exploits the time difference between page faults that occur when sensitive data is present in memory versus not.

```
1. Reset the present bit        2. Victim runs normal
  of interesting pages          code with dependent
                                    access patterns
         --------------             --------------
        |    Page 1    |           |    Page  1   |
         --------------             --------------
        |    Page 2    |           ||||Page||2||||| <---- Page Fault (From measurement)
         --------------             --------------
cache   | ....         |           | ...          |
         --------------             --------------
        |              |           |              |
         --------------             --------------
        |    Page n    |           |    Page  n   |
         --------------             --------------
```


### Adversary (Hardware level)
* Attacker who can access the "environment" but unprivileged
* Leakage from code is no longer necessary

```
                                                             -----------
                                                            |           |
                                                            | Adversary | \
                                                            |           |  \
                                                             -----------    \
                                                                  |          \
                                                                  X           \
                                                                  V            \
 -----------                                                 ------------       \  ------------
|           |  ------------ Attestation ------------------> |            |       \|            |
|    User   |                                               | Enclave    |  <-->  | Envinroment|
|           | --- communication via the secure channel ---> |            |        |            |
 -----------                                                 ------------          ------------
                                                            Computed securely
                                                        (conidentiality and integrity)

```

### Meltdown on Out of Order Execution (OOE)
* Process may choose to execution instructions out of order if it deems to be more efficient
* Exploit race condition for accessing sensitive data imposed by OOE
    * Allowing attacker to access data from memory

#### Steps to Out of Order Execution
1. Execute instructions based on the availability of hardware and source operands instead of the instruction order
2. Sort the execution result in a CPU buffer called re-order buffer (ROB)
3. During the instruction retirement, commit to registers in order or roll back if CPU realises a mispredication or exception

#### Meltdown Attack
    1. Access a probe buffer with *offset = secret * 4096*.
    * 4096 = size of page memory
    * "secret" = arbitrary value that the chosen to target a specific memory page believed to contain sensitive data.
    * Purpose is to load memory page into cache.
    * Location likely to contain sensitive data.
    * "Secret" is the guess? and value of the secret data.
2. Access memory page and count the access time.
    * Attacker repeatedly access a large number of memory pages.
    * Gauge which memory page contain the sensitive data.
3. The cached page w/ the shortest access time is likely the one containing the sensitive data. Extract data from memory page.

```
 -----------------------------------------------------      --------
|                                              ----   |    |        |
|                                   /-------->|    |<---\  |        |
|                                   |         |    |  | |  |        |
|                                   |          ----   | |  |        |
|                                   |          Cache  | |  |        |
|  ----------------------------     |     -------     | |  |   Mem  |
| | 1. mov al secret           |-------->| 1. ax |    | |  |        |
| | 2. sh ax 0xc               |         | 2. bx |    | |  |        |
| | 3. mov bx qword[bx+ax]     |<---X----|       |    | |   --------
|  ----------------------------           -------     | \--| al*4096| ------> Observe
|        Execution Unit                  reorder      |     --------
|                                         buffer      |    |        |
 -----------------------------------------------------      --------

```


#### Difficulties
* The contents in the enclave page cache (EPC) is encrypted
  * EVen if an attacker gains access to the EPC, they will not be able to read or modify the code and data that make up the enclave.
* An attempt to read a memory address in EPC return abort page (0xFF, not an exception )

### Foreshadow
* Variations of the meltdown vulnerability to target the sgx
    * Bypass the abort page semantics when using meltdown to access data in enclave.
    * Exploits **speculative execution**.
* Observations:
    * Abort page semantics apply only when the legacy page table check is done without exception.
    * When processor encounters an exception it is not handled immediately and the processor continues to execute code speculatively.
    * mprotect() can be used to clear the "present" bit of a page.
        * a flag that indicates whether a page is currently in memory or not.
        * By clearing the "present" bit, the attacker can cause the legacy page table check to fail and allow the exploitation of the vulnerability.
* Can be used to recover provisioning key and the recover attestation key to attest any malicious enclave in the remote platform.

## References
[Meltdown explained like you're five](https://www.youtube.com/watch?v=JSqDqNysycQ)
