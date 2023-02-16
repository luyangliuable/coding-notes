# Advanced Encryption Standard

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Advanced Encryption Standard](#advanced-encryption-standard)
    - [Electronic Code Book (ECB)](#electronic-code-book-ecb)
        - [Pros](#pros)
        - [Cons](#cons)
    - [Cipher Block Chaining (CBC)](#cipher-block-chaining-cbc)
        - [Pros [#cascading-effect]() [#pattern]()](#pros-cascading-effect-pattern)
        - [Cons](#cons-1)

<!-- markdown-toc end -->

AES is a widely adopted block encryption algorithm.

## Electronic Code Book (ECB)
* Simplest
* C[i] = key xor E(P[i])

### Pros
* Can run in parallel as encryption blocks are independent.

### Cons
* The original text in file is often retained after encrypting so it is bad for images.

## Cipher Block Chaining (CBC) 
C[i] = E(C[i-1] xor P[i])
C[0] = key xor E(P[i])

### Pros [#cascading-effect]() [#pattern]()
* Does not retain pattern due to cascading effect. 

### Cons
* Blocks must be encrypted sequentially.
* Susceptible to padding oracle attack.
