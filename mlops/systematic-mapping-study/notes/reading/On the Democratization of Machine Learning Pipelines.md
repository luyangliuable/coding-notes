On the Democratization of Machine Learning
Pipelines
Alexandre Carqueja
University of Porto
DEI-FEUP
Porto, Portugal
up201705049@up.pt
Bruno Cabral
University of Coimbra
CISUC
DEI-FCTUC
Coimbra, Portugal
bcabral@dei.uc.pt
Joao Paulo Fernandes ˜
University of Porto
LIACC
DEI-FEUP
Porto, Portugal
jpaulo@fe.up.pt
Nuno Lourenc¸o
University of Coimbra
CISUC
DEI-FCTUC
Coimbra, Portugal
naml@dei.uc.pt
Abstract—With the increase of Machine Learning (ML) adoption throughout many industries, the need for efficient methods
to continuously design, develop, and deploy ML models has
also grown. To address this issue, several ML pipelines have
emerged with the goal of creating development environments
which facilitate the deployment, evaluation and maintenance.
In this paper, we advocate that most existing pipelines are not
well suited for the initial stages of ML development, due to their
high setup and maintenance overheads. As such, we propose a
lightweight Quick Machine Learning framework, QML, which
is capable of reducing the setup overhead and operating in the
low infrastructure environments that are most common-place in
experimental ML projects.
To demonstrate QML’s usefulness, we present a case-study
where a lightweight ML pipeline was developed, and subsequently
validated on a standard ML classification problem.
Lastly, we assess the differences between our pipeline and an
alternative lightweight workflow, based on DAGsHub. With this
comparison, we conclude that our approach increases ML task
automation as well as feature support, while falling short only
in the Experiment Tracking category.
To enable the broader community to experiment and assess
QML, as well as the Lightweight Pipeline, this project has been
made publicly available 1
.
Index Terms—Machine Learning Pipelines, Lightweight,
Workflows, MLOps
I. INTRODUCTION
Machine Learning (ML) is a sub-field of Artificial Intelligence (AI) which has been in constant growth for the past
years. Between 2019 and 2020 this area of research saw an increase of 34.5% in journal publications, almost double that of
the year prior [17]. With these continuous advancements many
challenging problems are being tackled, such as personalised
recommendation systems [5], and autonomous driving [3].
Due to the increased successes of ML applications, more
and more companies have started relying on AI as a core element driving their business models, as corroborated by IBM’s
2022 Global AI adoption Index report [15]. In this report,
This work is funded by the FCT - Foundation for Science and Technology,
I.P./MCTES through national funds (PIDDAC), within the scope of CISUC
RD Unit - UIDB/00326/2020 or project code UIDP/00326/2020. And this
work is partially funded by the European Social Fund, through the Regional Operational Program Centro 2020 and by the CMU—Portugal project
CAMELOT (POCI-01-0247-FEDER-045915). 1https://github.com/WALEX2000/qml
IBM identified that 35% of companies were already using
AI in their business, and an additional 47% was exploring
uses for it, which continues the steady growth from previous
years. This report also found that small companies were half
as likely to successfully adopt ML technologies than large
corporations, a gap that is widening, likely due to the large
amount of resources demanded by ML development.
As the adoption of AI and ML technologies keeps on
rising, the need for efficient methods to continuously deliver,
improve, and deploy ML models also increases. A need
that is exacerbated by the difficulties companies face with
ML adoption, which is often deemed too costly and time
consuming, as reported by a 2019 survey on ML deployment
time [6]. An issue that is still quite relevant today, as stated
on a more recent report [20], where 508 ML practitioners
were surveyed. On this survey, 68% of respondents admitted
to have abandoned between 40 - 80% of all ML experiments
conducted in the previous year, mostly due to lack of resources
or infrastructure. Furthermore, 47% of participants reported
that it took then between 4 - 6 months to deploy a single
ML project; 88% said that their company’s annual budget for
ML infrastructure was smaller than 75,000$; and 50% did not
make use of any automated tracking tools.
To address these development challenges, Machine Learning
Operations (MLOps) has emerged. MLOps is an adaptation
of DevOps, the decade-old methodology that was created
to address similar concerns with production quality, but for
“standard” software [10]. Just as for the past decade, DevOps
practices have improved software quality and decreased delivery cycles [4], analogous MLOps practices are also expected
to have the same improvements on ML development. Unlike
DevOps, however, MLOps seeks to address ML specific issues,
such as model and data versioning, continuous training, model
monitoring and testing.
In its essence, DevOps is a development philosophy which
extends the Agile methodology, and defends the unison of the
Development and Operations teams. At its core, sit two central
concepts: Continuous Integration (CI), which promotes constant integration of small changes into the project’s repository,
and Continuous Deployment (CD), which promotes constant
and automated deployment of a software product, without the
978-1-6654-8768-9/22/$31.00 ©2022 IEEE 455
2022 IEEE Symposium Series on Computational Intelligence (SSCI) | 978-1-6654-8768-9/22/$31.00 ©2022 IEEE | DOI: 10.1109/SSCI51031.2022.10022107
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:25:14 UTC from IEEE Xplore. Restrictions apply. 
need of heavy human intervention.
Unfortunately, ML projects have additional requirements
related to data management and model training, which the
DevOps methodology does not address. Crucially, the concept
of Continuous Training (CT) is an addition exclusive to
MLOps, which promotes constant training and re-training of
models when changes are made, or new data is available.
Likewise, as ML requirements differ, so does the MLOps lifecyle (Figure 1), and consequently, MLOps pipelines.
Fig. 1. MLOps life-cycle, adapted from [23].
In order to manage all stages of the ML life-cycle, endto-end ML pipelines can be very useful. Currently, there is a
wide collection of tools that enable ML practitioners to build
these pipelines, such as:
FedML
(www.fedml.ai)
Kubeflow
(www.kubeflow.org)
Polyaxon
(www.polyaxon.com)
H2O
(www.h20.ai)
LynxKite
(www.lynxkite.com)
Seldon
(www.seldon.io)
Hopsworks
(www.hopsworks.ai)
MLReef
(www.mlreef.com)
Databricks
(www.databricks.com)
All of these are powerful options, and many of them are capable of supporting intricate ML environments, which may be
necessary in cutting-edge ML applications. However, despite
the varied use-cases where these alternatives can be helpful,
the amount of infrastructure costs and expertise required to
operate them poses a significant barrier to many ML practitioners, who still find themselves on the initial experimental stages
of ML development [9]. This is part of the reason why half
of the companies attempting ML development still resort to
manual workflows, even with all of these available tools [20].
We tackle the MLOps adoption problem by proposing a
framework for creating lightweight ML pipelines, entitled
Quick Machine Learning (QML), with the intention of decreasing setup overhead and infrastructure costs, while keeping
pipeline extensibility in mind. In our approach, we focus on
supporting all the necessary ML development tasks, spanning
most of the ML life-cycle, but adapted to the light workloads
often encountered in the initial stages of ML projects.
More precisely, we aim to answer two research questions:
RQ1: How feasible is it to create modular pipelines that
automate time-consuming ML tasks, without significantly increasing infrastructure complexity?
To answer this question, we conducted a small-scale casestudy, where we began by defining a sequence of required
pipeline steps, and subsequently applied our ML framework
(QML) to develop a modular ML pipeline which supports the
identified steps, while remaining light on infrastructure. Lastly,
we validated the suitability of this approach by applying the
developed pipeline to a standard ML problem.
RQ2: How does the lightweight pipeline perform in comparison to existing alternatives?
To answer this question we compared the pipeline from our
case-study to existing solutions, by re-running the same experiment with different tools. With this approach, we concluded
upon the advantages in setup-overhead and infrastructure reduction, as well as the disadvantages of our approach.
The remainder of this paper is structured as follows. In
section II, we explore relevant articles in the ML pipeline
domain. In section III, we propose our ML framework for endto-end pipeline development. In section IV, we demonstrate
QML on a case study, where we use it to create a lightweight
pipeline that supports all stages of ML development, except for
App monitoring, New Data Storage, and Model & Data Monitoring, and lastly, we validate it on a standard ML classification
problem. In section V, we re-create the experiment from the
case-study with another lightweight alternative (DAGsHub),
and compare the workflow differences with our approach. To
wrap up, in section VI, we draw some final conclusions.
II. RELATED WORK
In this section we discuss three important topics in the
ML pipeline field. In subsection II-A, we explore two characterization of the ML workflow, exposed in recent articles.
In subsection II-B, we exhibit a framework that reduces
technical debt in ML projects, which we make use of in our
own framework. And in subsection II-C, we review CERN’s
implementation of Kubeflow, a powerful platform for building
end-to-end ML pipelines.
A. Machine Learning Workflow
In order to create end-to-end ML pipelines that cover the entire ML life-cycle, it is necessary to have a solid representation
of the desired workflow. In [12], Ruf et al. tackled this issue
by conducting an overview of DevOps and MLOps principles,
followed by a proposed representation of the typical MLOps
workflow, composed of 4 distinct phases:
• Data Management
• ML Preparation
• ML Pipeline
• Deployment
Each of these phases contained 3 - 4 ordered tasks specific
to each phase, which could be executed by one of 6 different
actors (Data Scientists, Domain Experts, Data Stewards, Data
Engineers, Software Engineers, and MLOps Engineers).
With this representation, 26 open-source ML tools were
compared and benchmarked in accordance to how many of
the different phases they support, and how well they do it.
456 2022 IEEE SSCI — Special Session on Human and Machine Intell. in Collaborative Decision-Making Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:25:14 UTC from IEEE Xplore. Restrictions apply. 
Finally, a small MLOps pipeline was built using MLFlow, Git
and DVC for object detection with images.
In another study [11], Paleyes et al. performed a review
on published reports of ML deployment solutions. From the
analysed case-studies, a similar representation for ML workflows was derived, also containing 4 stages, but with a bigger
emphasis on Model Verification.
With this representation, the authors proposed a list of
common challenges practitioners face at each stage of the ML
workflow, ranging from data collection to model monitoring issues. Additionally, for each challenge some possible solutions
were explored, accompanied by ML tool recommendations
which could help solve the discussed problems.
B. MLBazaar
As seen on the previous papers, aside from end-to-end
pipelines there are also several tools designed to support
only select tasks oof the ML life-cycle. One such toole
iss MLBazaar, a novel framework for ML model building,
proposed by Smith et al. [7].
MLBazaar attempts to tackle some of the ML technical debt
issues first discussed by Google researchers in 2015 [2], and
later investigated by other authors, such as Tang et al. [13].
MLBazaar’s primary goal is to reduce Glue Code by standardizing the integration of ML libraries and custom functions,
with a common API. The proposed system uses a primitivebased approach, where several ML primitives from various
libraries are annotated in a JSON file, with the necessary
metadata to be successfully joined together.
By doing this, it is possible to integrate modules from
different libraries, as well as to contribute new modules,
without the need for any glue code, by simply providing ML
Bazaar with an ordered list of ML primitives.
Lastly, the tool also makes use of AutoML algorithms, based
on Gaussian Process search, to tune hyper-parameters and find
optimal pipeline structures. Which can speed up the model
development stage in the ML life-cycle.
One down-side of tools like MLBazaar, is that they do
not take the full ML life-cycle into consideration, and as
a consequence, must be integrated into more comprehensive
pipelines, as we do in our proposal.
C. Kubeflow
On the other side of the spectrum, Kubeflow provides a
complete, end-to-end ML pipeline [19]. It is a prominent opensource toolkit, which implements a cloud-native kubernetes
approach that promotes highly complex but performant ML
development environments.
A successful example of a Kubeflow implementation was
demonstrated at CERN, as described by Dejan Golubovic and
Ricardo Rocha in their 2021 publication [8]. In this article, the
authors describe CERN’s need for a scalable solution, capable
of serving many different ML problems, without requiring a
specialised team of engineers for each one.
Given Kubeflow’s scalable characteristics, it was chosen as
the foundation for CERN’s ML pipelines, and deployed by the
authors on their large private cloud. The Kubeflow components
utilised in this implementation were Jupyterlab instances,
which allow developers to collaborate with remote Jupyter
Notebooks on their experiments. Kubeflow’s KALE extension,
which translates notebooks into containerised pipelines that
are executed on the network’s distributed nodes. The Katib
extension, which provides automated hyper-parameter optimization features. And lastly, Knative, which was used to
deploy the resulting models through an exposed serverless
REST API, capable of auto-scaling resources according to
real-time demand [18].
To validate this setup, the authors ran a sample 3DGAN
project, where they realised that relying solely on CERN’s
private cloud was insufficient to achieve the desired performance. As such, Google’s public cloud was also used, and
a cost analysis of this solution was conducted. With it, the
authors concluded that the increase in performance was nearly
linear to the increase in allocated resources, and that by using
Preemptibles (Google Cloud’s low SLA instances), it was
possible to significantly cut on Google Cloud costs, to about
1$ per epoch, without significantly impacting performance.
Despite the successful implementation portrayed at CERN,
we argue that the engineering effort required to setup and
maintain a Kubeflow development environment still sits outside the capabilities of many small companies. And despite
the author’s methods for optimizing Google Cloud costs, 1$
per epoch on a standard problem can still result in hundreds
of dollars per training session, which can quickly fall outside
most companies’ ML budgets [20], given the need to train
multiple models multiple times to reach an adequate solution.
III. QUICK MACHINE LEARNING
In this section, we begin by proposing our own representation of the typical ML workflow in subsection III-A, and in
subsection III-B, we explain how QML operates.
A. Machine Learning Workflow Diagram
To develop an end-to-end ML framework, it is necessary
to understand the entirety of the ML workflow. This poses an
issue, as there can be multiple valid workflows that tackle
an arbitrary ML problem, as corroborated by the different
representations given by several authors ([11], [12], [14]).
As we required a comprehensive ML workflow for our
approach, we analysed the previous definitions and created our
own flowchart representation of the ML workflow, based on a
simplified version of the open standard for Business Process
Modeling Notation (BPMN), as shown in Figure 2.
Just as with previous representations, our proposed workflow contains 4 distinct phases (Data Management, ML Preparation, Model Building, and Deployment), as well as an extra
Requirements Gathering step. Unlike previous works, however,
we include an additional “Continuous Processes” phase. This
phase is not part of the regular work sequence, instead, it is
used to include all tasks that must be continuously executed
throughout the development of any ML project, such as SLA
compliance, and pipeline improvements.
2022 IEEE SSCI — Special Session on Human and Machine Intell. in Collaborative Decision-Making 457 Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:25:14 UTC from IEEE Xplore. Restrictions apply. 
Fig. 2. General ML Workflow derived from [11], [12] and [14]
Aside from the aforementioned extra phase, we also propose
two other improvements to previous ML workflow depictions:
Firstly, we represent the cyclical aspect of ML’s life-cycle
by connecting the end of the Deployment Phase back with
the Requirements Gathering step. This demonstrates that requirements may change throughout development, as is the case
when phenomenons such as concept or data drift occur [11].
Secondly, we add 4 decision nodes throughout the workflow.
These nodes enforce the notion that developing ML systems
is an iterative process, and that it is often necessary to ponder
between a new iteration moving forward in the workflow.
B. Proposed Framework
With the intent of creating a framework capable of supporting lightweight pipelines that follow the proposed workflow,
QML was developed. QML acts as the middle-man between
ML practitioners and their chosen pipelines, and enables
developers to modify or switch pipelines without having to
change the interface. At its core, it is a CLI tool which contains
only two commands: ‘start’ and ‘edit’.
The ‘start’ command is the central one, as it is responsible
for setting up new development environments, or booting up
existing ones, depending on the context. The ‘edit’ command,
on the other hand, simply outputs the directory where the
existing pipelines are installed, so that new pipelines can be
added, or so that existing ones can be edited, deleted, or
updated. On this directory, each pipeline is saved under folder
with the directory structure presented in Listing 1.
example_pipeline_name/
.env.yaml
assets/
file_1.txt
file_2.jpg
modules/
cli_command_1.py
event_handler_1.py
setup_process_1.py
...
Listing 1. Example of an installed QML pipeline directory structure.
At the root of the installation, the folder’s name serves as
the name of the pipeline. Then, immediately bellow it, the
specification file must be saved in a YAML format, and entitled
‘.env.yaml’. Lastly, in the ‘modules’ directory, all of the python
modules utilised by the pipeline are saved, and in the ’assets’
directory, all pipeline assets are saved.
The ‘.env.yaml’ file that specifies the pipelines behaviour is
divided by three main sections. The first is the setup section,
where the setup processes and necessary project structure are
defined, as showed in Listing 2. When the pipeline is first
initialize the structure is generated in the project’s directory,
and the processes are run to ensure that everything is initialized
properly.
setup:
structure :
- folder 1 :
- folder 2 :
- subfolder 1 :
- file 1 . txt
processes:
- setup process 1
Listing 2. Example of a setup section in a QML pipeline specification
file.
Next, the watchdog section, where project directories and
associated events are specified (Listing 3), so QML can launch
sub-processes that watch those directories and trigger the event
handlers when appropriate.
watchdog:
- directory : folder 2 / subfolder 1
events:
o n created:
- event handler 1
on modified:
- event handler 2
Listing 3. Example of a watchdog section in a QML pipeline specification
file.
Lastly, the commands section, where developers can specify
CLI commands which are made available to the ML practitioners, so that they can easly interact with the pipeline during
development (Listing 4).
commands:
- command name: cli command 1
- command name: cli command 2
settings:
ignore unknown options: True
Listing 4. Example of a commands section in a QML pipeline
specification file.
In all of these sections, the setup processes, event handlers,
and commands are all python files saved under the ‘modules’
pipeline folder. In order to comply with QML’s requirements,
all these files have to do is implement a designated function
depending on their type. For setup processes this function is
“runProcess”, for events it is “runEvent”, and for commands
it is “runCommand”, with the caveat that we are utilising
458 2022 IEEE SSCI — Special Session on Human and Machine Intell. in Collaborative Decision-Making Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:25:14 UTC from IEEE Xplore. Restrictions apply. 
python’s click package to create the CLI commands. As
such, arguments, options, and additional settings can be easily
integrated into the CLI commands.
The main advantage of our approach is that it is possible
to easily extend QML pipelines by simply editing the YAML
file, and providing the required module. Which allows QML
pipelines to be integrated from the very beginning of the
ML development, and subsequently adapted according to the
changing project needs.
IV. LIGHTWEIGHT PIPELINE CASE-STUDY
In order to demonstrate and test QML, we conducted
a proof-of-concept case-study in which we developed a
lightweight pipeline based on the workflow in Figure 2, that
was subsequently validated on a standard ML classification
problem.
In this section, we present the Lightweight Pipeline created with QML in subsection IV-A, and in subsection IV-B
we demonstrate its execution by solving the aforementioned
classification problem.
A. Lightweight Pipeline Presentation
In order to build the pipeline, we integrated several opensource tools, such as DVC, for data versioning, Pandas Profiler,
for data analysis, and MLBazaar, for Model Building, which
resulted in the pipeline presented in Figure 3.
Fig. 3. Workflow diagram for the proposed Lightweight Pipeline.
In this visual representation of the pipeline, we made use
of some new visual elements. First, we included gray nodes,
which represent miscellaneous steps that are necessary to
operate the pipeline, but that sit outside the expected tasks
of an ML workflow.
Secondly, we added some dotted elements, which represent
ML tasks that the pipeline does not support. For example,
as this pipeline is supposed to remain domain agnostic, we
have decided to forgo the “Raw Data Collection” step entirely.
Instead, it is assumed that the developer already has a data file
ready to be utilized.
Lastly, we differentiated between manual steps, semiautomated steps, and fully automated steps. The manual steps
are represented with rectangular nodes. The semi-automated
steps have a small circle on top of the rectangular nodes. And
the fully automated steps are represented with rounded edges,
as well as with the circle on top.
B. Addressing a Machine Learning Problem
With the pipeline built, we performed a case-study by applying QML to a standard ML classification problem. The data-set
we chose for this task was the Red Wine Quality data-set [1],
due to its usability and popularity. The data-set was collected
in 2009, and contained 1599 samples of Portuguese red wine.
These samples were evaluated and ranked by three separate
wine tasters, on a scale from 1 to 10, and the subsequent
median score was recorded as ‘quality’. Additionally, each
row also contained information about several wine metrics,
such as pH level, alcohol content, acidity, and others, which
were to be used as predictors for the wine’s quality.
With the data in hand, we defined our requirements to be
the accurate classification of the wine’s quality on at least
85% of cases. Then, we proceeded to setup the Lightweight
Pipeline by running the “qml start” command on our project’s
root folder. This command initialized a virtual environment,
scaffolded the required directory structure, and initialized our
project with Git and DVC. Afterwards, our local Git instance
was manually configured with a GitHub remote, and the DVC
instance with a Google Drive remote, as specified in their
documentation [22]. With both of these steps concluded, we
continued into the Data Management Phase (Figure 4).
Fig. 4. Lightweight Pipeline’s Data Management phase, with numbered steps.
The development of this phase started as follows:
Step 1: Download the data from Kaggle [21] and unzip it.
Step 2: Add the data file to the project’s data folder.
Step 3: Pipeline automatically versions the data with DVC.
Step 4: Pipeline automatically generates a data report.
Step 5: Inspect the report by running the command: “qml
inspect data data/winequality-red.csv”. This command
displayed an html page with information on the data-set and
a single warning for a feature with high number of zeros.
From this report, we observed that the target variable (quality)
was highly unbalanced, as despite its 1 to 10 scale, it only
contained values ranging from 3 to 8, most of which between
5 to 7. As we could not draw any further conclusions, we
proceeded to the first decision node in the workflow, in which
we made the decision that a deeper data analysis was required.
Step 6: Generate a new report with the command: “qml
inspect data data/winequality-red.csv -f”. At the cost of
a longer execution time, this command performed a deeper
analysis of the data, which provided us with 29 new warnings,
most pertaining to high correlation between features, and one
to duplicate rows.
2022 IEEE SSCI — Special Session on Human and Machine Intell. in Collaborative Decision-Making 459 Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:25:14 UTC from IEEE Xplore. Restrictions apply. 
In regards to the correlated features, we analysed the report’s
Spearmans and Pearsons correlation matrices, and concluded
that it would be necessary to perform feature selection on the
data-set. As for the duplicated rows, we were unable to draw
further conclusions from the report, and so resorted to manual
data exploration.
Step 7: Create a Jupyter Notebook to analyse the data.
In this notebook, we counted the duplicated entries with
and without taking into account the quality variable, which
showed that there were wines with the same characteristics
but different quality ratings, which indicated that the duplicate
rows were likely not due to faulty data collection, but instead
an intended aspect of the data.
With our analysis complete, we proceeded into the ML
Preparation phase (Figure 5).
Fig. 5. Lightweight Pipeline’s ML Preparation phase, with numbered steps.
As the required data was already on our machine, we went
straight to the second step of the ML Preparation phase.
Step 2: Generate a data handler with the command “qml
gen handler data/winequality-red.csv”. This generated a
template Jupyter notebook, in which we defined our target
variable as “quality”, provided an adequate scoring function,
and defined our train/test split ratio to be 75/25.
Step 3: Generate a data pre-processing pipeline with the
command “qml gen pipeline Wine FE”. This command
created another template Jupyter notebook, which was used to
build the data pre-processing pipeline with MLBazaar. With
that concluded, we continued to decision node 2, and pondered
on what data pre-processing steps were required.
Due to the highly unbalanced data-set, we decided it was
best to shift the classification scale from 1 - 10 to 0 - 2, where
0 would represent poor wines with ratings of 1,2,3 and 4; 1
for average wines with ratings of 5 and 6; And 2 for good
wines with ratings of 7 and above. As no standard primitive
could do this, we proceeded to step 4.
Step 4: Create a custom MLBazaar primitive. To do this,
we followed MLBazaar’s documentation [7] and created the
“re rate” primitive, which shifted the quality scale as described before. Then, we continued to the following steps.
Step 5: Add the MLBazaar primitive to the pipeline.
Step 6: Execute the data pre-processing pipeline with
the command: “qml run pipeline Wine FE data/-
winequality-red.csv -fd -sd winequality-red-FE”.
Step 7: Pipeline automatically versioned new data.
Step 8: Pipeline automatically generated new data handler.
Step 9: Pipeline automatically generated new data report.
Step 10: Inspect the report by running the command:
“qml inspect data data/winequality-red-FE.csv”. From
this analysis, we confirmed that the pre-processing had had
the intended effect. Then, in decision node 3, we decided
that it was necessary to add a standard MLBazaar primitive
to the pipeline, in order to drop the “pH” and “free sulfur
dioxide” columns, due to their low impact on quality and high
correlation with other features. After re-doing steps 5 through
10, we were satisfied with our ML Preparation results and
moved on to the Model Building phase (Figure 6).
Fig. 6. Lightweight Pipeline’s Model Building phase, with numbered steps.
In the Model Building Phase, we attempted to train several
models in order to find the best results, and created a model
pipeline for each one.
Step 1: Add an MLBazaar primitive to the model pipeline.
In our case we started with a Logistic Regression primitive.
Step 3: Manually configure the hyper-parameters of the
models. In this case we left them as default.
Step 5: Train the model pipeline by running the command: “qml run pipeline Wine Log data/winequalityred-FE.csv -sp”.
Step 6: Pipeline automatically versioned the model.
Step 7: Test the model with: “qml test pipeline
Wine Log data/winequality-red-FE.csv”.
Step 8: Pipeline automatically updates the model score
meta-data. In this case the accuracy score was 83%, which
we found lacking, as such, in decision node 7 we decided to
go back to hyper-parameter tuning.
Step 4: Use auto hyper-parameter tuner with the command:
“qml run pipeline Wine Log data/winequality-redFE.csv -sp -at 200”. By doing this we marginally bumped
up the accuracy to 84.5%, but as it still was not enough, we
tried several more models, such as Naive Bayes Classifier,
XGBoost Classifier, keras’s MLP MultiClass Classifier, and a
Random Forest Classifier. As the Random Forest got the best
results, we decided to deploy it in the Model Deployment
phase (Figure 7).
Fig. 7. Lightweight Pipeline’s Model Deployment phase, with numbered
steps.
Step 1: Run the CLI command: “qml deploy Wine RF”,
which created a docker image with the name “wine rf image”.
Step 2: Launch container locally with the command:
“docker run -d –name wine rf container -p 80:80
wine rf image”.
Lastly, we made sure the deployment had been successful
by sending inference requests to the endpoint and check460 2022 IEEE SSCI — Special Session on Human and Machine Intell. in Collaborative Decision-Making Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:25:14 UTC from IEEE Xplore. Restrictions apply. 
ing the status of each reply, which was always successful.
Thus, we completed the full ML development cycle with our
Lightweight Pipeline!
V. RESULTS AND ANALYSIS
In order to assess the impact of our approach, it was
necessary to compare it against a manual alternative. In
attempting this, we realised that it was not reasonable to test
our pipeline against a fully manual workflow, as that would
require us to forgo any standard tools, such as git or thirdparty remote repositories, which is not a realistic development
environment. As such, we decided to compare our pipeline
against DAGsHub, since it is also a lightweight tool, and
prominent in the ML community.
DAGsHub is an ML collaboration platform akin to Github,
which hosts remote git and dvc repositories within a comprehensive web interface. Additionally, it also provides two
repository templates that can be used to scaffold new ML
projects. For this experiment we chose the “Cookie Cutter
DVC Template” [16], which resulted in the workflow on
Figure 8.
Fig. 8. Workflow diagram of DAGsHub project development.
For our experiment, we re-ran the same Wine Quality
project from the previous chapter and concluded upon some
key differences between the two alternatives, starting with the
setup process. While DAGsHub’s setup was not too complex, it
required two more steps than our own, which increases unnecessary manual tasks, and thus gives the Lightweight Pipeline
a slight advantage in this regard. Additionally, DAGsHub
provides no support whatsoever for the Deployment Phase,
meaning that it was not possible to complete the ML life-cycle
using only its template.
As for the features supported by both tools, we analysed
them in 11 domains, as shown in Table I, and concluded that
DAGsHub is only superior in Experiment Tracking, which it
fully automates, while we lack support for it. Regardless, of
the remaining 10 domains, the Lightweight Pipeline automates
2 and semi-automates another 7, while DAGsHub only automates 1 more. Additionally, the remaining 5 that DAGsHub
supports are not automated in any way. Meaning that while
we assist developers with fully or partly automated processes,
DAGsHub only provides an environment in which they can be
manually executed.
Lightweight Pipeline DAGsHub
Data Versioning Automated Supported
Data Analysis Semi-Automated No Support
Data Cleaning Semi-Automated Supported
Feature Engineering Semi-Automated Supported
Model Training Semi-Automated Supported
Hyper-Parameter Tuning Semi-Automated No Support
Model Evaluation Semi-Automated Supported
Model Versioning Automated Automated
Experiment Tracking No Support Automated
Model Deployment Semi-Automated No Support
Model Monitoring No Support No Support
TABLE I
FEATURE COMPARISON BETWEEN THE OUR PIPELINE AND DAGSHUB.
Lastly, it was important to check whether both experiments
had lead to the same model results. As can be seen in Table II,
the results differ slightly, with the Lightweight Pipeline having
an average of 0.75% better accuracy, 0.25% lower F1 score,
and 0.0125 points lower Rooted Mean Square Error (RMSE).
However, these changes are insignificantly small, and likely
attributed to randomness.
Lightweight Pipeline DAGsHub
Accuracy 88% 87%
MSE 0.12 0.14
RMSE 0.35 0.37
Random
Forest
F1 87% 85%
Accuracy 85% 84%
MSE 0.15 0.17
RMSE 0.39 0.41
Logistic
Regression
F1 78% 78%
Accuracy 81% 81%
MSE 0.19 0.20
RMSE 0.44 0.44
Naive
Bayes
Classifier F1 76% 81%
Accuracy 85% 84%
MSE 0.15 0.16
RMSE 0.39 0.40
XGBoost
Classifier
F1 83% 81%
TABLE II
MODEL COMPARISONS BETWEEN OUR PIPELINE AND DAGSHUB.
VI. FINAL CONCLUSIONS
In this paper, we have presented a new framework for
ML pipeline creation, aimed at the initial stages of ML
development. This framework was successfully demonstrated
on a proof-of-concept case-study, where we developed a
lightweight pipeline and applied it to solve a standard ML
classification problem. Lastly, we compared our pipeline’s
workflow to that of a project using DAGsHub, which revealed
that our approach provides higher levels of automation, as
well as a fuller coverage of the ML life-cycle, without increasing development overhead, or costs. In turn, with these
improvements, we have made it easier for individuals and
organizations operating in low-resource environments to make
use of dedicated Machine Learning Pipelines.
2022 IEEE SSCI — Special Session on Human and Machine Intell. in Collaborative Decision-Making 461 Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:25:14 UTC from IEEE Xplore. Restrictions apply. 
We hope that, with our approach and more research on
effective lightweight ML pipelines, we may be able to further
democratize access to feature-rich ML pipelines, and aid
the new-comers of the ML community, while widening the
adoption of MLOps practices across the industry.
