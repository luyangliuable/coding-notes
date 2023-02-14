# Principles in Secure Software Design

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Principles in Secure Software Design](#principles-in-secure-software-design)
    - [Learn from Mistakes](#learn-from-mistakes)
    - [Minimise Attack Surface](#minimise-attack-surface)
    - [Use Secure Defaults](#use-secure-defaults)
    - [Use Defence in Depth](#use-defence-in-depth)
    - [Use Least Privilege](#use-least-privilege)
    - [Separation of Previlage](#separation-of-previlage)
    - [Backward Compatibility is Dangerous](#backward-compatibility-is-dangerous)
    - [Assume External Systems/Entitles are Insecure](#assume-external-systemsentitles-are-insecure)
    - [Authorise after authentication](#authorise-after-authentication)
    - [Only Receive Control Instructions from Trusted Sources](#only-receive-control-instructions-from-trusted-sources)
    - [Ensure all Data is Validated](#ensure-all-data-is-validated)
    - [Ensure Crytopgrahy is used Correctly](#ensure-crytopgrahy-is-used-correctly)
    - [Identify all Sensitive Data and Handle appropriately](#identify-all-sensitive-data-and-handle-appropriately)
    - [Fail to secure mode](#fail-to-secure-mode)
    - [Security Features is not Software Security](#security-features-is-not-software-security)
    - [Do not depend on security via obsurity](#do-not-depend-on-security-via-obsurity)
    - [Time and State [#distributed-system]() [#clock-synchronisation]()](#time-and-state-distributed-system-clock-synchronisation)
    - [Error Handling [#repudiation]()](#error-handling-repudiation)
    - [High Code Quality [#reliability]()](#high-code-quality-reliability)
    - [Encapsulation](#encapsulation)
    - [Environment [#system-resources]() [#security-policy]()](#environment-system-resources-security-policy)

<!-- markdown-toc end -->

## Learn from Mistakes

## Minimise Attack Surface
* Use Trusted computing environment
* Minimise the number of network connections

## Use Secure Defaults
* SSH key or password on by default
* Password aging and complexity on my default.


## Use Defence in Depth 
* Plan for failure

## Use Least Privilege
* Use the least amount of previlage required for the task

## Separation of Previlage

## Backward Compatibility is Dangerous

## Assume External Systems/Entitles are Insecure

## Authorise after authentication

## Only Receive Control Instructions from Trusted Sources

## Ensure all Data is Validated

## Ensure Crytopgrahy is used Correctly

## Identify all Sensitive Data and Handle appropriately

## Fail to secure mode

* Don't disclose more than you have to
* Don't tell attack why the error have occurred (Repudiation)

## Security Features is not Software Security

## Do not depend on security via obsurity

## Time and State [#distributed-system]() [#clock-synchronisation]()
* Distributed computing is about time and space.
* Communicate state information must be shared

## Error Handling [#repudiation]()
* Handle errors correctly and safely
* Do not give too much information (Repudiation)
* Represents class of contract with the programmer

## High Code Quality [#reliability]()
* Ensure reliability

## Encapsulation
* Boundary between objects allows secure code
* Makes code simple

## Environment [#system-resources]() [#security-policy]()
* People managing and accessing the system resources such as programs
* Controlled with a well defined security policy.
