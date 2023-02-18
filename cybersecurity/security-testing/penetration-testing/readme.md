# Penetrating Testing [#penetration-testing]() [#testing-for-negatives]()

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Penetrating Testing [#penetration-testing]() [#testing-for-negatives]()](#penetrating-testing-penetration-testing-testing-for-negatives)
    - [Enumerating Possible Actions [#exploratory-testing]() [#systematic-testing]() [#fuzzing]()](#enumerating-possible-actions-exploratory-testing-systematic-testing-fuzzing)
        - [Exploratory (manual) [#pentesting-tools]()](#exploratory-manual-pentesting-tools)
        - [Systematic (manual)](#systematic-manual)
        - [Fuzzing - Automated [#malformed-data]()](#fuzzing---automated-malformed-data)

<!-- markdown-toc end -->


Search for application weaknesses through simulating malicious attacks.

* Point of view of an attacker
* Testing for positives is functional testing
* Testing for negatives is penetration testing


## Enumerating Possible Actions [#exploratory-testing]() [#systematic-testing]() [#fuzzing]()

### Exploratory (manual) [#pentesting-tools]()
* Black box testing with the help of tools.
* Guided by user's instinct and experience.

### Systematic (manual)
* Black box testing with predetermined security test plan developed from requirements.


### Fuzzing - Automated [#malformed-data]()
Submit malformed, malicious and random data to a system's entry point to help uncover faults.

* With the help of tools.
* Testing by giving wide range of random inputs.
* Helps to reduce repetiveness of doing testing.

Use combinations of "known-to-be-dangerous" values (known as fuzzy vectors) and random data
> See [data-input-cases](../data-input-cases/readme.md)

* for integers: zero, possibly negative or very big numbers (e.g., -1,0,0x100,0x1000,0x7ffffffe,0x7fffffff)
* for chars: escaped, interpretable characters / instructions (e.g., %s%p%x%d,. 1024d, %.2049d, %p%p%p%p, %x%x%x%x, %99999999999s)

* Tools: google AFL, Microsoft's SDL MiniFuzz File Fuzzer

## Resources
[5 pen testing rules of engagement: What to consider while performing Penetration testing](https://hub.packtpub.com/penetration-testing-rules-of-engagement/) 
