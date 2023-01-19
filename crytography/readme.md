# Crytography
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Crytography](#crytography)
    - [One-way Hash Functions](#one-way-hash-functions)
        - [Example](#example)
    - [Security Properties](#security-properties)
    - [MD One-Way Hash Functions](#md-one-way-hash-functions)
    - [Password Verification](#password-verification)
        - [Need for:](#need-for)
    - [Commands](#commands)

<!-- markdown-toc end -->

## One-way Hash Functions
* Essential **building block** in crytography

### Example
* Password Authentication
* Integrity Preservation
* Blockchain

## Security Properties
* Difference from Hash function
    * Hash function: maps arbitrary size data to data of fixed size.
    * Example: f(x) = x mod 1000

* One-way hash function properties
    * hash(m) = h, difficult to find m
    * **Collision resistant**: Difficult to find m1 and m2 s.t. hash(m1) = hash(m2)

## MD One-Way Hash Functions
* MD stands for **message digest**
    * Includes **MD2, MD4, MD5, MD6**


## Password Verification
    * Cannot store the secrets in their plain text


### Need for:
    * Password storage where nobody can read.

## Commands
seed:9D,q^S)Z9tnxW[.%814U:[eKqmV~LD$^{f~.]wDlduZPGiL(%4SHH_)Im6z]/}Yy)~9[5^DUU+<XtQTzg$


Deterministic random number generator

## Symmetric Crytosystem 
* Uses the same key for **encryption and decryption**
* Encrypting and decryption should be efficient

### Issues
    * What is a good symmetric encryption scheme?
    * What is the complexity of encryption/descryption
    * What is the size of the cyphertext, relative to the plaintext.

## Stream Cipher

### WEP

### Insecurity of WEP

### Security Analysis of WEP

## Key Reuse Vulnerability


## Block Cipher

### Advanced AES Standard


#### Incorrect use of Block Cipher

#### AES Rounds

#### Modes of Operation

### Strength and Weakness of Electronic Code Book ECBs

### Cipher Block Chaining

#### Strength and Weakness of Cipher Block Chaining

#### Padding Oracle Attack (POODLE)
