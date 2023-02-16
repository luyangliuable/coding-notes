# Linux Shadow Function

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Linux Shadow Function](#linux-shadow-function)
    - [Example](#example)

<!-- markdown-toc end -->


* Has three parts:
  * Algorithm used
  * Salt
  * Password hash

* Salt and password hash are encoded into readable characters

* It uses multiple rounds of hash function to slow down brute-force attacks.

## Example
```
seed:$6$he6mi8ve$du4fa3szi9my3fyu/:17372:0:99999:7:::
```

* 6 means SHA512 which is the algorithm
* he6mi8ve is the seed
* du4fa3szi9my3fyu is the password hash
