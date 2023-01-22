# Intel Software Guard Extensions

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Intel Software Guard Extensions](#intel-software-guard-extensions)
    - [Notion of Trust](#notion-of-trust)
        - [Establishing Trust](#establishing-trust)
    - [Hardware Assisted Trust](#hardware-assisted-trust)
        - [Examples](#examples)
    - [Trusted computing Base (TCB)](#trusted-computing-base-tcb)
    - [Trusted Execution and Isolation](#trusted-execution-and-isolation)
    - [Threat Model](#threat-model)
    - [SGX Security Services](#sgx-security-services)
    - [Employ basic programming model of SGX](#employ-basic-programming-model-of-sgx)
    - [Side-channel Attacks Methods](#side-channel-attacks-methods)
    - [SGX Enclave](#sgx-enclave)
        - [Trusted Section](#trusted-section)
        - [Untrusted Section](#untrusted-section)
        - [Ecall and Ocall functions](#ecall-and-ocall-functions)
            - [Example](#example)
    - [Source](#source)

<!-- markdown-toc end -->

## Notion of Trust
*  Confidence that A system or component can be relied
* The realisation of trust of entity B from entity A is based on the notion B will always behave **honourably, reliably and securely** under the right circumstances.

* Trust tries to formulate a good-faith relationship between computing machines as well as between their users.

* Involves user and computing device.
  * Trust is:
    * Not a binary state, it can vary in degree and can change over time.
    * Multi-dimensional concept,
        * different trust dimensions can be considered such as trust in the identity, trust in the technology, trust in the organization, and trust in the security controls and practices.

### Establishing Trust
Trust can be established through a combination of factors such as:

* Trust Verification Mechanisms
  * **Authentication**: The process of verifying the identity of a user or system
  * **Access controls**: Restricting access to resources to authorized users
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
  * SGX guarantees that the code/data inside the enclave cannot be accessed by an attacker, even if the attacker has gained full control of the system's firmware, BIOS, and operating system.


## SGX Security Services

## Employ basic programming model of SGX

## Side-channel Attacks Methods


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
