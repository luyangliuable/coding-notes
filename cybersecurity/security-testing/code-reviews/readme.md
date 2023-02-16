# Source Code Review [#source-code-review]() [#white-box-testing]() [#data-flow-issues]() [#control-flow-issues]()

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Source Code Review [#source-code-review]() [#white-box-testing]() [#data-flow-issues]() [#control-flow-issues]()](#source-code-review-source-code-review-white-box-testing-data-flow-issues-control-flow-issues)
    - [Grey Box Testing [#grey-box-testing]()](#grey-box-testing-grey-box-testing)
        - [With a Tool](#with-a-tool)
            - [Vulnerability Covered by FlawFinder](#vulnerability-covered-by-flawfinder)
            - [Advanced Static Code Analyzers](#advanced-static-code-analyzers)

<!-- markdown-toc end -->


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
