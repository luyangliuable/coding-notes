# Padding Oracle Attack

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Padding Oracle Attack](#padding-oracle-attack)
    - [Attack initialization](#attack-initialization)
    - [Countermeasures](#countermeasures)

<!-- markdown-toc end -->

* SSLv3.0 is susceptible to padding oracle attack
* It is a weakness of CBC mode.

## Attack initialization
1. Client handshakes and sends client_hello
2. Attacker intercepts via MITM attack and impersonates server until client agrees to downgrade to v3.0


## Countermeasures
* Remove server response
* Use AES GCM model authentication encryption.
  * Ensure cipher text is not modified during transimsison
