# Summary Template for Systematic Mapping Study on MLOps

## Paper Title: Sustainable MLOps: Trends and Challenges

## Authors: Damian A. Tamburri

## Publication Year: 2021

## Source/Conference/Journal: https://ieeexplore.ieee.org/document/9356947
 
## Abstract/Introduction Summary:
[Brief summary of the paper's abstract or introduction, highlighting the main focus and purpose of the study.]
Main Focus and Purpose:

Investigate the sustainability of Machine-Learning Operations (MLOps).
Propose a research roadmap for the sustainability of MLOps.
Key Insights:

Google Trends identifies MLOps as a significantly rising trend.
Operationally, Machine-Learning software behaves like other software, processing input to produce output.
However, in continuous operation (DataOps pipeline), the workings of Machine-Learning software differ greatly.
MLOps requires the orchestration of several functions:
Data ingestion/transport.
Data transformation.
Continuous ML (re-)training.
Continuous ML (re-)deployment.
Output production/presentation (e.g., business intelligence).
The total orchestration of these functions is often called AI Software.
Integrating MLOps with Cloud engineering technologies, like Function-as-a-Service, makes operations more efficient but architecturally complex.
Observations:

Numerous tools (e.g., Apache Airflow, KubeFlow, Google Cloud AutoML) exist to support the lifecycle of ML components within AI Software.
As AI software operations grow in complexity, their sustainability reduces.
Complexity is due to:
Software architecture challenges.
Orchestration management challenges related to handling many software components.
Sustainability is viewed from three dimensions:
Technical: Keeping the software operational.
Organizational: Allowing operational improvements with minimal effort.
Social: Improving intended social function without breaching its social contract.
Paper Structure:

Background and related work.
Educational challenges regarding AI software.
Concluding remarks.


## Motivation:
RQ1: Motivation and Benefits of Using MLOps:


## Benefits:
[Key benefit 1 of using MLOps as mentioned in the paper]
[Key benefit 2...]
[...]
RQ2: Approaches and Tools for MLOps:

## Approaches:
* Domain driven design
* Able to backtrack their operations to inital inception to the emission of the automated decision
* Using decision trees to explain machine learning algorithm
* Explainability, accountability, fairness, accountability in ML operations for sustainability 
[Main approach 1 to MLOps discussed in the paper]
[Main approach 2...]
[...]

Associated Tools:
[Tool 1 that facilitates/supports MLOps]
[Tool 2...]
[...]
RQ3: Challenges in Operationalizing MLOps:

## Challenges:
RQ4: Integrating Responsible AI Principles into MLOps Pipelines:

* As MLops and AI software is becoming more complex, sustainbility is harder to maintain.
* Orchestration management challenges related to handling many software components.
* Data scientists are not computer scientists by training
* Data engineering role has evolved and now requires a larger set of skills
* Data science teams are short of Data Engineers
* Complex AI software typically includes tens of autonomous decision making components so it is hard to be monitored.
* Accountability: Decision making software are required to be able to explain its actions

Strategies/Methods:
[Strategy/Method 1 to integrate Responsible AI into MLOps]
[Strategy/Method 2...]

Challenges/Concerns:
[Challenge/Concern 1 in integrating Responsible AI into MLOps]
[Challenge/Concern 2...]

Conclusion and Future Directions:
[A concise summary of the paper's conclusion and insights on potential future research directions, if provided.]

## Reviewer's Comments: [Any subjective notes, comments, or observations you might have after reading and summarizing the paper.]

Explanation leads MLOps to be observable and self-improvable as well as possibly continuous with their intended social contract; (2) explainability leads to fairness which is the foundation for sustaining said social contract itself; (3) accountability accompanies fairness matching it with the legal establishment in which any MLOps are entailed. Figure 6 offers a recap of such a definition.
