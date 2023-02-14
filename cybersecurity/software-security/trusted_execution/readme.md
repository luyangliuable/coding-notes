# Intel Software Guard Extensions

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Intel Software Guard Extensions](#intel-software-guard-extensions)
    - [Hardware Assisted Trust](#hardware-assisted-trust)
    - [Isolation in Trusted Execution](#isolation-in-trusted-execution)
    - [Sealed Storaged](#sealed-storaged)
    - [Remote Attestation](#remote-attestation)
    - [Side-channel Attacks Methods](#side-channel-attacks-methods)
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


## Isolation in Trusted Execution [#attack-surface]() [#computation]() [#communication]()
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
    * The TCB is implemented at a low level of the system such as **firmware or kernel**.
    * Provide an additional layer of protection.
    * TCB services example incl. secure boot, secure enclaves


## Sealed Storaged
Sealed storage in an enclave refers to a mechanism that allows data to be **encrypted** and stored within the enclave in a secure and tamper-proof manner. The data can be sealed, meaning that it is encrypted and bound to a specific set of **attestation parameters**, such as a **specific enclave** and platform, so that it can only be accessed when those parameters are met.

This sealed storage is used to store sensitive data such as **keys**, **credentials**, and other sensitive data that must be protected from disclosure. The data is encrypted with a key that is derived from the attestation parameters and is stored within the enclave.

Sealing the data makes it resistant to attacks that attempt to extract the data from the enclave, as the data is only accessible when the attestation parameters are met, and it would be difficult to extract the key used to encrypt the data.

Sealed storage can also be used to store an encrypted version of the data, which can be decrypted only inside the enclave. This ensures that the data is protected even if the attacker is able to extract the data from the enclave.

This makes the data resistant to extraction and disclosure.

## Remote Attestation
* Guarantees that a remote party can verify the identity and configuration of an enclave.
    * Proof an enclave runs on a **given cpu** and a given **security level**.
    * Confirm that the **code and data inside the enclave has not been tampered or modified**.

* SGX attestation parameters:
    * **MRENCLAVE**: Enclave Unique ID. Crytographic hash of enclave code and data.
    * **MRSIGNER**: Platform Unique ID. Crytographic hash of signing entity's public key.
    * **ISVPRODID**: Enclave Product ID Unique Value. Assigned my intel or ISV (independent software vendor)
    * **ISVSVN**: A unique value that represents the security version of the enclave.

* Verification
  * The enclaved code generates a quote that includes a digest of the code and data inside the enclave, which is then signed by the enclave's private key.
  * The verifier uses the enclave's public key to verify the quote.
  * Example: Verify enclave integrity and code/data has not been tampered with

## Side-channel Attacks Methods
> See [side-channel-attack-methods](../vulnerabilities/side-channel-attack/readme.md) 

A type of attack that aims to extract sensitive information from a system by **analysing low-level information** such as **power consumption**, **electromagnetic emissions**, or **timing**. These attacks can be used to extract sensitive information such as encryption keys or other secret data.

  ```c
  #include <sgx_urts.h>
  #include <sgx_uae_service.h>

  int main() {
      sgx_enclave_id_t eid;
      sgx_status_t ret;

      // Initialize the enclave
      ret = sgx_create_enclave(ENCLAVE_FILENAME, SGX_DEBUG_FLAG, NULL, NULL, &eid, NULL);

      if (ret != SGX_SUCCESS) {
          // Handle error
      }

      // Prepare the attestation report
      sgx_report_t report;

      ret = sgx_create_report(eid, NULL, &report);
      if (ret != SGX_SUCCESS) {
          // Handle error
      }

      // Retrieve the quote from the report
      sgx_quote_t* quote;
      uint32_t quote_size;

      ret = sgx_get_quote(&report, SGX_LINKABLE_SIGNATURE, NULL, 0, quote, &quote_size);

      // Send the quote to the verifier for validation
      // ...

      // Destroy the enclave
      sgx_destroy_enclave(eid);

      return 0;
  }
  ```



