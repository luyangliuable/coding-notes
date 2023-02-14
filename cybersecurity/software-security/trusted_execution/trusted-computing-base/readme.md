# Trusted Computing Base

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Trusted Computing Base](#trusted-computing-base)
    - [Trusted computing Base (TCB) [#previlage]() [#security-policy-enforcement]() [#security-compliance]()](#trusted-computing-base-tcb-previlage-security-policy-enforcement-security-compliance)
        - [Examples (that are also TCBs) [#secure-boot]() [#secure-storage]() [#secure-enclaves]()](#examples-that-are-also-tcbs-secure-boot-secure-storage-secure-enclaves)

<!-- markdown-toc end -->


## Trusted computing Base (TCB) [#previlage]() [#security-policy-enforcement]() [#security-compliance]()
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

### Examples (that are also TCBs) [#secure-boot]() [#secure-storage]() [#secure-enclaves]()
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
