# Intel Software Guard Extensions

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Intel Software Guard Extensions](#intel-software-guard-extensions)
    - [Hardware Assisted Trust](#hardware-assisted-trust)
        - [Examples (that are also TCBs)](#examples-that-are-also-tcbs)
    - [Trusted computing Base (TCB)](#trusted-computing-base-tcb)
    - [Isolation in Trusted Execution](#isolation-in-trusted-execution)
    - [SGX Threat Model](#sgx-threat-model)
    - [SGX Security Services](#sgx-security-services)
        - [Features of SGX Trusted Computing Enabler](#features-of-sgx-trusted-computing-enabler)
    - [SGX + Secure Boot](#sgx--secure-boot)
    - [Employ basic programming model of SGX](#employ-basic-programming-model-of-sgx)
    - [Side-channel Attacks Methods](#side-channel-attacks-methods)
        - [Prime+Probe Attack](#primeprobe-attack)
        - [Flush+Reload Attack](#flushreload-attack)
        - [Page Fault Attack](#page-fault-attack)
        - [Adversary (Hardware level)](#adversary-hardware-level)
    - [SGX Enclave](#sgx-enclave)
        - [Trusted Section](#trusted-section)
        - [Untrusted Section](#untrusted-section)
        - [Ecall and Ocall functions](#ecall-and-ocall-functions)
            - [Example](#example)
    - [Source](#source)

<!-- markdown-toc end -->
  * **Encryption**: Protection of data in transit and at rest
* Prevention and Response Mechanisms
  * **Monitoring**: Detection and response to security incidents
  * **Policies**, **procedures**, and **standards**: Governing the security of systems and networks

## Hardware Assisted Trust
Use of hardware-based security features to enhance the security and trust of system.

### Examples (that are also TCBs)
* Secure boot
    * Verify the integrity of system's firmware and os during startup.
    * Prevent malicious software from loaded during boot process.
* Secure storage
    * Hardware-based encryption and secure key storage to protect sensitive data (e.g. on hard disk).
* **Secure enclaves**
    * Hardware or software environment adding extra layer of security for sensitive data and operations.
    * Only trusted software is executed.
    * Sensitive data is protected.
    * Operations are performed in a secure environment
    * Only trusted software is executed, sensitive data is protected, operations are performed in a secure environment.

## Trusted computing Base (TCB)
* Use of hardware, software and controls to
    * ensure trust
    * enforce security policy.
    * protect system from unauthorised access
* Has the **highest OS privilege** level.
* **Responsible for system's security police enforcement**. **Core** of system's security
* It is **small** to facility thorough and detailed examination of come base
* Managed and **thoroughly checked periodically** for security compliance.
* Must be also be protected from itself
    * Incl. built-in mechanisms to detect and prevent unauthorised access or modifications to its own components.

## Isolation in Trusted Execution
* Separation of resources via trust verification mechanisms
    * prevent unauthorised access to sensitive data such as authentication or encryption.
    * use of authentication, encryption, access controls and encryption.
* Can create self-contained **computation** and **communication** environments
    * e.g. **Virtual machines** or **containers** isolated from the rest of the system.
    * **Limit the scope** or attack surface of a potential security incident.
* System separation in trusted and untrusted zones.
    * Trusted zone is protected by TCB.
    * Trusted zone: Secure environment for sensitive operations and data.
    * Untrusted zone: Store less sensitive operations and data can be access by trusted zone.
* Handled by a specialised level consisting of collection of software tools that use the **TCB services**.
    * TCB is implemented at a low level of the system.
    * The TCB is implemented at a low level of the system such as **firmware or kernel**.
    * Provide an additional layer of protection.
    * TCB services example incl. secure boot, secure enclaves

## SGX Threat Model
* Cloud provider's software (e.g. web, cloud and remote access services) are malicious,
  * modifying the OS to install malware.
  * modifying the firmware to disable security features.
  * **SGX guarantees that the code/data inside the enclave cannot be accessed by an attacker, even if the attacker has gained full control of the system's firmware, BIOS, and operating system**.

* All hardware besides the CPU is untrusted
    * An attacker could install a hardware **keylogger** on via I/O, or could use a **hardware-based rootkit** to gain persistent access to the system.
    * **If either CPU, firmware, BIOS, or operating system is compromised the security guarantees provided by SGX can be bypassed**.


## SGX Security Services
* Trusted computing enabler
    * secure computer on someone else's computer
    * ability to provide **trusted execution environment** (TEE) enabling deployment of secure applications/services
      * TEE is a secure area of the main processor

### Features of SGX Trusted Computing Enabler
* Confidentiality: code and data inside an enclave cannot be accessed or modified by an attacker, even if the attacker has gained full control of the system's firmware, BIOS, and operating system.

* Integrity: SGX guarantees that the code and data inside an enclave cannot be tampered with or modified by an attacker, even if the attacker has gained full control of the system's firmware, BIOS, and operating system.

* Remote Attestation: SGX guarantees that a **remote party can verify the identity and configuration of an enclave, and can confirm that the code and data inside the enclave have not been tampered with or modified**.

* Key Protection: SGX guarantees that the keys used to encrypt and decrypt data inside the enclave are protected from attackers.


## SGX + Secure Boot
By using Secure Boot and SGX together, the system can ensure that it is running only authorized software during the boot process and that sensitive data and operations are protected by SGX. Secure boot can also ensure that the firmware and OS are not compromised before SGX starts.

* Secure boot is not part of SGX.

## Employ basic programming model of SGX
1. App is built with trusted and untrusted parts.
2. App runs and creates enclave which is placed in trusted memory
3. Trusted function is called; code running inside enclave sees data
    * External access to data is denied.
4. Function returns; enclave data (sensitive) remains in trusted memory

```

Untrusted Part                     Trusted Part
of App                 call data   of App
 --------------------       __ --------------
|                    |     |  |              |
|  1. Create Enclave |     |--|              |
|                    |     |  |-> 3. Execute |
|                    |     |--|     .        |
|2. Call trusted func|---->|  |     .        |
|                    |     |--|     .        |
|                    |     |  |     .        |
|                    |      --|     v        |
|    etc             |<-------| 4. return    |
|                    |        |              |
|                    |         --------------
|                    |
|                    |
 --------------------
```

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
* Attack who can access the "environment" but privileged
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
* Variations of the meltdown vulnerability
    * Exploits **speculative execution**.
* Observations:
    * When processor encounters an exception it is not handled immediately and the processor continues to execute code speculatively.
    * mprotect() can be used to clear the "present" bit of a page.
        * a flag that indicates whether a page is currently in memory or not.
        * By clearing the "present" bit, the attacker can cause the legacy page table check to fail and allow the exploitation of the vulnerability.


## SGX Enclave
In an SGX enclave, the code and data are divided into two sections: the trusted and the untrusted sections.

### Trusted Section
The trusted section contains the code and data that are protected by the enclave and that have access to the sensitive data and functionality provided by the enclave. This section includes the main logic of the application, such as cryptographic operations, data processing, and any other functionality that needs to be protected from the untrusted host.

### Untrusted Section
The untrusted section contains the code and data that are not protected by the enclave and that have limited access to the sensitive data and functionality provided by the enclave. This section includes the code that communicates with the host, such as the EDL functions that are called by the host, the code that manages the enclave's lifecycle, such as the code that creates and destroys the enclave, and any other code that does not need to be protected by the enclave.

### Ecall and Ocall functions
The trusted and untrusted sections are separated by the use of the ecall and ocall functions.

* ecall (enclave call) functions are functions that are **executed inside the enclave and that can be called from the untrusted host**. These functions are defined in the untrusted section and are used to invoke the functionality provided by the enclave.

* ocall (outside call) functions are functions that are **executed outside the enclave and that can be called from the trusted section**. These functions are used to perform operations that are not available inside the enclave, such as accessing the file system or making network connections.

* The trusted section should include the main logic of the application and it should only perform the operations that need to be protected by the enclave

* The untrusted section should include the code that communicates with the host and the code that manages the enclave's lifecycle. It should also **include the EDL functions** that are called by the host.

#### Example

```edl
enclave {
    trusted {
        public void ecall_hello_world([in, string], const char *str);
    };

    untrusted {
        void ocall_print_string([in, string] const char *str);
    };
}
```


## Source

* https://www.youtube.com/watch?v=3MDIPAZnSTw
