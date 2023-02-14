# Threat Modeling

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Threat Modeling](#threat-modeling)
    - [Stride Approach [#spoofing]() [#tampering]() [#repudiation]() [#information-disclosure]() [#denial-of-service]() [#elevation-of-Previlage]()](#stride-approach-spoofing-tampering-repudiation-information-disclosure-denial-of-service-elevation-of-previlage)
        - [Attack Approach from STRIDE Point of View [network-user]() [snooping-user]() [colated-user]()](#attack-approach-from-stride-point-of-view-network-user-snooping-user-colated-user)
    - [](#)

<!-- markdown-toc end -->


A process by which potential threats such as structural vulnerability or absence of safeguards can be identified and enumerated.

* It is realistic
* Considers attacker's capabilities

## Stride Approach [#spoofing]() [#tampering]() [#repudiation]() [#information-disclosure]() [#denial-of-service]() [#elevation-of-Previlage]()

* spoofing, tampering, repudiation, information-disclosure, denial-of-service, elevation-of-Previlage

* Break software security into separation components and analyze each component for threats to mitigate each of them.

| Threat                 | Security Property |
|:----------------------:|:-----------------:|
| Spoofing               | Authentication    |
| Tampering              | Integrity         |
| Repudiation            | Non-repudiation   |
| Information disclosure | Confidentiality   |
| Denial of Service      | Availability      |
| Elevation of Previlage | Authorization     |


### Attack Approach from STRIDE Point of View [network-user]() [snooping-user]() [colated-user]()
* Network user
  * Hack a server by connecting to the internet
  * SQL Injection, XSS, CSRF, buffer overrun payloads.
* Snooping User
  * Hack another user connected to the same WIFI network
  * Man in the middle attack
  * Session hijacking, denial of service
* Co-lated User
  * Hack another user by using malware installed on their machine
  * keylogger, read/write user's system, files or memory
  * Password theft

## Threat-driven Design
* Network-only attackers implies messages traffic is safe.
  * No need to encrypt communication
  * This is what telnet remote login software assumed.
  

