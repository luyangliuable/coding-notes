Machine Learning application lifecycle augmented
with explanation and security
Saikat Das
Department of Computer Science
Midwestern State University
Wichita Falls, TX 76308
Saikat.Das@msutexas.edu
Sajjan Shiva
Department of Computer Science
The University of Memphis
Memphis, TN 38152
sshiva@memphis.edu
Abstract— We have developed a Distributed Denial of Service
(DDoS) intrusion detection framework that employs ML
ensembles of both supervised and unsupervised classifiers that are
complementary in reaching a corroborated classification decision.
Our work has been limited to DDoS attack detection techniques.
We propose to extend our framework to general ML system
development, based on our review of current ML system
development life cycles. We also propose to augment the general
life cycle model to include security features to enable building
security-in as the development progresses and bolt security-on as
flaws are discovered after deployment. Most ML systems today
operate in a black-box mode, providing users with only the
predictions without associated reasoning as to how the predictions
are brought about. There is heavy emphasis now to build
mechanisms that help the user develop higher confidence in
accepting the predictions of ML systems. Such explainability
feature of ML model predictions is a must for critical systems. We
also propose to augment our lifecycle model with explainability
features. Thus, our ultimate goal is to develop a generic ML
lifecycle process augmented with security and explainability
features. Such an ML lifecycle process will be of immense use in
ML systems development for all domains.
Keywords—Machine learning life cycle, security augmented ML
life cycle, explanation augmented ML life cycle, MLOpS
I. INTRODUCTION
Cybersecurity Ventures estimates that the economic loss due
to cybercrime will soon reach the level of $6 trillion annually by
2021 [1]. Developing new countermeasures to detect and
prevent cyber-attacks will certainly aid in stemming the tide of
cybercrime. Research on developing techniques to detect and
prevent attacks has been underway for quite some time [2].
Machine learning (ML) based techniques are now being
employed to make detection more effective in countering such
attacks and therefore improving accuracy, reliability and
resiliency of the infrastructure. Recently ML systems have been
employed in a multitude of domains in addition to cybersecurity.
An ML system is basically a software application that is
either stand alone or integrated into another system. Most
existing ML systems are developed by experts in the domain for
which they are utilized in. These experts tend to be more inclined
to tweak the system to provide accurate predictions efficiently
than making the application itself secure from cyber-attacks.
Development of secure software has become an industry
standard now. Security augmented software development life
cycles have evolved, matured and employed by software
industry. Microsoft’s secure software development cycle (SDL)
is an example [3]. Since ML systems are data driven and their
predictions and behavior are based on incoming data, standard
techniques for building secure software need to be tailored. As
such, the security aspect in ML system building has taken the
second priority. The ML system development cycle typically
consists of the following stages: Business Need (Requirements
collection and analysis), Dataset acquisition (validation and
cleanup), Model development, Model training and validation,
Model testing, Model Deployment, and Model service and
monitoring. Three components of the ML system development
environment are vulnerable to attacks: Dataset, Model and the
Framework utilized in building the system. Datasets can be
attacked and altered during system development and after
deployment. Code hygiene is an important factor in model
implementation. Frameworks can also be compromised
resulting in inappropriate model selection and construction.
Insider threat in terms of data attacks and manipulation also need
to be handled.
Most ML systems today operate in a black-box mode,
providing users with only the predictions without associated
reasoning as to how the predictions are brought about. Recently,
explainability of ML model predictions has become an area of
intense research [4]. According to a recent Gartner survey [5],
about 80% of users do not completely trust ML predictions.
With the emphasis now on trustable artificial intelligence
(especially for critical systems) it has become a must to make
ML predictions transparent by augmenting explainability and
interpretability features into their development life cycle. We
have so far developed a taxonomy of explainability [6]. We have
investigated various explainable methods and tools [7] and are
currently working with LIME [8] and Kernel SHAP [9] methods
to obtain consistent explanation for detected DDoS attacks. As
the explanations of detected attacks are shown in the form of
effective features, we further use these features to retain the
model for better detection.
The rest of the paper is organized as follows. Section II
summarizes some of the related works. Section III shows the
state of the art of ML life cycles. Section IV presents our
proposed generalized machine learning life cycle augmented
with explanation and security. In Section V, we show the
978-1-6654-0690-1/21/$31.00 ©2021 IEEE
0171 2021 IEEE 12th Annual Ubiquitous Computing, Electronics & Mobile Communication Conference (UEMCON) | 978-1-6654-0690-1/21/$31.00 ©2021 IEEE | DOI: 10.1109/UEMCON53757.2021.9666619
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:14:41 UTC from IEEE Xplore. Restrictions apply. 
assessment methodology for our proposed ML life cycle and
concludes the paper.
II. RELATED WORK
Developing processes for handling various stages of ML life
cycle has been an active research area. We summarize some
pertinent works in this section.
Stefan, et al., [10] introduced a quality assurance
methodology through a new process model called
CRossIndustry Standard Process for the development of
Machine Learning applications with Quality assurance
methodology (CRISP-ML(Q)). They mention that while
developing an ML model, it is very challenging to meet success
criteria without violating the business requirements. To satisfy
business needs, they defined the scope of ML application by
involving both domain experts and data scientists, devised a
minimal viable product (MVP), and suggested that a feasibility
study is needed to minimize risk of failures due to false
expectations.
In ML model development, data validation ensures the early
detection of errors, better model performance and savings in
engineering hours to debug problems. Polyzotis, et al., [11]
proposed a data validation system that is designed to detect
anomalies specifically in data fed into machine learning
pipelines. Although they established some assumptions, a real
implementation is needed to justify those assumptions.
It is important to meticulously define the bounds of
requirements by including real world data. To achieve noise
reduction, signal processing filters can be used to remove
unrelated signals from data [10]. However, this process should
be evaluated because the usage of invalid filters could purge
crucial signals that exist in the data.
Developing the model involves data augmentation and
feature engineering. To perform a label preserving
transformation, if invariances are known, it is beneficial to
perform data augmentation in the input space [10]. As part of
feature engineering, it is required to compare engineered
features against a feature baseline to determine the utility of the
feature. Features that are not useful to improve performance of
the model should be purged.
To address model code testing issues, Schaul, et al. [12]
proposed an open-source testing framework that contains a
series of unit tests and visualization tools. It works on the
principle of divide-and conquer making it capable of identifying
and addressing potential defects earlier. They reported a tool has
assisted in unraveling issues in terms of conforming to practical
properties. They used over 3000 unit tests with 10 parameter
dimensions for testing and each algorithm and unit test pair is
repeated up to 10 times. However, with this tool, performance
of unit tests is not predictive so there is scope for developing
predictive unit tests that predict ML model/algorithm’s
performance in real world activities.
Pham, et al., [13] designed a detector that finds and localizes
bugs in existing deep learning (DL) software libraries. They also
tracked potential anomaly propagation and analyzed faulty
functions in DL libraries that cause software bugs. They
experimented with well-known DL libraries, like TensorFlow,
CNTK and Theano using 11 datasets and their detector detected
12 bugs and 104 unique inconsistencies for 30 pretrained
models. Their approach can be applied for machine learning
software libraries like sckit-learn, pandas, numpy, etc. to find
bugs and faulty functions over a large number of pretrained
models.
While training the model, optimization of hyper-parameters
of all the versions of models should be done to verify and test
the efficiency of best possible model. Pruning methods can be
used to acquire optimized model of lesser size [10]. In some case
it has been shown that 90% of neural networks can be pruned
without losing the accuracy. Further, ensemble methods allow to
train many models and help to obtain fault-tolerant systems as
the error of one model is compensated by another model.
Due to the large input dimensions of ML systems, it is not
possible to achieve test coverage thoroughly. To validate the
performance of model, having an additional test data set for
evaluation which is not similar to training set was recommended
[10]. Robustness of the model can be determined using K-fold
cross validation which is repeatedly executed using disjoint
subsets of data.
Regarding the robustness of ML systems, Dusica et al. [14]
mention that it is challenging to guarantee the performance of
ML when there are deviations in the input. Methods such as
regularization in training, altering the objective of training to
meet the robustness metrics are not efficient in achieving higher
levels of robustness since they offer approximate guarantees.
Thus, there is a need for further research to acquire robustness
guarantees of ML systems.
Song, et al., [15] have presented some challenges in testing
the ML models/applications, like effective corner cases
generation, improving test coverage, testing the ML applications
with millions of parameters, and obtaining accurate pseudooracle.
For the deployment phase of ML system, Stephan, et al., [10]
suggested deploying the system to only small subset of users in
the real-time environment to understand the system behavior,
thus reducing the cost of fixing incorrect deployments.
However, their work does not cover batch inference, pipelines
and versioning steps that are usually involved in the deployment
of model.
Model Serving determines user acceptance and how well the
system connects to the business needs. To assure user
acceptance and usability, Stephan, et al., [10] proposed first
building a prototype and testing with end users to figure out the
acceptance, experience and usage rate of end users. Also, to
achieve customer acceptance and trust, they mentioned
incorporating explainability. Their study of several existing
explainability methods and frameworks that are helpful in root
cause analysis of training data misclassifications has proven to
improve overall performance.
Stephan, et al., [10] report a two- step approach to deal with
model monitoring and maintenance. In the first step, the model
is evaluated to determine its staleness and decide whether update
is needed. In the second step, the model is updated and evaluated
before it is pushed to the system to check if the update was
0172
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:14:41 UTC from IEEE Xplore. Restrictions apply. 
successful. Also, they suggested comparing the performance
after each update with previous versions to minimize the
downtime.
Tianyu, et al., [16] identified the vulnerabilities in ML model
supply chain where they showed that the acquisition of ML
models from third party sources comes with new security issues.
A NIST report (NISTIR 8269) [17] published in 2019 showed
the taxonomy and terminology of adversarial machine learning
and discussed various attacks within ML process flow. Herpig
mentioned the attack surface inside the ML development to
secure the process flow and identified the security issues in
national security in his report "Securing Artificial
Intelligence"[18].
III. ML LIFE CYCLE STATE OF THE ART
Fig. 1 shows the stages in a typical ML life cycle. There are
several ML lifecycles recently proposed by industry each with
its own characteristics and stages. Table I shows a comparative
analysis of representative lifecycles. Please note that the data
presented in Tables I and II is what we could gather from the
corresponding websites of the industries listed in References
section.
Fig. 1. Typical ML Life Cycle
TABLE I. MLOPS STEPS USED IN VARIOUS INDUSTRY
Feature Oracle IBM Microsoft Amazon Google
Business
Need
Business
Need
Data Business Understanding Data Acquisition Data
extraction:
Data Data Ingest Data Acquisition and
Understanding: Data Source,
Pipeline, Data validation, cleanup
Data
Preprocessing
Data analysis:
Model
Development
Develop
Model (s)
Data
Preprocessing
Modeling: Feature Engineering,
Model Training, Model evaluation
Data
Transformation
Data
preparation
Model
Training
Train
Model (s)
Model Training Deployment: Scoring,
Performance, Monitoring
Hyperparameter
Tuning
Model training
Model
Testing
Test
Model (s)
Deploy Customer Acceptance Model Training Model
evaluation:
Model
Deployment
Deploy
Model (s)
Live System Batch Inference Model
validation
Model
Serving
Connect to
Business
Model Evaluation Model serving
Model
Monitoring
Monitor
and
Optimize
Model
monitoring
Augmenting security aspects into software development
lifecycle ensures the security triad of confidentiality, integrity
and availability to the development process. A well-known
secure software development lifecycle (SDL) was proposed by
Microsoft in 2012. Table II shows the components of a
potential secure ML development lifecycle and compares it with
the components proposed by Oracle [19], IBM [20], Microsoft
[21], Amazon [22] and Google [23]. In addition, we propose
some security aspects in the last column corresponding to each
component.
TABLE II. COMPARING STEPS FROM VARIOUS INDUSTRIES ALONG WITH SECURITY ASPECTS
Stages Components
Oracle
IBM
Microsoft
Amazon
Google
Security Aspects
Training Training programs required about security for the
developers
0173
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:14:41 UTC from IEEE Xplore. Restrictions apply. 
Requirements Business
Understanding
✓ ✓ Security requirements, Abuse cases, Risk analysis
Data
Processing
Data Acquisition ✓ ✓ ✓ ✓ Data integrity and security
Ingest (Data
Integrity and
security)
✓
Data Extraction ✓ ✓
Data Analysis ✓ ✓
Data Preparation
(Data Validation
+ Data Cleanup)
✓ ✓ ✓ ✓
Feature
Engineering
✓ ✓ Discard useful features
Data
Transformation
✓ ✓
Design
Model Selection Grid search for an estimator
Hyperparameter
Tuning
✓ ✓
Ensemble ✓ Data Integrity and security
Implementation
Model Training ✓ ✓ ✓ ✓ ✓ Cross validation, Approved tools/ Library, Secure
APIs, Static analysis
Batch Inference ✓ Deprecate functions
Verification
Model Evaluation ✓ ✓ ✓ ✓ Risk Analysis, Pen testing
Model Validation ✓ ✓
Release
Deploy ✓ ✓ ✓ Final Security Review before release, Incident
response plan
Model Serving ✓ ✓ ✓
Response Model Monitoring ✓ ✓ ✓ ✓ Execute Incident response plan
IV. PROPOSED ML LIFE CYCLE AUGMENTED WITH
EXPLANATION AND SECURITY
With the above analysis as the basis, we propose a generic
ML life cycle with security and explainability features, shown in
Fig. 2.
The stages are business need, data, model preparation, model
training, model testing, model deployment, model serving and
monitoring. The associated processes for each of the stages are
shown in the corresponding boxes. Processes for security and
explainability at each stage are also identified. In general,
security aspect in each stage confirms all the security measures
are considered. These include security requirements, abuse
cases, risk analysis, data integrity and security, discarding
useless features, grid search, cross validation, secure API, static
analysis, penetration testing, final security review, incident
response plan, etc. The explainability aspects are required in
terms of explaining model’s prediction. They are, finding the
attributes for explanation, data validity information, right model
selection, model interpretability, explanation of prediction,
verifying explanation consistency and adding confidence score
with explanation. Incorporating security and explainability
aspect with ML lifecycle stages makes it robust and trustworthy
to the developer and client.
Fig. 2 shows seven stages and in each stage, there are three oval
shaped boxes which represent mandatory tasks (red outlined
box), security tasks (green outlined box) and explainable aspects
(blue outlined box). Now, we will discuss the mandatory tasks
for each stage.
Business Need: To develop a ML model, initially the
business understandability is required. The requirements for the
ML development are analyzed in this stage.
Data: As the data is the major component of a ML classifier,
they need to be acquired from an authentic repository. Then data
visualization, validation and cleanup are the further processes to
sanitize the raw data.
Model Preparation: Before developing a ML model, data
needs to be preprocessed. As the ML model only accepts
numerical data, non-numeric (if exists) contents are required to
transformed into numeric. Furthermore, training time can be
reduced, and a better performance accuracy can be achieved
using feature engineering in this stage.
Model Training: In this phase, models are trained using the
pre-processed data. To generate a best performed trained model,
model validation, hyper-parameter tuning, and ensemble
mechanisms are performed multiple times.
0174
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:14:41 UTC from IEEE Xplore. Restrictions apply. 
Fig. 2. Stages of a machine learning development lifecycle
Model Testing: In model testing, the pre-trained models are
tested with testing dataset, and analyzed the performances using
performance metrics or deployment scoring system.
Model Deployment: After completing the testing phase, the
trained models are ready to deploy in real system. In this
deployment phase, several batch inferences, pipelining, model
verification and versioning operations are performed.
Model Serving and Monitoring: The ultimate goal of
developing a ML model is to serve as per the customer
acceptance and connect to the business. These two tasks are
accomplished in this phase. Like any software development, ml
development also requires monitoring, optimization, and live
evaluation when the model is serving to solve real-time
problems.
V. ASSESSMENT METHODOLOGY
Using the proposed ML lifecycle, we have implemented a
complete security solution that not only develops a detection
mechanism for DDoS attacks but also generates the
corresponding explanation supporting the detection. The
detection mechanism is borrowed from our existing research,
i.e., ensemble ML frameworks [24][25], ensemble feature
selection framework [26] [27] and DDoS explainer models [28]
[29], which has the outstanding performance in terms of
detecting DDoS attacks more accurately and maintaining a
lower false alarm. When human operators use IDSs to make
decisions like attack detection, interpretability is almost as
important as accuracy. Hence we use two interpretable machine
learning techniques to build the explainer models and after
comparing these two explainer models, the best performing
model generates the appropriate explanation of the detected
DDoS attacks which improves the trustworthiness of the
decision-making process to the security experts. Figure 3 shows
the process flow of our proposed framework which has the
capability of both detecting DDoS attacks and generating
corresponding explanation. The framework consists of four
major parts, namely data preprocessing, model classification,
DDoS detection and explanation of that prediction.
The process flow starts with the data extraction from the raw
NSL-KDD [30] dataset and then feed the dataset to the data
preprocessing phase to produce ML model acceptable
preprocessed data. From the preprocessed data, the ensemble
supervised ML framework classifies them and generates various
models using different modeling algorithm.
0175
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:14:41 UTC from IEEE Xplore. Restrictions apply. 
Fig. 3. Processflow of our proposed DDoS detection and exaplanation mechanism
For single model classification, we have used logistic regression
(LR), decision tree (DT), naïve bayes (NB), Neural network
(NN), and support vector machine (SVM) to build the models.
Then the outcomes of these five supervised models are
combined with six ensemble mechanisms. The best performing
detection model obtained from the model classification phase
detects DDoS attacks using the testing and verification data.
The core part of our proposed framework is to generate
explanation for the predicted DDoS attacks which is performed
in the explanation of prediction phase. As mentioned earlier, we
have used two IML models, namely LIME and SHAP to develop
the explainer models from the training dataset. Each explainer
model generates the explanations for training, testing and
verification data separately where the prediction for these data
instances are obtained from DDoS detection phase. It should be
mentioned that the data instances in all datasets are labeled with
a cluster number in the data preprocessing phase.
We are now extending the proposed framework for general
ML system development and further extending the process
requirements and details.
ACKNOWLEDGEMENT
This work was partially supported by a DHS/AFIT grant. We
also thank Priyanka Chilakalapudi for her assistance in gathering
the material on related works
