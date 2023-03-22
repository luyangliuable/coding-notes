# Interference

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Interference](#interference)
    - [Types](#types)
    - [Performance Impacts of Interference](#performance-impacts-of-interference)

<!-- markdown-toc end -->

## Types
* Electromagnetic interference (EMI)
  * When other unrelated signals interfere with message signal that is of the same signal bandwidth
* Crosstalk (Xtalk/XT)
  * Electrically coupled signals from an adjacent electrical cable often using the same type of waveform
* Co-Channel interference (CCI)
  * Crosstalk in a radiofrequency channel
* Adjacent-channel interference (ACI)
  * Interference by harmonics from a lower radiofrequency channel.
* Inter-symbol interference (ISI)
  * Power from preceding symbols corrupting the current symbol being decided upon by a receiver
  * ISI commonly arises with severe shape distortion in waveform
  * e.g. can arise from a dispersive transmission channel
  * Shaping pulses can reduce ISI.
  * The overlapping (constructive and destructive interference) of waves causes intersymbol interference.


## Performance Impacts of Interference
* Intersymbol interference can cause bit errors or multiple bit error called a burst.
* They are often quantified with the following measures
* Signal to interference ratio (S/I SIR)
    * ratio of signal power to interference power
* Carrier to interference ratio (C/I CIR)
    * Signal to noise raito for a radio frequency wireless channel
    * Where the power of the intering signal I ~= N in the channel.
* Signal to noise and interference ratio
    * Ratio of signal power to noise and interference power.
* Carrier to Noise and Interference Ratio (C/(N+I) / CNIR)
  * SNIR for a radio-frequency wireless channel.
