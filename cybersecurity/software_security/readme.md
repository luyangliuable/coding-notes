# Sofware Security

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Sofware Security Lecture One](#sofware-security-lecture-one)
    - [Tutorial Labs](#tutorial-labs)
    - [Learning Outcomes](#learning-outcomes)
    - [Undesired Behaviour](#undesired-behaviour)
    - [CIA Triad](#cia-triad)
    - [Where does software security fits in](#where-does-software-security-fits-in)
    - [Definitiion of some common term](#definitiion-of-some-common-term)
    - [Heartbleed](#heartbleed)
    - [Australian data breach laws](#australian-data-breach-laws)
    - [Why is sofware security a problem](#why-is-sofware-security-a-problem)
    - [Common Vulnerabilities](#common-vulnerabilities)
    - [Attacker: who are they?](#attacker-who-are-they)
    - [Secure Software](#secure-software)
        - [Dependability](#dependability)
        - [Reliability](#reliability)
        - [GAP](#gap)
        - [Considering Security](#considering-security)

<!-- markdown-toc end -->

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
  for (int i = 0; i < 10; i++) {
    printf("Hello world.\n");
  }
  return 0;
}
```

## Tutorial Labs
* Hands on activities discussions lecture notes recap.

## Learning Outcomes
* Demonstrate the importance of developing secure sofware.
* Elaborate on threads, vulnerabilities that need to be addresses during the development of secure and trusted sofware.
* Present secure an insecure coding implementation.
* Introduce new techniques and systems with advanced security features.
* Design software system that should be secure
* Write code that should be secure
* Review code that should be secure
* Test code that should be secure

## Undesired Behaviour
* Stealing information
    * Coporate secrets (product plan, source code, IP, ....)
    * Personal info. (health record)
* Modifying information or functionality
    * Destroying records (accounts)
    * Installing unwanted sofware (spyware)
* Denying access (denial of service, ransomware)
    * Unable to access a website, database, cloud drive

## CIA Triad

* Confidentiality: Information is not made avalaible or disclosed to unauthorised invididuals entitity or processes
* Integrity: SOfware maintains and assures the accuracy and completeness of data over its entire life cycle.
* Availability: info. must be available when it is needed.

## Where does software security fits in
* S/W runs on o/s and abides by its security rules
* S/W that uses DB must connect to and interact with the DB.
* TODO


## Definitiion of some common term
* Threat
    * A potential dangerous event that if occurs breach a desirable security property of a system.

* Attacker
    * A malicious entity with a motive to realsie a threat on a system. (i.e. attack the system) e.g. a bank theft criminal organisation.

* Vulnerability
    * A weakness in a system is exploitable by an attack realise a threat. (e.g. An online bank server storing user passwords in a publicly assessible server)

## Heartbleed
* Buffer overflow buf in OpenSSL crytography library
* Allows attacker to read server private keys.
* 17 of "secure" internet servers worldwide estimated to be vulnerable (500 milion servers!!!)
* Simple patch but huge cost of patching all these servers.

## Australian data breach laws
* Australian parliament enacted the Privacy amendedment.
* TODO

## Why is sofware security a problem
* Many vulnerabilities are being exploited
    * Strong incentives for finding and exploiting vulnerabilities
    * Finanicial (black market for vulnerabilities/malware)
    * Political/Esponiage (cyber warfare/intelligence)

* Large number of software vulnerabilities are being discovered
    * Made worse by increasing software
      * Complexity (millions of code lines)
      * Connectivity (more potential threats, zero-day vulnerabilities)
      * Extendabiltiy (online updates)

## Common Vulnerabilities
* Implementation vulnerability
  * Incorrect code
  * Easy to spot in code and detectable for automatic vulnerability scanning tools

* Design vulnerability
    * Flaw in logic/protocol of the software (incorrect use of crytography, unauthorised access to shared resources.)
    * Detectable at the design state from design specs.
    * Not easy to automate detection ("correct" implementation)
    * Sometimes a bad tradeofff of usability over security

## Attacker: who are they?
* Criminals seeking gain or hiding criminal activities.
* Insiders (employees) seeking revenge or financial gain.
* Hackers driven by intellectual challenges
* Operators./users who make mistakes
* Organised terrorist groups or nation states trying to influence national policy
* Foreign agents seeking info. for economic political or military purposes.

## Secure Software
* Secure software continues to function correctly under malicious attacks - Gary MaGraw
* When a program is executed, **the state of a number of objects may change**.
* A program is said to be secure if **new states of the objects modified by the program are collective in an acceptable (safe) state**.
* Saftety: **a good (acceptable) state can only be transformed into another good state**, even in the presence of adversarial (intentionally malicious) user behaviour,

### Dependability
* TODO

### Reliability
* TODO


### GAP
* Most technologists acknowlefge this undertaking importance... TODO

### Considering Security
* The adversary will actively attempt to find vulnerabilities in rare future interations and edge cases.
* For a typical user, (accidentally) finding a bug will result in a crash.
* An adversary will work to find a bug and exploit it to achieve their goals.

