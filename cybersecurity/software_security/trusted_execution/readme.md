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
    - [Sealed Storaged](#sealed-storaged)
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

## Sealed Storaged
Sealed storage in an enclave refers to a mechanism that allows data to be encrypted and stored within the enclave in a secure and tamper-proof manner. The data can be sealed, meaning that it is encrypted and bound to a specific set of attestation parameters, such as a specific enclave and platform, so that it can only be accessed when those parameters are met.

This sealed storage is used to store sensitive data such as keys, credentials, and other sensitive data that must be protected from disclosure. The data is encrypted with a key that is derived from the attestation parameters and is stored within the enclave.

Sealing the data makes it resistant to attacks that attempt to extract the data from the enclave, as the data is only accessible when the attestation parameters are met, and it would be difficult to extract the key used to encrypt the data.

Sealed storage can also be used to store an encrypted version of the data, which can be decrypted only inside the enclave. This ensures that the data is protected even if the attacker is able to extract the data from the enclave.

In summary, Sealed storage in an enclave is a mechanism that allows data to be encrypted and stored within the enclave in a secure and tamper-proof manner. The data is sealed, meaning that it is encrypted and bound to specific attestation parameters, such as a specific enclave and platform, so that it can only be accessed when those parameters are met. This makes the data resistant to extraction and disclosure.


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
