# SGX

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [SGX](#sgx)
    - [SGX Threat Model](#sgx-threat-model)
    - [SGX Security Services [#trusted-computing-enabler]() [#trusted-execution-environment]()](#sgx-security-services-trusted-computing-enabler-trusted-execution-environment)
        - [Features of SGX Trusted Computing Enabler](#features-of-sgx-trusted-computing-enabler)
    - [SGX + Secure Boot [#secure-boot]()](#sgx--secure-boot-secure-boot)
    - [Employ basic programming model of SGX](#employ-basic-programming-model-of-sgx)
    - [SGX Enclave](#sgx-enclave)
        - [Trusted Section](#trusted-section)
        - [Untrusted Section](#untrusted-section)
        - [Ecall and Ocall functions](#ecall-and-ocall-functions)
            - [Example](#example)
    - [Source](#source)

<!-- markdown-toc end -->

## SGX Threat Model
* Cloud provider's software (e.g. web, cloud and remote access services) are malicious,
  * modifying the OS to install malware.
  * modifying the firmware to disable security features.
  * **SGX guarantees that the code/data inside the enclave cannot be accessed by an attacker, even if the attacker has gained full control of the system's firmware, BIOS, and operating system**.

* All hardware besides the CPU is untrusted
    * An attacker could install a hardware **keylogger** on via I/O, or could use a **hardware-based rootkit** to gain persistent access to the system.
    * **If either CPU, firmware, BIOS, or operating system is compromised the security guarantees provided by SGX can be bypassed**.


## SGX Security Services [#trusted-computing-enabler]() [#trusted-execution-environment]()
* Trusted computing enabler
    * secure computer on someone else's computer
    * ability to provide **trusted execution environment** (TEE) enabling deployment of secure applications/services
      * TEE is a secure area of the main processor

### Features of SGX Trusted Computing Enabler
* Confidentiality: code and data inside an enclave cannot be accessed or modified by an attacker, even if the attacker has gained full control of the system's firmware, BIOS, and operating system.

* Integrity: SGX guarantees that the code and data inside an enclave cannot be tampered with or modified by an attacker, even if the attacker has gained full control of the system's firmware, BIOS, and operating system.

* Remote Attestation: SGX guarantees that a **remote party can verify the identity and configuration of an enclave, and can confirm that the code and data inside the enclave have not been tampered with or modified**.

* Key Protection: SGX guarantees that the keys used to encrypt and decrypt data inside the enclave are protected from attackers.


## SGX + Secure Boot [#secure-boot]()
By using Secure Boot and SGX together, the system can ensure that it is running only authorized software during the boot process and that sensitive data and operations are protected by SGX. 

* Ensure that the firmware and OS are not compromised before SGX starts.

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


## SGX Enclave
In an SGX enclave, the code and data are divided into two sections: the trusted and the untrusted sections.

### Trusted Section
* Contains the code and data that are protected by the enclave and that have **access to the sensitive data and functionality provided by the enclave**.
* Section includes the **main logic of the application**, such as:
    * Cryptographic operations
    * Data processing
    * Any other functionality that needs to be protected from the untrusted host.

### Untrusted Section
Contains the code and data that are not protected by the enclave and that have limited access to the sensitive data and functionality provided by the enclave.
* This section includes the code that communicates with the host, such as:
    * The EDL functions that are called by the host
    * Code that manages the enclave's lifecycle, such as the code that creates and destroys the enclave
    * Any other code that does not need to be protected by the enclave.

### Ecall and Ocall functions
The trusted and untrusted sections are separated by the use of the ecall and ocall functions.

* ecall
  * enclave call
  * functions that are **executed inside the enclave and that can be called from the untrusted host**.
  * These functions are defined in the untrusted section and are used to invoke the functionality provided by the enclave.

* ocall
  * outside call
  * functions that are **executed outside the enclave and that can be called from the trusted section**.
  * These functions are used to perform operations that are not available inside the enclave, such as accessing the file system or making network connections.
  * Perform privileged or I/O operations in an enclave, e.g., system calls, file I/O

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
