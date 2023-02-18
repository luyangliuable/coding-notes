# Stream Ciphers

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Stream Ciphers](#stream-ciphers)
    - [Pros [#stream-ciper-advantages]() [#memory]() [#parallel]()](#pros-stream-ciper-advantages-memory-parallel)
    - [Cons [#key-reuse-vulnerability]() [#prng]()](#cons-key-reuse-vulnerability-prng)
    - [Rivest Cipher 4 (RC4)](#rivest-cipher-4-rc4)
    - [Security in WEP](#security-in-wep)
        - [Vulnerability](#vulnerability)
    - [Difference between WPA and WEP](#difference-between-wpa-and-wep)
    - [Reply attack](#reply-attack)

<!-- markdown-toc end -->

A stream cipher is a type of symmetric-key encryption algorithm that encrypts plaintext into ciphertext.

* **Pseudo random key** using pseudorandom bit generator (PRBG).
* PRGB is a **mathematical algorithm** that generates a sequence of bits, which are seemingly random, but are actually determined by an initial value called a seed.
* The key is typically the same for all messages encrypted using the stream cipher.
* The key is typically the seed for the pseudo random number generator.
```
 -----
| key |
 -----
 -----
|     \
|      \
|       \
|        \
|  PRBG   \
|          \
|           \
|            \
 -------------
 xor
 -------------
|   message   |
 -------------
 --------------------
 -------------
| ciphertext  |
 -------------
```

## Pros [#stream-ciper-advantages]() [#memory]() [#parallel]()
* It takes **less memory than block cipher algorithm**
    * Suited for **low resource environments** such as wireless communication services.
* **Can entrypt messages of any length** whereas block cipher can only encrypt fix sizes of plaintext sometimes needing padding.
* Suitable for plaintext of arbitrary length generated on the fly (e.g. media stream)
* Can process input elements in parallel.


## Cons [#key-reuse-vulnerability]() [#prng]()
* Prone to key-reuse vulnerability
* Relies heavily on the randomess and secrecy of random number generators
  * Good Randomness: Evenly distributed number
  * Good Secrecy: Hard to predict random number based on previous outputs


## Rivest Cipher 4 (RC4) [#symmetric-key-stream-cipher]()
* A symmetric key stream cipher that was widely used in many protocols and systems
* The algorithm was kept secret until it was leaked to the public in 1994.
* RC4 is a fast and simple algorithm that is suitable for software and hardware implementation.
* It has been found to have weaknesses in its **key schedule**, and its use is now discouraged in favor of more secure algorithms.


## Security in WEP  [#security]()
* IV || KEY -> RC4 -> KEYSTREAM = 0101
* PLAINTEXT = 1100
* CIPHERTEXT = KEYSTREAM xor PLAINTEXT = PLAINTEXT xor RC4(IV, KEY)

* One of the first security protocols for wireless networks, and it was widely adopted in the early days of wireless networking.
* It is easy to set up and use.

### Vulnerability [#key-reuse-vulnerability]()
* For P1 and P2, if P1 is know then P2 is also known. Where P1 and P2 are original text.
* C1 = P1 xor RC4(v, k)
* C1 = P2 xor RC4(v, k)
* C1 xor C2 = P1 xor P2 xor RC4(v, k) xor RC4(v, k) NOTE: RCR(v, k) cancels out

* IV (i.e. seed) by design is very short which is 24 bits so it is easy to brute force.
* 1500 byte per packet, 416 packets per second, 36 mil packets per day.


## Difference between WPA and WEP
| WEP                                    | WPA                                                       |
|:--------------------------------------:|:---------------------------------------------------------:|
| KEY is 40 bit and 24 bit random number | KEY is 256 bit                                            |
| Key management not provided            | Key management provided via 4 way handshaking mechanism   |
| No protection against reply attacks    | Sequence counter implemented against for reply protection |
| Possible on old hardware               | Possible to deploy only on current hardware infrastrature |

## Reply attack
* Network attack in which a valid data transmission is maliciously repeated or delayed.
* Attacker intercepts a data transmission, records it, and then retransmits it at a later time.
