# Threat Modeling

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Threat Modeling](#threat-modeling)
    - [Stride Approach [#spoofing]() [#tampering]() [#repudiation]() [#information-disclosure]() [#denial-of-service]() [#elevation-of-Previlage]()](#stride-approach-spoofing-tampering-repudiation-information-disclosure-denial-of-service-elevation-of-previlage)
    - [Vulnerability Cycle [#exploit]()](#vulnerability-cycle-exploit)
        - [Attack Approach from STRIDE Point of View [network-user]() [snooping-user]() [colated-user]()](#attack-approach-from-stride-point-of-view-network-user-snooping-user-colated-user)
    - [Threat-driven Design](#threat-driven-design)
    - [Vulnerability Cycle](#vulnerability-cycle)

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

## Vulnerability Cycle [#exploit]()

### Attack Approach from STRIDE Point of View [#network-user]() [#snooping-user]() [#colated-user]()
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

Develop -> Get alert and install patch -> Discover vulnerability

## Threat-driven Design
* Network-only attackers implies messages traffic is safe.
  * No need to encrypt communication
  * This is what telnet remote login software assumed.
  
Develop -> Get alert and install patch -> Discover vulnerability

1. Someone uncovers and discloses a new vulnerability in a piece of software.
2. Hackers exploits the vulnerability and launch attacks agians the system,
3. Simulaneously, software security teams work on a fix.
4. If the vulnerability is serious, inform news/media.
5. Knee-jerk countermeasures
6. If The patch is ready, security team create/obtain, test, apply the patch
7. Security technicians check for similar vulnerabilties by examining related utilities and code fragments (as well as the new patch itself) 
## Mitgation is the Point of Threat Modelling

Mitigation is an area of expertise such as networking, databases or cryptopgraph.

* Best to get experts for assistance

## Validating Threat Models
* Check Diagram to see if it matches code
* Make sure all threats are enumerated
* STRIDE per element that touches a trust boundary
* Make sure QA has reviewed the model
