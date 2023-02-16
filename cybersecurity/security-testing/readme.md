# Security Testing

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Security Testing](#security-testing)
    - [Difference between Security Testing and Functionality Testing](#difference-between-security-testing-and-functionality-testing)
    - [Security Testing Approaches](#security-testing-approaches)
        - [Risk Based Security Testing](#risk-based-security-testing)
        - [Source Code Review (i.e. white-box testing)](#source-code-review-ie-white-box-testing)
        - [With a Tool](#with-a-tool)
            - [Vulnerability Covered by FlawFinder](#vulnerability-covered-by-flawfinder)
            - [Advanced Static Code Analyzers](#advanced-static-code-analyzers)
        - [Penetrating Testing](#penetrating-testing)
    - [Using Testing Tools](#using-testing-tools)
    - [Analyses Testing Specific Types of Application](#analyses-testing-specific-types-of-application)
    - [Develop Security Test Plans](#develop-security-test-plans)

<!-- markdown-toc end -->


## Three Levels of Security Testing [#risk-based-testing]() [#code-review]() [#penetration-testing]()
* Risk based testing
* Code Review (White box testing)
  * With a tool
  * Manually
* Penetration Testing (Black box testing)
  * Exploratory Manual
  * Systematic Manual
  * Fuzzing
    * Random malformed inputs pumped into entry points to help uncover faults
    * Saves time and it is automated

## Difference between Security Testing and Functionality Testing
| Security Testing                                            | Functionality Testing                 |
|:-----------------------------------------------------------:|:-------------------------------------:|
| Can be corrected without being bug free                     | Can be corrected without being secure |
| Addresses software failures that have security implications | Only software failures                |
| Uses penetration testing                                    | Unit tests, integration tests etc     |


## Security Testing Approaches
* Risk based security testing
* "White-box" testing
    > see [white-box-testing](./coding-notes/cybersecurity/penetrationg-testing/white-box-testing/readme.md)
    * Manual human peer review
    * With a tool, e.g. static code analysis
* Penetration Testing
    * "Black-box" testing
    * Fuzzy testing
* Simulate adversarial behaviors to evaluate security

### Risk Based Security Testing
* Identify threats using Threat Modeling.
    * Microsoft Security Development Lifecycle (SDL) Threat Modeling.
* Quantify the risk associated for each threat 
    * [threat impact]/[ease of exploiting the threat]
* Priorities the risks for mitigation: **decompose applications**, **identify component interfaces**, and then identify vulnerability and risks.
* Well-known approach.
* Create Data Flow Diagram (DFD) 
    * Identify the security breach boundaries.
* Identify types of threat. 
* Check whether code for any of the possible mitigation method is incorporated.


### Penetrating Testing [#penetration-testing]() [#testing-for-negatives]()
Search for application weaknesses through simulating malicious attacks.
> TODO See [penetration-testing](./penetration-testing/readme.md)

* Point of view of an attacker
* Testing for positives is functional testing
* Testing for negatives is penetration testing

### Source Code Review [#source-code-review]() [#white-box-testing]() [#data-flow-issues]() [#control-flow-issues]()
* Code walk through - also known as "white box testing"
* Look for bad practices of programming
    * Structural issues such as hard coded key/password.
    * Look for leaking information
    * Data flow issues (lack of proper data validation)
    * Control flow issues 
        * unreleased/unclosed resource streams
        * denial of service
        * matching lock/unlock operations
* Source code review concentrates on the language based security.
* Require strong experience with both software development and security.
* Should be performed by someone outside the development team.
* Deliverable requirement
    * A report for developers to fix the identified vulnerability
    * Executive summary
    * List of technical issues identified
    * Glossary, appendices, indexes and etc.
    
## Grey Box Testing [#grey-box-testing]()
Combination of source code review and penetration testing.

### With a Tool
* Less time consuming
* A tool can store more common vulnerabilities a human can remember.
* Humans better at code understanding/insight than manual search for a pattern.
* Simple (often free) search-based tools.
    * Examples: FlawFinder, RATS, ITS4, ...
    * Search source file for "dangerous functions" known to cause common vulnerabilities, e.g. strcpy(), gets() for buffer overflows.
    * Produces list of "hits" for buffer overflows.
* Better than pure search.
    * Ignores commented code.
    * Risk ranking
    * But little attempt to analyses relationships within code (i.e. static analysis).

* Static code analyzers
  * Flawfinder, Fortify
  * Input: Code
  * Search the code for **common code vulnerabilities**.
  * Output: Report file containing potential vulnerabilities
  * Goals
    * Find common bugs quickly
    * Allow developers to focus on parts of code likely to be risky
  * Limitations
    * Cannot find design level vulnerabilities
    * Cannot make a judgment of importance of a found vulnerability
    * Only detect vulnerabilities in tools "rule database"
    * Suffer from errors
      * False positive
        * Example: Loss of precision
        ```c
        short s = 0;
        int i = s;
        short r = i;
        ```
      * False negative
        * New zero-day vulnerability not included in the "**rule database**" (patterns) * Runtime environment is unknown * Call external APIs * Other factors, e.g. scheduling of multiple threads

#### Vulnerability Covered by FlawFinder
* Improper **input validation**
* Improper Limitation of a pathname to a **restricted directory**. (i.e. Path traversal)
* Allows for **OS Command Injection**.
* Improper **restriction of operation within bounds of a memory buffer**.
* Buffer copy without checking size of input (i.e. classic buffer overflow)
* Buffer Over-read
* Uncontrolled Format String
* Execution with unnecessary Previlage
* Use of a broken of risky cryptographic algorithm
* Concurrent execution of using shared resource with improper synchronisation (i.e. race condition)
* Insecure temporary file
* Use of potentially dangerous function

#### Advanced Static Code Analyzers
* Reduce false positive rate with **deeper code analysis**.
  * **Data Flow Analysis**: Identifies user-controlled input that is involved in a dangerous operation (e.g. longer user input data copied into fixed size buffer.)
  * **Control Flow Analysis**: Identified dangerous operation sequences (e.g. a file is not configured properly before use)


## Analyses Testing Specific Types of Application

## Develop Security Test Plans
