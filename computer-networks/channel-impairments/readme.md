# Channel Impairments

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Channel Impairments](#channel-impairments)
    - [Types](#types)

<!-- markdown-toc end -->

## Types
* Noise
  * Random fluctuations in signal power.
* Interference
  * Additive or multiplication inclusion of other signals degrading signal quality.
* Distortion
  * Malformed shape in original waveform produced by transmission medium.
* Dispersion
  * Distortion induced by different pathlengths or propagation velocities seen by signal components.
* Fading
  * Time variant loss of signal due to destructive interference effects seen in some radiofrequencies.
* Loss
  * Reduction in signal levels arriving at the receiver.
## Choices
* Network designers typically have little control over what types of link equipment are available.
* network designers should understand the impact of these choices, given the noise behaviour of the channel which is to be used.
* This allows the network designer to choose the equipment best suited to the transmission environment.
* E.g. if the link channel is known to be prone to bursty interference, choosing equipment with modulation and error control strategies which are resistant is smarter than choices which are less resistant.
* Poor choices can especially cause problems with time sensitive network traffic, if frequent resend attempts occur.
* Smart designers will consider what tradeoffs are possible if any between performance and error rates in a system – tolerance for errors always depends on the application
