AI Governance in the System Development Life Cycle: Insights on
Responsible Machine Learning Engineering
Samuli Laato
sadala@utu.fi
University of Turku
Turku, Finland
Teemu Birkstedt
teemu.birkstedt@utu.fi
University of Turku
Turku, Finland
Matti Mäntymäki
majuma@utu.fi
University of Turku
Turku, Finland
Matti Minkkinen
matti.minkkinen@utu.fi
University of Turku
Turku, Finland
Tommi Mikkonen
tommi.mikkonen@helsinki.fi
University of Helsinki
Helsinki, Finland
ABSTRACT
In this study we explore the incorporation of artificial intelligence
(AI) governance to system development life cycle (SDLC) models.
We conducted expert interviews among AI and SDLC professionals and analyzed the interview data using qualitative coding and
clustering to extract AI governance concepts. Subsequently, we
mapped these concepts onto three stages in the machine learning (ML) system development process: (1) design, (2) development,
and (3) operation. We discovered 20 governance concepts, some of
which are relevant to more than one of the three stages. Our analysis highlights AI governance as a complex process that involves
multiple activities and stakeholders. As development projects are
unique, the governance requirements and processes also vary. This
study is a step towards understanding how AI governance is conceptually connected to ML systems’ management processes through
the project life cycle.
CCS CONCEPTS
• Software and its engineering → Software creation and management.
KEYWORDS
AI Governance, machine learning, software development life cycle,
system development life cycle, MLOps, DevOps, software development
ACM Reference Format:
Samuli Laato, Teemu Birkstedt, Matti Mäntymäki, Matti Minkkinen, and Tommi
Mikkonen. 2022. AI Governance in the System Development Life Cycle:
Insights on Responsible Machine Learning Engineering. In 1st Conference on AI Engineering - Software Engineering for AI (CAIN’22), May 16–
24, 2022, Pittsburgh, PA, USA. ACM, New York, NY, USA, 11 pages. https:
//doi.org/10.1145/3522664.3528598
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
CAIN’22, May 16–24, 2022, Pittsburgh, PA, USA
© 2022 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-9275-4/21/05. . . $15.00
https://doi.org/10.1145/3522664.3528598
1 INTRODUCTION
The growing popularity of artificial intelligence (AI), particularly in
the form of inscrutable machine learning (ML) models [2] across industry sectors has created the need for AI governance, i.e. to ensure
that AI models operate in a planned and a desirable manner from development to initial roll-out, operation and eventual retirement [12].
The global push for AI governance is evident in developments such
as the OECD recommendation on AI [36] and the European Union’s
proposed Artificial Intelligence Act which seeks to harmonise European AI rules [13]. Dafoe defines AI governance to consist of
"devising global norms, policies, and institutions to best ensure the
beneficial development and use of advanced AI." [9]. Other authors
have complemented this sociopolitical view by focusing on organizational rules, practices and processes on AI technology [31, 41],
and by identifying distinct levels of AI governance ranging from
software development teams to organizational management and
industry-level oversight [43]. In addition to the organizational AI
governance [31], there is a need to involve governance aspects
already at the stage of the AI system implementation. Accordingly,
there is a need to connect the organizational level AI governance
needs into AI implementation processes across the solution life
cycle.
Due to the increasing presence of ML models in software systems, data scientist and ML engineers have become prominent roles
in software development teams. Thus, there is a need to integrate
the work of data scientists and ML engineers into system development life cycle (SDLC) models [1, 20]. This is not a straightforward
task, as the process of creating ML models is often experimental
and takes place in uncharted territory, and is consequently, more
difficult to predict than more mundane well established IT system
development processes [20, 22]. Furthermore, due to the characteristic of ML models being inscrutable black boxes, issues such as
ensuring explainability [2] and establishing audit trails for the ML
models [9, 12] have to be accounted for. Hence, in addition to linking ML engineering with conceptual SDLC models, it is important
to involve the aspect o AI governance in as well.
There is a long research tradition in SDLC models [40] with
recent work partially taking place also under other terms such as
DevOps [11] and MLOps [48]. Similarly AI research has a long
history, and now that the field is experiencing a resurgence after
the ‘AI winter’ of the 1980s and 1990s [38], a myriad of knowledge
is constantly being generated at a rapid pace. In this setting we see
113
2022 IEEE/ACM 1st International Conference on AI Engineering – Software Engineering for AI (CAIN)
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:24:12 UTC from IEEE Xplore. Restrictions apply. 
CAIN’22, May 16–24, 2022, Pittsburgh, PA, USA Laato et al.
as a fruitful starting point to assess prominent SDLC models from
the perspective of ML model implementation and AI governance.
Accordingly, we propose the following research question (RQ):
RQ: What key issues and decisions ML development projects face
during their life cycle with regards to AI governance?
To answer the RQ, we have conducted a series of semi-structured
interviews among high-profile experts involved in AI and software
development. With this approach, we elucidate key concepts related
to AI governance and how they map to different stages of ML model
development life cycle. Our study advances the understanding of
AI governance in the context of ML model development and thus
contributes to the emerging body of IS literature on AI system
design and development [3, 5]. As our contribution to IS practice,
we bridge the gap between the technical layer of AI governance
and practical AI system development.
The rest of this paper is structured as follows. First, we go
through previous literature on AI governance and SDLCs. We then
present our empirical research and analysis methods followed by
the results. Next, we discuss our key findings, implications of the
research and limitations and future work. In the end we present
our final conclusions.
2 BACKGROUND
2.1 SDLCs and AI development
During the past decades software industry has moved towards
iterative development [4] and DevOps practises [21, 26, 52]. In
DevOps, the development and operation of an IS are carried out
by the same people and the stages between pushing code into a
repository and pushing the system into production are automated
to as a high degree as possible [11, 52]. This process follows the
continuous integration/continuous development (CI/CD) paradigm
which implies that as code is pushed into a repository, it is automatically (and continuously) integrated into the surrounding system
and deployed into production after a series of automated tests and
checks [29, 52]. CI/CD involves a great deal of tools and requires
rigorous implementation [29]. Still, this paradigm can be seen as
the current industry standard and is encouraged by cloud vendors
such as Google Cloud [22] and used by major online services such
as Facebook [14].
The growing applicability of ML models for solving various tasks
has also led to the emergence of new developer roles in software
development teams, in particular that of a data scientist [49]. The
duties of data scientists can involve experimenting with data, training machine learning models and providing them for use to the
rest of the development team [49]. Recent work has highlighted
that there are difficulties when incorporating this work of data
scientists into existing software development processes and practises [18, 20]. An interview study among data scientists revealed
that on average the three most relevant hurdles in their work are (1)
decision making with customers; (2) testing and quality assurance;
and (3) debugging [18]. These challenges arise mostly from the
differences that exist between ML model development and other
software development [18]. Thus, work integrating the work of
data scientists into SDLC models is needed.
Studies have acknowledged that ML systems require appropriate
software engineering workflows and verification and validation
testing [43]. High-level AI ethics tools have also been mapped to
the stages of algorithmic development, but in their current stage
they lack usability [34]. In addition, ML models themselves have
technical characteristics that need to be taken into account in the
SDLC [18]. Next we outline and discuss in further detail four key
factors that have been discussed in recent literature, namely: (1)
advanced ML model are black boxes, (2) ML models are probabilistic
as opposed to deterministic, (3) ML development is data-driven,
and (4) ML models cannot be tweaked once trained, and comparing
which model is the best is a non-trivial task.
First, advanced ML models such as the ones employing deep
neural networks (DNNs) are largely black boxes, requiring post
hoc explainability or circumstantial explainability [2]. Due to the
way ML systems are built and operate, the human operators see
the input and output values, but do not necessarily have an explicit
understanding of how the algorithm processes the data [2]. The operation of an artificial neural network can be considered so complex
that external tools for interpreting its operation are needed [39].
However, in some cases even these tools are not enough. In fact, verifying that the ML model works as intended (functional properties)
occurs through rigorous testing of it with a specific test data set
(which was not used to train the model) collected from the model’s
operation context [53].
Second, ML models are probabilistic as opposed to deterministic [1]. The rudimentary form of digital logic and programming
involves giving a computer explicit instructions on what to do. The
computer executes these instructions perfectly and does nothing
else. Systems programmed in this way are considered deterministic,
as the output can be fully traced to the given input and the digital
logic in between. ML models in turn do not give a discrete output,
but instead, offer a probability as an output. Thus, system engineers are forced to work with confidence intervals and particularly
the more complex models such as DNNs may never reach 100%
prediction accuracy [1].
Third, ML model development is data-driven. Data that is used for
training models needs to be acquired, annotated (in supervised ML),
prepared to a specific format for the training algorithms, checked
for quality and split for training and testing [1, 53] among other
factors. Furthermore, it is not straightforward what to do with the
data. Thus, data scientists have emerged [49]. Furthermore, in datadriven development it is crucial to control the quality of the data
and know where models based on the data should and should not
be used, especially in clinical settings and other contexts where
high prediction accuracy is paramount [46]. Oftentimes new source
data are collected for the ML system to make up for changes in
the real world environment. In addition, data can be collected from
human decisions that are based on the model. This data can then
be used to train new, even more holistic models.
Fourth, ML models cannot be tweaked once trained, and thus,
new models need to be created to replace them. Hence, the SDLC
of a ML model also differs from traditional software development
in how new models are moved into production. One popular approach is to train challenger models (new models) and test whether
they perform better than the champion model (the ML model currently in operation). In practise, there may be several challenger
models before tests show one of them to be ready to replace the
champion [35].
114
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:24:12 UTC from IEEE Xplore. Restrictions apply. 
AI Governance in the System Development Life Cycle: Insights on Responsible Machine Learning Engineering CAIN’22, May 16–24, 2022, Pittsburgh, PA, USA
Collectively, these characteristics of ML model development and
operation have contributed to the need to integrate the work of
data scientists and ML engineers into existing SDLC paradigms [20].
Furthermore, the computational requirements of ML models are
very different from rule-based systems [19, 51] which influences the
environments where they can be trained and operated. In summary,
accommodating the characteristics of ML models in SDLCs calls
for technical-level analysis, To control and govern the ML model
development and operation, AI governance during the SDLC is
needed.
2.2 AI Governance
Related to the sociopolitical approach to AI governance [9] is
organization-level AI governance [31, 41]. Mäntymäki et al. [31] define organizational AI governance as "system of rules, practices, processes, and technological tools that are employed to ensure an organization’s use of AI technologies aligns with the organization’s strategies,
objectives, and values; fulfills legal requirements; and meets principles
of ethical AI followed by the organization.". The broader literature
suggests this definition and demonstrates that AI governance entails
social/ethical, legal, and technical elements [6, 7, 33, 42]. One of the
most popular AI governance conceptualization is a layered model
illustrating the interaction between society and AI systems [15].
The model comprises three interacting layers where the technical
layer represents the foundation, followed by the ethical layer and
the social and social and legal layer on the top. In this study, we
focus on the technical layer. The scope of this governance layer has
been divided into three core parts: data, model, and system [41].
Data-related AI governance needs may be managed in five core
steps: (1) acquirement of the data; (2) cleaning; (3) using and reusing;
(4) publishing; and (5) preserving or destroying [44]. Through data
auditing, the steps in this process can be followed to avoid biases.
In ML model development, data is crucially involved in all stages
of the process and is needed to train and test models [53] throughout the development cycle [48]. Therefore, data is an integral part
of ML systems from initial design all the way to eventual retirement [48]. Governance of data sources is therefore paramount to
ensure holistic AI governance [41].
Model-related AI governance is non-trivial due to complex ML
models having poor explainability [2]. Models can be post hoc tested
with various tests that ensure it operates in a desired fashion [53].
Besides testing, governance may be carried out by increasing the
transparency and explainability of ML models [2, 39]. With regards
to the black box ML model itself, operators employ post hoc analyses
to understand how the model works. This is particularly the case
with more complex ML models such as DNNs [2]. While various
tools have been developed to increase explainability of the AI, the
more powerful and useful the AI model is, the more difficult it
is to explain in general [10]. Yet, as AI explainability is crucial, a
large body of academic literature is currently focusing on the topic,
and the field is commonly referred to explainable/explanatory AI
(XAI) [2].
The third aspect of AI governance in the technical layer relates
to the IS [41]. This is also the broadest and most ill-defined category,
as it comprises of the entire IT ecosystem in which the ML model
and related data pipelines are situated. System level governance is
important, as checks and limits may be implemented at this level to
contain the ML model in case it starts yielding undesired predictions.
For example, reinforcement AI learning agents have been deployed
in environments to interact with humans and learn from them [51].
Ensuring these systems are governed and controlled acts as a layer
of protection.
In summary, the AI governance tools are dependent on the data,
ML approach and the surrounding system [41]. However, other
factors such as regulation and ethics can also have impact on the
technical level. Due to the black box nature of the powerful DNN
models, technical AI governance relies on aspects such as data
governance [23], model validation and testing [53] and XAI [2].
3 MATERIALS AND METHODS
3.1 Expert interview design
For answering the RQ described in the Introduction section, we
recruited experts in the field of AI and software development for indepth interviews [8]. The data were collected with semi-structured
interviews. We chose semi-structured interviews to be able to adapt
the interview questions based on new information that arose during
the interviews [16]. The interviews lasted from 30 minutes to one
hour. The interviews were focused on conceptual support for ML
system development in the form of SDLC models, and how AI
governance relates to these processes. We presented the informants
four popular visual conceptualizations of SDLC models (waterfall,
spiral, scrum, devops) and discussed each model with regards to
their good and bad sides, how it fits to ML model development
and AI governance. While these models are not commensurable,
we estimated they provide insights into the development practices
surrounding ML-models.
3.2 Data collection and informants
The interviews were carried out during February-April 2021 by
the first author. All interviews were done through the video conferencing tool Zoom, and they were recorded and subsequently
transcribed. The informants were recruited through the extended
network of the authors, and permission to participate anonymously
in this research project was asked at the beginning of the interview
session. Additional notes and remarks were made during the interviews by the first author. These raw notes totalled up to 10,262
words.
The informants are depicted in Table 1. The informants were
from both industry (n=12) and academia (n=5). In terms of their
profile and expertise, nine were AI/ML experts and eight considered
themselves primarily as software/system experts, although as experts in the field of software, informants in both groups had at least
some knowledge of both domains. As an example, we interviewed
two AI system developers who had previously been software developers, and also software system developers who had worked
in development projects that involved incorporating data and AI
to the system. Some of the informants (e.g., ID15 and ID17) were
more familiar with data governance and others (e.g., ID2, ID5) were
more familiar with ML Training algorithm development. A few
informants (e.g., ID6) were in their own words "unfamiliar" with AI,
but had extensive knowledge on SDLCs. Overall, the informants
115
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:24:12 UTC from IEEE Xplore. Restrictions apply. 
CAIN’22, May 16–24, 2022, Pittsburgh, PA, USA Laato et al.
can be seen as representative of professionals who actively teach,
research or implement AI systems in practise.
3.3 Data analysis
In our data analysis we followed three steps: (1) familiarization
with the data; (2) coding of the data; and (3) formation of a data
structure that describes the data.
In the first step, we familiarized ourselves with the interviews
through re-listening to the recordings, reading the notes and took
further notes about interesting observations related to the research
topic of AI governance. In the second step, we assigned codes to the
interview transcriptions following the open coding approach [45].
These codes were known as the first order concepts, and they were
close to the wording used by the informants to capture their experience [17]. To select relevant concepts from the rich qualitative
material, we specifically looked for concepts in the SDLC models
that were linked to the technical level of AI governance [41]. We
connected similar codes together to form relevant 1st order concepts [17]. The final set of codes and examples where they appeared
in the interviews are displayed in Table 2.
In the third step, guided by Gioia et al. [17], we created a data
structure that described the interview data and the key codes identified in the second step. We subsequently connected the 1st order
concepts into 2nd order themes and gave names to these themes.
This process was iterated until the first order concepts were meaningfully connected to 2nd order themes and the data structure
accurately described the data we had familiarized ourselves with
in the first step of analysis. The outcome of these steps is depicted
in Figure 1.
Gioia et al. [17] suggest connecting the 2nd order themes into
theory-guided aggregate dimensions [30]. Here, we followed the DevOps paradigm [52] and included the steps of system development
and operation as aggregate dimensions. During the process of connecting our 2nd order themes into the two aggregate dimensions,
we noticed that many of the 2nd order themes were antecedents to
the DevOps process. In fact, modern MLOps paradigms include a
third step in the DevOps cycle, which is design [48]. Advantages of
differentiating between design and development has also been highlighted in work dealing with cooperation in software development
teams [24]. Accordingly, we formulated a third aggregate dimension, system design. The final data structure is displayed in Figure 1.
In the next section we present the findings for each category in
more detail and include selected quotes from the informants.
4 FINDINGS
4.1 Dimension 1: system Design
Before ML systems are created and any models beyond early prototypes are trained, certain prerequisites need to be taken into account.
The 1st order concepts in this domain could be sorted primarily
into three 2nd order themes: (1) business case, (2) data resources
and the (3) external environment. Next we discuss findings on each
of these three themes from the perspective of AI governance.
4.1.1 Business case. Defining the business case is important for
any project, but our informants discussed two aspects that are
particularly relevant from the standpoint of AI governance: (1) the
suitability of ML regarding the business case and (2) the projectlevel needs. Several of the interviewees emphasised that while AI
and ML have a lot of hype around them, not all projects benefit
from applying ML. Hence, the very first thing a project should look
into is the suitability of ML for solving the business problem. The
following quotes stress this point:
"When applying machine learning or AI, the most central and
difficult thing is to find the business case." (P12)
"I strongly think that before we do anything, we need to have some
kind of an idea what we are doing. (–) When starting to train a model,
we should have at least some question in mind to which we want a
solution, and think whether machine learning is the right approach
to answering this question." (P15)
Moving onward from the suitability of ML, the project-level
needs also in relation to AI governance should be mapped out. ML
was seen challenging for business cases involving sensitive data,
heavy regulation and strong transparency needs. All these factors
increase the governance requirements of the AI project, increasing
costs and potential issues (legal, ethical...) in the project. These costs
can be brought down with e.g., technical solutions that shoulder
some of the AI governance requirements or conceptual work that
helps in identifying potential pitfalls and areas of focus. These
issues were linked to the project-level needs, which, according to
the informants, included data and analytics needs and capabilities,
the company’s maturity, and other factors that are decided early
on during the project. The following quotes highlight some of the
considerations that are related to these issues:
"[Initially] there is thought and analysis about whether a project is
even started, and after that some design is done and some broad level
frames are set to define what is this thing that we are doing." (P8)
"Not many customers have the capability to work with [ML pipelines],
but we have already created some of these to our customers" (P17)
In summary, when defining the business case and tools to address
it, careful thought is needed on whether to involve ML, since in
addition to basic questions such as "can ML help me solve this
business case", governance issues can greatly increase the costs
and risks of the project. Hence, AI governance needs of the project
should be mapped out and strongly included already when defining
the business case as part of the system design.
4.1.2 Data resources. The informants brought up that a key prerequisite for several ML projects is the availability of suitable data
resources. In case no suitable training data is available, certain systems simply cannot be created until that data is obtained. Furthermore, connected to this theme from the AI governance standpoint
are the quality and validity of the data, data storage issues and legislation. Rigorously carrying out data source mapping in the system
design phase involves AI governance in the form of data governance [44] a partially overlapping aspect of AI governance [31].
Accordingly, data and its governance constitute a central step in the
project design phase. An example quote from one of the informants
discussing the matter is presented below:
"Nowadays when starting a project with a customer we always
scope what data is related to the case, and if a strong data perspective
is there we involve a data scientist to the project for further inquiries."
(P3)
116
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:24:12 UTC from IEEE Xplore. Restrictions apply. 
AI Governance in the System Development Life Cycle: Insights on Responsible Machine Learning Engineering CAIN’22, May 16–24, 2022, Pittsburgh, PA, USA
Table 1: Profiles of the informants
ID Current employment Organization Experience
1 Data and security specialist Large public sector company 5+ years
2 Professor (AI-focused) Large public University 15+ years
3 Senior data specialist Medium private software consulting company 20+ years
4 Senior insurance mathematician Large private insurance company 5+ years
5 Research Fellow (AI-focused) Large public University 15+ years
6 Professor (SDLC-focused) Large public University 20+ years
7 System architect Large private corporation 5+ years
8 Senior software developer Large private software consulting company 10+ years
9 Professor (SDLC- and AI-focused) Large public University 20+ years
10 Competence lead Medium private software consulting company 10+ years
11 Professor (AI-focused) Large public University 20+ years
12 Director of software and services Medium private corporation 20+ years
13 Chief technology officer Medium private corporation 10+ years
14 Software expert Large private corporation 20+ years
15 AI consulting expert Large private software consulting company 10+ years
16 Data group lead Large private software consulting company 10+ years
17 Partner in an AI company Small private AI-focused company 20+ years
Table 2: Codes used in the analysis and examples
Code Example from the interviews
Suitability of ML "In fact I think our customers are oftentimes more focused on the technical
implementation whereas we are still thinking about whether ML is even a
suitable tool for their business case"
Project level needs "first there is a need to think about the [project’s] data and analytics
strategy at a very high level"
Data sources "ML models are closely tied to the data they are trained with."
Capability to use data "(–) whether we can even use the data we have in the first place."
Use environment "Training a model with bogus data gives no indication of whether it works
in the real world environment."
Technical tools "we can use tools such as Azure Machine Learning or Amazon Sagemaker."
Regulatory compliance "Where data is stored matters from the perspective of, say the GDPR legislation."
Data versioning "for reproducability in ML, data versions used for training are tracked."
Data validation "the quality and validity of the used data is of course important."
Data ethics "(–) whether it is ethical to use the data, and in what ways."
Model versioning "We need to version each model and be able to connect them to datasets
they were trained with."
Algorithm specifics "(–) a lot depends on what kind of a model you are building, is it supervised
learning or some reinforcement learning thing."
Parameter weights "After we get one model trained, a lot of time is spent on tweaking the model
parameters to achieve best possible performance."
Manual overview "We always also manually follow what the models do and whether the
outputs make sense to us."
Test dataset "A ML model cannot be meaningfully tested with anything else than data
from the real world situation it’s going to be used in."
Operation "Of course we need to also test how well the model fits to the surrounding
environment system."
Model interpretation "as complexity grows and there are so many parameters at some point no
one is able to understand what is going on."
XAI tools "for example, there’s a tool that can deliver a heatmap that explains the
factors contributing to the model output [in image recognition]."
Bias detection "detecting biased or unfair outputs of the model... (–)"
Anomaly detection "We can teach a model what is normal and use that in monitoring."
117
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:24:12 UTC from IEEE Xplore. Restrictions apply. 
CAIN’22, May 16–24, 2022, Pittsburgh, PA, USA Laato et al.
Figure 1: Results of the analysis and clustering of the interview data regarding ML model governance [17].
Related to the above is the capability to use the data. The potential factors hindering data utilization range from legislation to
technical challenges. Major cloud service vendors were identified
in the interviews as a major enabler of data usage by providing
storage, computing capabilities and libraries and other tools. For example, Informant 11 saw the role of cloud vendors as so important
in system development that he compared paying for them to paying
for electricity. This sentiment was popular among the informants.
By contrast, a few informants brought up that relying on cloud
vendors may not be possible in all scenarios due to data security
issues. Informant 1 explained on this topic as follows:
"There are many requirements, internal and external, on where
data can be stored and used. There are many levels also for data
security. (P1)
A third concept discussed in the interviews related to the theme
of data sources was data ethics. This was only brought forward
by a couple of informants, but is an important aspect to consider
as indicated by prior literature [47]. Informant 9 brought forward
specific frameworks for creating ethical AI and how they are being expanded to the direction of information (data) governance.
Informant 15 mentioned various technical tools such as DVC 1 and
Delta Lake2 that provide support for the ethical handling of data.
Both approaches (frameworks, technical tools) can be utilized simultaneously. Ethical handling of data was seen to require technical
governance, which subsequently needs to be taken into account in
the system design phase.
4.1.3 External environment. The external environment, in which
the ML system operates in, also poses governance requirements.
First, ML models do not operate on their own in a vacuum, but are
implemented as part of an information system. Second, the technical tools used to build the ML system heavily influence and direct
the development. Third, the whole IT system (data and code) surrounding the ML model operates in an environment influenced by
laws, regulations and policies. All these three aspects have intrinsic
AI governance aspects to consider.
The participants gave examples of several systems that they had
been part of creating, where ML models are injected and connected
to, and consequently made part of the larger system. Typically
there is a separate pipeline for ML models and strict tests when
1The data version control tool is available at: https://dvc.org/
2Delta Lake is available at: https://delta.io/
118
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:24:12 UTC from IEEE Xplore. Restrictions apply. 
AI Governance in the System Development Life Cycle: Insights on Responsible Machine Learning Engineering CAIN’22, May 16–24, 2022, Pittsburgh, PA, USA
the deployed model should be replaced with a challenger model. In
practice this means, for example, that the ML model and system
where the ML model is part should be tested separately. Governance
is needed to ensure the model and system perform as intended in the
real world context they are used. Understanding the boundaries of
the system and what happens if predictions given by the ML model
go wrong are important. Containing potential failures was seen
crucial, and the practical governance tool for this was preparing
what to do if ML model predictions fail. Informant 3 explained:
"We set a price for success and a price for failure." (P3)
The technical tools used for developing also have significant
influence. During the interviews libraries such as TensorFlow, Keras
and PyTorch surfaced many times, and the cloud environments to
which, for example, TensorFlow is tied to were mentioned as well.
As data storage and computation oftentimes additionally takes place
in these cloud platforms, their role with in the system design is
enormous. The marketing aspect of this was also mentioned and
speculated upon:
"For example, Google has released TensorFlow as open source. I
am not sure about all the motives of this, but I think (–) [the cloud
providers] want to introduce their libraries and way of doing as the
standard and get people to use their platform as the basis of their
future projects." (P5)
For many AI projects, regulatory requirements such as the GDPR
legislation pose limitations to how data can be handled and where
it can be stored and used [50]. Regulatory compliance needs to
account for hard law, but also other regulations and policies. Accordingly, understanding the legislation related to the project at
hand was deemed important by the informants. Several of the informants mentioned GDPR. For example, Informant 9 discussed
how data collection is rampant these days in the industry, and how
it still needs to comply by law:
"Video game companies collect enormous amounts of data [from
their users]. I hope they have realized that GDPR exists. But this
just emphasizes how data-driven the operations have become in that
domain." (P9)
4.2 Dimension 2: system development
In our analysis the AI governance needs related to the development
phase could be divided into three distinct conceptual themes: (1)
data development, (2) model development, and (3) system testing.
Next we discuss these three stages in further detail.
4.2.1 Data development. The informants discussed various ways
by which data can be governed when developing ML systems, and
here data versioning was pertinent. In particular when training
multiple models, it is important to keep track of which model is in
use and which dataset was used to train this. This enables tracking
down the cause in case an issue is detected in a model. Informant
15 explained:
"In particular in machine learning to produce results that can be
replicated we need data versioning, there are tools for this (–) for
example, DVC3." (P15)
Another aspect informants discussed was data validation. The
most commonly given reason for data validation in the interviews
3Informant refers to the Data version control (DVC) tool, available at: https://dvc.org/
was that it ensured that the data is of sufficient quality for training
models for the specified tasks. Furthermore, data validation was
deemed important due to privacy policies and related regulatory
requirements. However, while these things were seen important,
not all companies adhere to data validation. Informant 2 explained
on this topic:
"I don’t feel there is a lot of data validation out there, except for
basic things such as who can access the data and where it’s stored.
But of course we have privacy policies and related legislation to which
we have to comply to." (P2)
4.2.2 Model development. The informants universally spoke for
the importance of keeping track of the various versions of the
models that were trained. When multiple models are trained, a way
to govern the process is linking the model version number to the
dataset it was trained with.
Model development was seen as a highly iterative process, and
during this process many things related to the algorithms and training approach change. Several prototypes could be created from
linear models and random forests to more complex DNNs. According to the informants, most projects involving ML require a great
deal of experimenting and testing:
"[when training a model] we realize that the data we have does not
fill the expectations we set for it, or our original idea does not work,
and we need to go back. Then we see the chosen way of modelling was
wrong for this data, and we need to go back." (P2)
Accordingly, some of the governance tools also change during the
course of ML model development. As examples, supervised learning
involving a great deal of labelling. This requires understanding and
governance of the labelling process (who carried out the labelling,
how accurately labelled is the data etc.). Reinforcement learning,
by contrast, does not typically use much external data, but the
environment in which the reinforcement learning agent is being
trained needs to be tracked.
The informants pointed out that parameter tweaking is a major
part of getting the model to work as intended, but that there exists
various tools to assist in and automate this process. Mentioned tools
included the XGBoost library4 and tools offered by cloud vendors,
e.g., Amazon Sagemaker and Azure Machine Learning. These tools
offer documentation and reports that help follow changes, tweaks
and adjustments that they carried out. The provided documentation
enables the governance of the parameter tweaking part of model
development.
4.2.3 System testing. Connected to both system development and
system operation was system testing, which according to the informants was regularly carried out in multiple stages of the development and operation of ML models. With regards to AI governance
three central concepts were discussed: manual overview, testing
data sets and the operation environment.
A lot of manual work is involved in creating models, and manual
governance remains an important step to see that a system keeps
working as intended, especially as an increasing amount of the
process is automated.
4XGBoost software and documantation are available at:
https://xgboost.readthedocs.io/en/latest/
119
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:24:12 UTC from IEEE Xplore. Restrictions apply. 
CAIN’22, May 16–24, 2022, Pittsburgh, PA, USA Laato et al.
"[When training models] each time I manage to complete some
intermediary step or see some results I like to check whether things
look feasible and if not, then I return to the drawing board and try
again." (P4) and further:
"Even if I’m responsible for the model, if there are multiple people looking at the outcomes it’s always good. Once the model starts
sprouting out something quite wild it’s good there is someone who
quickly stops the process [to avoid further damage]." (P4)
When focusing on how the model works, reliable test data from
the model use environment is paramount. For predictive ML models
based on supervised, semi-supervised or unsupervised learning,
test data is the primary way to determine how well it works. The
informants gave numerous examples of how this has been done
in practise. Some informants also mentioned the possibility to use
synthetic data or other metrics, but they too agreed that a test
data set is currently the most solid and reliable way to test model
performance and subsequently govern the output.
"Quickly thinking [the model testing process] is simple. You have
a test data set that shows the system is correct 97% of the time. The
accuracy is thus 97% period. However, oftentimes its more complicated
as there are all kinds of dependencies in the data. (–) Even promising
test results may no longer hold when taken into a new environment."
(P2)
The final aspect of system testing related to AI governance was
how well the model fits the operation environment. If data is created
from the model use, this is even more important. For systems with a
feedback loop where new models are continuously trained with data
collected from the use of the old model, poor operation environment
testing can cause issues in the incoming data and subsequently the
trained models. While operation environment -related tests are
largely carried out during system operation, some of these tests
need to be carried out in the development phase before pushing a
model into production. Carrying operation environment tests were
seen as a key part of AI governance of the system as they account
for variables related to the environment within which the model
operates.
4.3 Dimension 3: system operation
From our data three 2nd order themes of AI governance related to
system operation arose: (1) system testing; which was also related
to the development phase, (2) technical model explanations, and
(3) automated monitoring. Next we discuss these three themes in
further detail.
4.3.1 Model explanation. Unlike rule-based systems and other
transparent models, black box AI models are so complex their understanding is not humanly possible. Informants 15 and 17 compared
attempts to understand them to natural science. Informant 11 provided a clear explanation outlining the XAI challenge:
"When [the ML model is] multiplying enormous matrices together
and then applying some non-linear functions to them a hundred times
in a row, how can anyone ultimately know what is happening there?"
(P11)
The informants noted that the more complex ML models become,
the more difficult it is for humans to interpret and understand them.
As an example, Informant 3 stated:
"The more simpler the model the more explainable it generally is.
The more outwards [towards complexity] we go, and the bigger gun
we have to shoot the model with, the less details we see." (P3)
Libraries such as SHAP5 and LIME [39] were mentioned by some
informants as ways to increase the explainability of ML models.
Furthermore, the informants noted that XAI is a requirement in
some areas such as healthcare but is not as crucial in, for example,
targeted ads. In some cases there may be a trade-off between using
XAI and predictive power. Informant 17 explained as follows:
"If a black box model is 99,9% accurate but a model we can explain
and govern is say 98,5% accurate, in some instances it may be justified
to use the latter model even though its predictive power is slightly
worse." (P17)
4.3.2 Automated monitoring. The final discussed category was
automated monitoring of models in operation. Here techniques
pertained to, in particular, bias and anomaly detection. Here biases
refer to unfair predictions made by the model, and anomalies to
unusual occurrences and events in the AI system output or the
overall system.
The importance of automated monitoring from the governance
perspective is critical, as it acts as a final layer of security in systems
where ML model predictions need to be accurate. For instance, selfdriving cars can employ a previous version of the central driving
AI as a backup, and in case something goes on with the champion
model, the previous version can be quickly activated even if a car
is driving full speed on a motorway. In medical diagnostics, an
automated monitoring system can detect if poisoned data is being
fed into the system using an anomaly detection approach, and
isolate the poisoned data from the rest of the data set. Automated
monitoring was discussed particularly with the informants working
with continuously online products. Informant 12 explained:
"We monitor broadly the state of our devices and [can react to]
phenomena and observations we make and adjust our system to better
align with the practical work." (P12)
Monitoring enables the governance of the system as it serves to
protect the boundaries within which the system is set to operate.
5 DISCUSSION
5.1 Mapping the findings into the SDLC
This study set out to investigate (1) the key technical steps and
decisions in the SDLC of ML models that impact the AI governance
of the resulting system and (2) how technical AI governance aspects
map to the life cycle of ML systems. The 1st order concepts and 2nd
order themes identified from the expert interviews (see 1) provide a
tentative answer to the first question by outlining the AI governance
considerations that arise from the SDLC of ML models.
The analysis of the results can be continued further, as the aggregate dimensions used in the qualitative analysis were steps from
the ML model development life cycle model MLOps [48]. Hence,
the findings can re-visualized as a SDLC model. A basic sequential
view is presented in Fig. 2. This waterfall-type visualization can be
used to monitor the governance need of AI projects. In this model
the actual development work occurs in the center block, and that
may very well be iterative and follow, for example, agile practises.
5The SHAP library is available at: https://pypi.org/project/shap/
120
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:24:12 UTC from IEEE Xplore. Restrictions apply. 
AI Governance in the System Development Life Cycle: Insights on Responsible Machine Learning Engineering CAIN’22, May 16–24, 2022, Pittsburgh, PA, USA
However, recent SDLC guidelines (e.g., [22]) favor DevOps, MLOps
and CI/CD practises as discussed in the Background section.
Figure 2: Transforming the governance needs into an SDLC
by using the waterfall approach.
In order to integrate AI governance into the CI/CD pipeline [37]
we selected a popular DevOps-based CI/CD approach [52]. Following the linear mapping of the discovered stages of AI governance,
we can also map the aggregate dimensions and their sub-themes
into CI/CD pipelines commonly used in software development
following the DevOps paradigm [52]. This approach is visualized
in Fig. 3. Here, the development process starts from defining the
model prerequisites and system design, which consisted of three
broad level sub-categories: business case, data resources and requirements from the external environment. From here, iterative
development work begins. For the system development, three categories of AI governance have to be considered: data development;
model development; and system testing. The developed ML models
can subsequently be deployed as part of the surrounding IT system
and moved onward in the DevOps pipeline [52]. The model operation dimension covers four steps in this pipeline from automated
tests and monitoring to collecting continuous feedback. Under performance testing we have automated tests and quality monitoring.
Quality monitoring also relates to XAI tools which can be used to
give insight into the model performance [2]. Finally, continuous
feedback from the deployed system is collected to manually or automatically interfere in case something goes off. XAI tools can also
assist in collecting continuous feedback, as they open up how the
model performs through increasing transparency.
Figure 3: Mapping the identified key AI governance stages
into a CI/CD pipeline [52].
5.2 Theoretical contributions
With our findings, we address the calls of previous work to integrate
the work of ML engineers into the SDLC literature [20]. We support
previous conceptualizations of ML system life cycle models (e.g. [1])
by bringing in the perspective of AI governance. We connect the
DevOps conceptualization of Virmani [52] to the recent work on
MLOps [48] and show how AI governance can be displayed in a
CI/CD pipeline. With these contributions, we advance research on
AI governance [3, 5] by providing early steps for the conceptual
unification of AI governance and SDLC models.
With reference to the research gap on implementing AI governance in SDLC models identified in the Introduction, our work
contributes a systematic mapping of technical AI governance dimensions to common SDLC models: a sequential waterfall-type
approach and a DevOps-based CI/CD approach. To complement
previous exploratory work by researchers [34], our empirical study
is based on interviews of high-profile AI experts and thus, firmly
grounded in software development practice. In the literature on
the multiple levels of AI governance [15, 43], this mapping of key
AI governance issues onto the cyclical phases of system design,
iterative development and system operation, provides a rich basis
for further conceptualization and implementation of the technical
layer of AI governance [41]. The eight 2nd order themes as well
as the granular level of the 20 1st order concepts offer an initial
checklist of considerations in technical AI governance in different
stages of the system life cycle. The foundation of technical AI governance ultimately enables beneficial AI development and use on
the organizational and societal layers [15].
5.3 Contributions to practice
Previous work has stressed that when software consulting companies deliver ML systems, the final product should be the MLOps
pipeline [48]. We support this approach via situating the discovered governance needs into a CI/CD pipeline visualization [37, 52].
While previous work has presented more detailed pipelines [22, 48],
these are also solution-dependent and do not necessarily apply to
all forms of ML such as reinforcement learning. Due to the heterogeneity and continuously changing and evolving nature of AI
systems, it is important to bring clarity to AI governance with conceptualizations and visualizations that can be applied broadly to
several projects.
While previous work on the technical layer of AI governance
has neatly described it in the three themes of data, model and
system [41], our findings offer a more rugged viewpoint on the
topic. A recent work on bridging the gap between AI ethics theory
and practise resorted into providing recommendations instead of
rigid guidelines [43]. In accordance, our work should also be taken
into practice via consideration and assessment, and not viewed as
an exhaustive list. In addition, as recent work has noted that AI
systems are used widely by non-IT professionals (e.g. [25, 27]), our
work can help laypeople conceptualize and understand some of the
key governance issues involved with AI systems. In summary, our
work has contributions on both theory and practice in primarily two
key areas: AI governance and SDLCs for ML-systems. We provide
a synthesized summary of these contributions in Table 3
5.4 Limitations and future work
Our work has the following limitations regarding the empirical
study. First, the informants were recruited from the authors’ extended networks and not all invited participants could take part in
the interviews. This may limit the generalizability of the findings.
However, the informants represented a relatively wide variety of
121
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:24:12 UTC from IEEE Xplore. Restrictions apply. 
CAIN’22, May 16–24, 2022, Pittsburgh, PA, USA Laato et al.
Table 3: A summary of the main theoretical contributions of this study.
Contribution area Key contributions
AI Governance We discover key AI governance steps involved in ML model development through
expert interviews. We bridge the gap between AI governance theory and practical
development. We connect governance into three development stages and show how
these connect to a CI/CD pipeline.
SDLC models We propose a set of governance needs to be taken into account in the SDLC process
of systems involving ML. We propose a CI/CD visualization based on [52]
and elucidate the AI governance steps involved in each phase of the pipeline.
organizations (both academia and industry) and were heterogeneous in expertise and experience. Second, the novelty of the topic
at hand is a potential source of limitations. AI technologies are
constantly being developed and new solutions emerge at a rapid
pace. AI governance is a relatively fresh field and one that is also
constantly evolving as it is dependent on the AI technology. Altogether, we feel that we had a sufficient saturation of interviews at
this stage, and see more detailed field experiments, case studies and
system-specific analyses as a promising direction to continue this
line of research.
For future research, the results of this work could also be further
fine-tuned by conducting a delphi-study [28] where the findings
presented in this work are sent back to the interviewed experts, or
another group of experts, and critically evaluated based on received
feedback. Such approaches may sharpen the now relatively broad
analyses and bring more details to the picture. Another approach
we see as fruitful is to focus on popular contemporary platforms for
ML development, such as Amazon SageMaker and Azure Machine
Learning, and critically evaluate their support for AI governance
from the perspective of conceptual work on the topic. Finally, ethics
was discussed relatively rarely in the interviews, but it has been the
topic of extensive discussion in recent literature on AI governance
(e.g. [32, 42]). Hence we see it fruitful to take even more detailed and
granular perspectives towards organizational AI governance and
then ultimately connecting them back to SDLC conceptualizations,
and consequently, concrete development work.
6 CONCLUSIONS
In this work we conducted in-depth expert interviews to elucidate
the governance needs of technical ML development in view of
the SDLC. We discovered 20 unique 1st order concepts which we
connected to 8 second order themes. We mapped these to the three
stages of MLOps as described by Valohai [48]. Using the CI/CD
pipeline presented by Virmani [52], we connected our findings to
specific steps in ML system development. In doing so, we took
early steps to integrating AI governance aspects to ML system
development as well on a conceptual level from the SDLC model
perspective.
The relative importance of various stages in AI governance may
change over time as technology evolves. For example, the on-going
research on XAI tools [2] as a potential solution to governance issues arising from the black box nature of DNNs and other complex
AI systems. Theoretically, technical advances here could radically
increase model explainability to the point where AI models may
be more holistically governed. However, whether such a future is
realistic remains a debate. Currently it seems that the sheer complexity of these models prevents any attempts to gain insights into
how they operate, and as deep neural networks, convolutional networks and other complex ML techniques are advancing, the model
explainability may only worse over time. If this is the case, then
the role of testing (in its many forms [53]) will become paramount
in the governance of ML models.
