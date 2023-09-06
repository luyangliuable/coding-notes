# Summary Template for Systematic Mapping Study on MLOps

## Paper Title: Bridging the Gap Between Java and Python in Mobile Software Development to Enable MLOps

## Authors: [Names of the Authors]

## Publication Year: [Year of Publication]

## Source/Conference/Journal: [Source of the Paper]
 
## Abstract/Introduction Summary:
[Brief summary of the paper's abstract or introduction, highlighting the main focus and purpose of the study.]
Main Focus: The increasing significance of Machine Learning (ML) engineers in mobile development, especially as AI components become critical for mobile applications. The study emphasizes the challenges ML engineers face due to the lack of MLOps tools designed for mobile platforms.

Purpose of Study:

Highlight the increasing role of ML engineers in mobile development.
Address the technological gap in tooling support for ML engineers on mobile platforms, particularly around the integration of Python, a dominant language in data science, with mobile OS like Android.
Propose an extensible architecture for rapidly developing data analytics components on the Android platform, with a clear separation of concerns between app developers and ML engineers.
Provide a proof of concept implementation of the proposed architecture.
Key Points:

Significance of ML in Mobile Development: With AI components becoming essential for business-critical apps, ML engineers play a pivotal role, focusing on data lifecycle aspects, while app developers handle the application lifecycle.

Technological Trends:

Smartphones as IoT Gateways: Smartphones have become crucial for vertical IoT communication, serving as universal gateways. This is driven by the proliferation of sensor technology in various sectors.
AI on the Edge: Due to challenges like user privacy, network congestion, and cloud costs, there's a trend towards pushing AI capabilities to the edge.
Adoption of Agile Development Practices: DevOps and MLOps have emerged as essential practices. While DevOps enhances collaboration among developers, testers, and IT operations, MLOps focuses on the reliable and efficient deployment of ML models.
Technological Gap: Despite several frameworks available for mobile development, there's a lack of tools tailored for ML engineers on mobile platforms. The integration of Python with native code on Android OS is limited.

Proposed Solution: An extensible architecture for developing data analytics components on Android. This architecture promotes a clear distinction between app developers and ML engineers, allowing the latter to independently develop and manage data processing modules. The architecture leverages a plug-in pattern, ensuring extensibility, flexibility, and customization.

Contributions:

Identification of the existing technological gap.
A conceptual plug-in architecture for deploying and running Python modules on Android.
A proof of concept for fatigue detection using time-series sensor data from wearable fitness trackers.
The paper is structured to cover research context, conceptual architecture, proof of concept, results, and future work directions.

RQ1: Motivation and Benefits of Using MLOps:

## Motivation:
[Key motivation 1 for using MLOps as highlighted in the paper]
[Key motivation 2...]
[...]

## Benefits:
[Key benefit 1 of using MLOps as mentioned in the paper]
[Key benefit 2...]
[...]
RQ2: Approaches and Tools for MLOps:
* The cross-platform frameworks BeeWare and Kivy
  * Used to package Python code as Android apps with support for user interfaces and access to most Android services and hardware interfaces

## Approaches:
RQ3: Challenges in Operationalizing MLOps:
* Plug-in Architecture
  * relies on the principle of allowing adding features as plug-ins to the core application, providing exten-sibility, flexibility, customisation, and isolation of application features. 
* Data ingestion
* Service Provider Interface 
* Chaquopy for Bridging Java and Python

## Challenges:
RQ4: Integrating Responsible AI Principles into MLOps Pipelines:

* Limited python support on mobile dev force developers to use native programming languages
  * Native languages are not well-suited for ML-oriented tasks due to complexity and rigidity

Strategies/Methods:
[Strategy/Method 1 to integrate Responsible AI into MLOps]
[Strategy/Method 2...]
[...]

Challenges/Concerns:
[Challenge/Concern 1 in integrating Responsible AI into MLOps]
[Challenge/Concern 2...]
[...]
Conclusion and Future Directions:
[A concise summary of the paper's conclusion and insights on potential future research directions, if provided.]

## Reviewer's Comments: [Any subjective notes, comments, or observations you might have after reading and summarizing the paper.]
Not really related to MLops, only thing is it tells you a possible way to use plug in artitecture so everything can be python.
