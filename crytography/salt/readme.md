# Salt

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Salt](#salt)

<!-- markdown-toc end -->

## Purpose of Salt
* Same input but output different hashes.
* Often a random string

password-hash = one-way-hash-rounds(password || random-string)

## Attacks prevented by salt
* Rainbow table attack
  * Precomputed values for reversing cryptographic hashing
* Dictionary attack
  * Place candidate target hash in a dictionary.

