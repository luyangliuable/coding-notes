# Bit Error Rate

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Bit Error Rate](#bit-error-rate)
    - [Power Budget and Quality of Service](#power-budget-and-quality-of-service)

<!-- markdown-toc end -->

## Power Budget and Quality of Service

* Power budgets determines the ratio of input signal power to the receiver, relative to the power levels of unwanted impairments, such as receiver noise, interference and crosstalk.

* If the power budget makes inadequate allowances for impairments, the SNR, Signal/Interference and Signal/Crosstalk ratios, for any given modulation scheme, will yield unacceptably high BERs.

* In a multi-hop network, the end-to-end BER, without error control, is the sum of BERs across all N hops in the network.

* Even one underperforming link can compromise a route with many hops along with it.


* In a multi-hop network, the end-to-end BER, without error control will be determined by the sum of BERs across all N hops in the network.

BER\_multi-hop = SUM(M, i=0, BER_i)

## BER vs Packet Loss Rate
* Packet Loss rate is determined by the BER of the link
  * Or does not doesn't use FEC capabilities.
* BER is determined by SNR, Signal/Interference and Signal/Crosstalk ratio, for any given modulation scheme.
* Quality of service is critically on packet loss rates over links between routers in a network.
* Bad choices in link design at layer 1,2 can significantly impact performance observed at layers 3+4 in a network.
