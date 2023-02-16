# Random Number Generator

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Random Number Generator](#random-number-generator)
    - [Use Cases](#use-cases)
    - [Good Properties [#randomness]() [#predictability]() [#complete]()](#good-properties-randomness-predictability-complete)
    - [Steps to Generating Pseudo Random Numbers [#pseudo-random-number-generator]()](#steps-to-generating-pseudo-random-numbers-pseudo-random-number-generator)
    - [Vulnerabilities](#vulnerabilities)
    - [Bad Seeds](#bad-seeds)

<!-- markdown-toc end -->

A random number generator is a function that allows the creation of random numbers of fixed length.

## Use Cases
* Generate hard to predict secret keys.
* Generating hard to predict random "salts"

## Good Properties [#randomness]() [#predictability]() [#complete]()
* Uniform distribution of randomness
  * Enough randomness usually 128 bits (2^128 possible combinations)
* Had to predict when looking at previous outputs.
  * Linear congruence generators meet the first property but fail the second one.
* Long and complete cycle.

## Steps to Generating Pseudo Random Numbers [#pseudo-random-number-generator]()
1. Need an initial short truly random input seed.
2. Use a deterministic function and output part of the state as a pseudorandom number.

## Vulnerabilities
* If the attacker guesses the seed attacker can get all input pseudorandom numbers used in application (e.g. All secret keys).
* If bad mathematical choices are used in PRNG, numbers can be predicted based on previous outputs.
* After first OS boot, most system parameters are highly predictable with initial default values.

## Bad Seeds
* From time since system booted
* Using process id.

## Hardware True Random Bit Solution [#hardware-true-random]() [#prng]()
Intel secure key allows RRAND and RDSEED functions in CPU instructions.
