# Security Testing

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Security Testing](#security-testing)
    - [Three Levels of Security Testing [#risk-based-testing]() [#code-review]() [#penetration-testing]()](#three-levels-of-security-testing-risk-based-testing-code-review-penetration-testing)
    - [Difference between Security Testing and Functionality Testing](#difference-between-security-testing-and-functionality-testing)
    - [Security Testing Approaches](#security-testing-approaches)
        - [Risk Based Security Testing](#risk-based-security-testing)
        - [Penetrating Testing [#penetration-testing]() [#testing-for-negatives]()](#penetrating-testing-penetration-testing-testing-for-negatives)
    - [Analyses Testing Specific Types of Application](#analyses-testing-specific-types-of-application)
    - [Test Plan vs Tests vs Test Case Vs Scripts vs Test Runs [test-plan]()](#test-plan-vs-tests-vs-test-case-vs-scripts-vs-test-runs-test-plan)
    - [Jargon](#jargon)
    - [Develop Security Test Plans](#develop-security-test-plans)
        - [Roles and Responsibilities](#roles-and-responsibilities)

<!-- markdown-toc end -->


## Three Levels of Security Testing [#risk-based-testing]() [#code-review]() [#penetration-testing]()

Basically these are the common security Testing Approaches.

* Risk based security testing
* Code Review (White box testing)
  > see [white-box-testing](./code-reviews/readme.md)
  * Manual human peer review
  * With a tool, e.g. static code analysis
* Penetration Testing (Black box testing)
  > see [black-box-testing](./penetration-testing/readme.md)
  * Simulate adversarial behaviors to evaluate security
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


## Analyses Testing Specific Types of Application


## Test Plan vs Tests vs Test Case Vs Scripts vs Test Runs [test-plan]()
[#test]() [#test-case]() [#test-scripts]() [#test-runs]()


| Test Plan                                    | Tests                                    | Test Case                       | Test Script                                                  | Test Runs                                     |
|:--------------------------------------------:|:----------------------------------------:|:-------------------------------:|:------------------------------------------------------------:|:---------------------------------------------:|
| Includes Test Goals                          | High level description of what test does | Information on input and output | The script for giving a input and expecting a correct output | An execution containing output of a test case |
| Include overview of functionality of project |                                          |                                 |                                                              |                                               |
|                                              |                                          |                                 |                                                              |                                               |


## Jargon
audit - a review of a system in order to validate it.
    * Code auditing
    * Reviewing auditing logs


## Develop Security Test Plans

### Roles and Responsibilities
* Test Lead
  * Set up test process
  * Create/update test plans
* Test Designer
  * Set up security models
  * Create/Update test cases and test suites
* Test Engineer
  * Run test cases
  * Create/Update test results


```
Test Plan          Tests          Test Cases     Test scripts   Test runs
 -------------      t1  ------>  Input/output    run sy1ke5xa     9 4 <
| Test items  |
| 1. XXX      |     t2  ------>  Input/output    run do6ki7va     9 4 <
| 2. ZZZ      | ->
|             |     t3
|             |
 -------------      t4
```

