# Nyquist

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Nyquist](#nyquist)
    - [Sampling Theorem](#sampling-theorem)
    - [Nyquist Rate of a Channel](#nyquist-rate-of-a-channel)
    - [Multilevel Signaling](#multilevel-signaling)

<!-- markdown-toc end -->


## Sampling Theorem
Any waveform could be reconstructed accurately from a stream of samples but only if these samples were **taken at a frequency that was twice that of te highest frequency component of the original waveform**.

## Nyquist Rate of a Channel
* If the rate of signal transmission is **2B** then a signal with frequencies no greater than B is sufficient to carry the signal rate.

* Given a bandwith of B, the highest signal rate C can be carried is 2B.

C = 2B [bps, bits/s]

## Multilevel Signaling
* Increasing signal elements means different voltages represent more than one bits at a time.
  * This increases burden on receiver
  * Noise and other impairments limit the practical value of M.

C = 2Blog_2(M)
