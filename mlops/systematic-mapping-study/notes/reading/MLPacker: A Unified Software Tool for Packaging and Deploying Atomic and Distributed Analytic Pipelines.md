MLPacker: A Unified Software Tool for Packaging
and Deploying Atomic and Distributed Analytic
Pipelines
Raul Mi ´ n˜on´
∗
, Josu D´ıaz-de-Arcaya∗
, Ana I. Torre-Bastida∗
, Gorka Zarate∗
and Aitor Moreno-Fernandez-de-Leceta†
∗TECNALIA, Basque Research & Technology Alliance (BRTA)
Albert Einstein 28, Minano, 01510, ˜ Alava, Spain, ´
{raul.minon, josu.diazdearcaya, isabel.torre, gorka.zarate}@tecnalia.com
†
Instituto Ibermatica de Innovacion´
Donostia-San Sebastian, Spain
ai.moreno@ibermatica.com
Abstract—In the last years, MLOps (Machine Learning Operations) paradigm is attracting the attention from the community, extrapolating the DevOps (Development and Operations)
paradigm to the artificial intelligence (AI) development lifecycle. In this area, some challenges must be addressed to
successfully deliver solutions since there are specific nuances
when dealing with AI operationalization such as the model
packaging or monitoring. Fortunately, interesting and helpful
approaches, both from the research community and industry
have emerged. However, further research is still necessary to fulfil
key gaps. This paper presents a tool, MLPacker, for addressing
some of them. Concretely, this tool provides mechanisms to
package and deploy analytic pipelines both in REST APIs and
in streaming mode. In addition, the analytic pipelines can be
deployed atomically (i.e., the whole pipeline in the same machine)
or in a distributed fashion (i.e., deploying each stage of the
pipeline in distinct machines). In this way, users can take
advantage from the cloud continuum paradigm considering edgefog-cloud computing layers. Finally, the tool is decoupled from
the training stage to avoid data scientists the integration of blocks
of code in their experiments for the operationalization. Besides
the package mode (REST API or streaming), the tool can be
configured to perform the deployments in local or in remote
machines and by using or not containers. For this aim, this paper
describes the gaps this tool addresses, the detailed components
and flows supported, as well as an scenario with three different
case studies to better explain the research conducted.
Index Terms—MLOps, AI life-cycle, packaging, deploying,
analytic pipeline
I. INTRODUCTION
The improvement in AI techniques, specifically in Machine Learning (ML) and Deep Learning (DL), supposes a
technological disruption and allows an advance and a digital
transformation in multiple domains. However, although different AI works and studies continue to increase, the majority
of the efforts have been focused on model training, mainly
tested in the laboratory. Consequently, the challenges derived
when implementing a solution in real scenarios and production
environments are often obviated.
Fortunately, recently, the MLOps methodology [1] has
emerged aiming at minimizing the existing leap between
laboratory proof of concept and production-real AI products.
This concept can be defined as a set of best practices that aims
to reliably and efficiently implement and maintain machine
learning models in production. To this end, this methodology defines the different phases of the analytic models lifecycle, leveraging continuous integration to achieve a rapid and
repeatable implementation of models. This way, the model
becomes a reusable software artifact and can be continuously
deployed and monitored through a reproducible and measurable process. In addition, similarly to any other software
artifact life-cycles, there are two crucial phases, packaging and
functionality serving. However, due to the AI software nature,
in this context, these phases become even more complex and
imply new challenges and issues to address.
Traditionally, the systems in charge of packaging and
serving have been complex pieces of software, as stated
in Google MLOps manifesto [2]. Currently, these types of
systems must also be adapted to AI processes, from serving
a simple model such as a linear regression to provide a
complex analytic pipeline composed by ML, DL models and
pre and post-processing phases. Moreover, the complexity is
increased due to key factors to consider like: the variety of
computing environments (Cloud, distributed, edge, hybrid ...)
or the different kind of programming languages, frameworks
or libraries to implement and package the models. The number
of ML algorithms and software implementations is quite large.
Indeed, each library usually has its own recommended way to
deploy models. Therefore, the existence of multiple ways of
deploying a model makes the automation of these deployments
a great hurdle.
In this context, a wide variety of tools have emerged for providing heterogeneous types of inference in production using
different approaches to manage packaged models previously
trained using ML/DL frameworks. However, the majority are
focused on providing a solution to a specific range of ML
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:11:45 UTC from IEEE Xplore. Restrictions apply. 
algorithms or to a concrete framework implementation. For
instance, Torchserve [3] and Tensorflow Extended [4] are
examples of specific deployment tools, belonging to Pytorch
[5] and Tensorflow [6] respectively.
In addition, not always analytic pipelines support is provided and when it is done, seldom distributed pipelines are
considered. Similarly, rarely, the packaging in streaming mode
is included, normally only REST API support is provided
which is not always suitable for specific scenarios like edge
computing. Finally, the majority of MLOps libraries (like
MLFLow [7]) force to be included in the training phase
obligating data scientists, not experts in data engineering, to
be also focused in such tasks.
This paper aims at presenting the MLPacker tool for
facilitating the ML management life-cycle. Specifically, for
packaging and serving ML models or atomic and distributed
analytic pipelines, supporting two distinct serving modes in
API REST or in streaming. In addition, the approach is
decoupled from the training phase which implies that neither
a model or analytic pipeline require the code used to generate
the model nor to integrate packaging or deployment libraries
when coding. Only associated meta-information is required in
the packaging stage. In this way, data scientists can obviate
these stages when conceptualizing their solutions.
II. RELATED WORK
In this section, the state of the art with respect to different
tools that address the key features considered in MLPacker
are examined. To this end, we have divided the approach
into five functionalities to be satisfied by the analyzed tools:
a) creating atomic analytic pipelines deployed in the same
machine; b) support for distributed analytic pipelines (i.e.,
being able to deploy each step of the pipeline on different
machines); c) allow packaging the model as a REST API
d) or in streaming, using publish/subscribe technologies; e)
decouple the deployment from the training phase, avoiding
the integration of deployment libraries in this stage.
In this line, a set of technologies have been analyzed, among
which the following can be highlighted: MLFlow [7] is a tool
to manage the life-cycle of analytic models, focused on four
main aspects: experiment tracking, model packaging alongside
with their meta information, serving the models through an
auto-generated REST API and model registration. However,
despite providing a functionality for packaging and serving
models in REST APIs, streaming packaging is not considered.
In addition, no information has been found for the creation of
analytic pipelines. Finally, MLFlow library must be integrated
from the training phase to be able to deploy the resulting model
as an API. kedro [8] is an open source framework based on
Python for the development of analytic models and pipelines
that promotes the modularization of developments, good practices and standardization. It has significant features, such as
dataset abstraction, pipeline creation and automatic creation of
the project structure, documentation and interactive graphical
displays of the analytic pipeline. Likewise, it facilitates the
creation of containers for the versioning of analytic models.
Among the main shortcomings, it is very focused on training
pipelines, since no connectors focused on streaming have been
found, nor utilities to create a REST API for the deployment.
Additionally, analytic pipelines cannot be decomposed into
different processes to create distributed pipelines. DVC (Data
Version Control) [9] allows tracking and versioning the data
and ML models used for experimentation, and also allows the
creation of analytic pipelines from code. Nevertheless, training
code to execute the analytic pipeline is required and only
atomically in the same machine. BentoML [10] aims at simplifying the deployment of analytic models in automatically
created REST APIs, without requiring the training code, just
the model serialized and related properties. In addition, metainformation about the model and its packaging is generated,
as well as the associated OpenAPI and containers. However,
the creation of pipelines and the deployment in streaming
mode is not supported. Scanflow [11] is an MLOps platform
to deploy and train distributed analytic pipelines on top of
Kubernetes and using MLFlow [7]. As far as we are concern,
the steps of the pipelines do not support streaming deployment,
just packaging in REST APIs, and requires the source code
as MLFlow. ML.NET [12] is an open source framework
for incorporating ML capabilities into .NET applications. It
provides means for generating analytic pipelines, and is able
to bundle the generated pipelines into binary files. However,
it does not support distributed analytic pipelines, nor it offers
functionalities for generating the inputs and outputs of the
pipelines. Finally, Clipper [13] is a prediction system that is
able to leverage different machine learning frameworks for
the model development and packaging, and it provides means
for the communication of such models and the applications
through a REST API. It does not support the packaging in
streaming mode.
In Table I we offer a comparison of the aforementioned tools
with each of the criteria. It can be seen that to the best of the
author’s knowledge, no tool has been found that satisfies all the
needs raised and none of them supports streaming packaging.
III. CONCEPTUALIZING, DESIGNING AND IMPLEMENTING
MLPACKER
This section presents MLPacker. Firstly, in Subsection III-A
its objective and main working modes are exposed. Then,
in Subsection III-B the components of the architecture and
implementation aspects are detailed. Subsection III-C specifies
the required input for MLPacker and, finally, Subsection III-D
explains the different flows.
A. Overview
This paper presents the software tool MLPacker aiming
at packaging, deploying and serving ML models and ML
analytic pipelines. As ML pipeline we mean a set of steps that
transform data by applying different techniques like cleaning,
standardization, aggregation or the execution of an ML model.
They are crucial in real scenarios when deploying ML into
production since generally the process requires pre and post
operations to successfully fulfill the objective. Then, we define
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:11:45 UTC from IEEE Xplore. Restrictions apply. 
(a) Atomic Analytic
Pipelines
(b) Distributed Analytic
Pipelines
(c) REST API
Packaging
(d) Streaming
Packaging
(e) Training
Decoupling
MLFlow ✗ ✗ ✓ ✗ ✗
Kedro ✓ ✗ ✗ ✗ ✗
DVC ✓ ✗ ✗ ✗ ✗
BentoML ✗ ✗ ✓ ✗ ✓
Scanflow ✓ ✓ ✓ ✗ ✗
ML.NET ✓ ✗ ✗ ✗ ✓
Clipper ✓ ✓ ✓ ✗ ✓
MLPacker ✓ ✓ ✓ ✓ ✓
TABLE I
TOOLS THAT SUPPORT DIFFERENT STAGES OF THE MACHINE LEARNING PACKAGING AND OPERATIONALIZATION.
two types of analytic pipelines which we denominate: 1)
atomic: all the pipeline is deployed in the same machine.
Consequently, an input for the first step of the pipeline must
be provided and the last step will generate a result; and 2)
distributed: different stages of the pipeline are deployed in
distinct machines. This enables the possibility of processing
some steps in an edge layer such as anonymization or low latency demanding processes and, in turn, the cloud should deal
with more resource-demanding processes. Therefore, input and
output mechanisms (such as publish-subscribe technologies)
must be provided among the different steps to ensure the
inter-machine communication. Despite, usually, only atomic
pipelines are supported, distributed pipelines allow to leverage
of the cloud continuum paradigm [14]. It is worth mentioning,
that currently the application is focused on the inference stage,
as a consequence, ML training pipelines are not considered in
this iteration.
The tool can be configured to be executed in eight distinct
modes, as a result of considering the following dimensions:
1) Package mode: this variable admits two values, api and
stream. When api is selected the model or pipeline to
be deployed is embedded into a REST API and then is
exposed to receive requests for inference. The stream
mode integrates it into publish-subscribe technologies
to be prepared to consume streaming data, execute the
model or pipeline and publish the result.
2) Deploy mode: this mode permits selecting between
local or remote. Local mode runs the model or pipeline
in the same computer where the tool is executed and
remote mode deploys it in a specified machine or set of
machines.
3) Containerized: this variable indicates whether the deployment will be conducted by embedding the API or
the streaming code into a container or a set of containers
or, by contrast, is executed natively in the underlying
operative system.
B. Architecture and Implementation
Fig. 1 presents the architecture of the tool. The components
have been implemented using Python 3. Below, the objective
and the details of each one are explained:
• Client is utilized as the entry of the tool making use of
the argparse library to provide command line interface
(CLI) behaviour. It is also responsible for orchestrating
the following steps of the process considering the input
received.
• RestMe is in charge of creating the correspondent API
to wrap the model or pipeline to deploy. Internally, it
uses BentoML to create the REST API. However, instead
of having to manually create the necessary code to build
the API (as in the BentoML approach), it is automatically
built using Jinja templates considering the input.
• StreamMe aims at creating the required analytic pipeline,
in streaming mode, instantiating the necessary connectors
and AI frameworks. For this purpose, it has been implemented the streaming builder Python class which requires
an input and output connector and accepts a set of ML
models or blocks of code to be executed.
• Code component permits the processing of blocks of
code to be deployed. To this end, they must be stored
in a Git repository with a requirements.txt file indicating
the dependencies and the target language. In addition, a
function named as handler must be provided which must
orchestrate the code to execute, accepting an input with
the data and returning the result of the process. Currently,
this functionality is supported with Python code and for
the stream package mode.
• The Frameworks component provides an abstract super
class with the necessary methods to interact with AI
frameworks. In this iteration, two methods have been
defined load model to load binary models saved on disk
and get model result to execute the model inference. Thus,
when integrating a new framework these methods must
be implemented. Currently, TensorFlow and Scikit Learn
frameworks are supported.
• Similarly to Frameworks component, the Connectors
component provides an abstract super class with the
required methods to use a connector: connect to establish
a connection if necessary with the target technology
and consume and produce to obtain and provide data
respectively. In this iteration, there is support for MQTT
(Message Queing Telemetry Protocol), Kafka and Web
Sockets.
• Bundler service is dedicated to manage the container
related aspects. Specifically, when a pipeline is created in
stream mode, the necessary code is selected (instead of
packaging all the AI frameworks and all the connectors)
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:11:45 UTC from IEEE Xplore. Restrictions apply. 
CLIENT
 RESTME        STREAMME
CONNECTORS
            FRAMEWORKS
BUNDLER SERVICE
DEPLOYING SERVICE
CODE
Fig. 1. MLPacker Architecture overview
and additional code for the entry point and files like requirements.txt and Dockerfiles are automatically created.
Next, the necessary Docker images are built. Finally, if
local deploy mode is selected the necessary containers are
created and executed, by contrary, if remote deploy mode
is selected, the image is pushed to a container registry. For
this purpose, Docker Python library is utilized. It is worth
noting that in API package mode with the exception to
the push to the registry task, the rest of the tasks are
performed using the underlying BentoML library.
• Deploying service is used in the remote deploy mode
for deploying the model or analytic pipeline already
packaged in the selected infrastructure. To this end,
specific Ansible roles are executed (by using the Ansible
Python library) to install Docker and Docker Compose
in the target machine, pull the required images from the
container registry and execute them in the target machine.
Currently, the installation of Docker and Docker-compose
is supported in Debian machines.
C. Input
The tool presented requires an input where the necessary
information to package and deploy the analytic pipeline is
provided. Concretely, it is necessary to provide the analytic
pipeline, meta-information related with each step of it such
as the location of the process or model to deploy and the IA
framework utilized, the connector properties, the infrastructure
to deploy in and the modes considered. For this purpose,
an extension of the PADL (Analytical Pipeline Definition
and Deployment Language) [15] language has been utilized
which is a syntax aiming at describing analytic pipelines to
be deployed in a distributed edge-fog-cloud infrastructure.
Listing 1 exposes an example of the syntax used to model
an analytic distributed pipeline where three steps are configured. The First and third steps are blocks of code and the
second one a model. These steps are characterized with the
necessary meta-information required for the tool such as the
programming language or AI framework utilized, the input and
output queues or the remote machine where its steps must be
deployed. Moreover, queues and infrastructure required metainformation is also described.
{"version": "1.0", "id": "1", "containerized": true,
"package-mode": "stream", "deploy-mode": "remote",
"pipeline": {
"preparation": {"language": "python", "type": "code",
"props": {
"path": "git@git.code.tecnalia.com:packer/code/preparation.git",
"entrypoint": "main.py", "function": "handler"},
"queues": {"input": "q1", "output": "q2"},"infra": "m1"},
"lstm": {"framework": "tensorflow", "type": "model",
"props": {
"path": "./packer/models/lstm.h5",
"input_format": "json","serializer": "h5"},
"queues": {"input": "q2","output": "q3"},"infra": "m2"},
"outliers_filter": {"language": "python","type": "code",
"props": {
"path": "git@git.code.tecnalia.com:packer/code/outlier-filter.git",
"entrypoint": "main.py","function": "handler"},
"queues": {"input": "q3","output": "q4"},"infra": "m3"}},
"queues": {
"q1": {"connector": "mqtt",
"props":{"server":"mqtt_1","port":1883,"topic":"test1"}},
"q2": {"connector": "mqtt",
"props":{"server":"mqtt_1","port":1883,"topic":"test2"}},
"q3": {"connector": "kafka",
"props":{"server":"kafka_1","port":9092,"topic":"test3"}},
"q4": {"connector": "kafka",
"props":{"server":"kafka_1","port":9092,"topic":"test4"}}},
"infra": {"m1": {"hostname": "edge_node","sshConfig": {"user": "vagrant","pass":
"vagrant","port": 22}},
"m2": {"hostname": "cloud_1","sshConfig": {"user": "vagrant","pass": "vagrant",
"port": 22}},
"m3": {"hostname": "cloud_2","sshConfig": {"user": "vagrant","pass": "vagrant",
"port": 22}}}}
Listing 1. Example of PADL extension modelling a distributed pipeline
D. Procedure
Once the input is configured, the tool can be executed
providing it as a file parameter. Then, the flow defined in Fig.
2 starts. Firstly, the Client parses the input and extracts the
modes configured and the defined analytic pipeline, connectors
and infrastructure to select where to redirect the flow. If it is
API mode, RestMe creates one process or container for atomic
pipelines or various processes or containers for each step
of the pipeline for distributed pipelines which are packaged
in a REST API. Otherwise, in Stream mode, the atomic or
distributed pipelines are built. For this aim, the selected connectors, code and frameworks are used to define the pipeline
necessary code by using a specific class programmed to this
end. If is containerized? is selected, Bundle service is in
charge of packaging in a Docker image that necessary code
(discarding not used connectors and AI frameworks / libraries),
generating on the fly a specific main class for the pipeline to
deploy. For both package modes, API and Stream, Deploy service in Local deploy mode executes the processes previously
created or creates and executes the required containers from
the images built. On Remote deploy mode, when containers are
necessary, the corresponding images are pushed to a container
registry and then in the target machines, an Ansible playbook
pull those images, instantiates them as containers and execute
them. By contrast, when containers are not selected, another
Ansible playbook copy the required processes to the target
machines and execute them.
IV. SCENARIO
This section presents a scenario to illustrate three use
cases of MLPacker in order to validate the utilization of
the tool. Let’s suppose a scenario where a company offers
a service to perform a continuous monitoring in different
edge devices of its clients. To this end, they install in the
target devices an agent which collects distinct metrics of the
operative system resources alongside with the timestamp: CPU
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:11:45 UTC from IEEE Xplore. Restrictions apply. 
     
     PADL +
Package
 mode?
CLIENT
RESTME
STREAMME
DEPLOYING
 SERVICE CONNECTORS
FRAMEWORKS
BUNDLER
SERVICE
API
STREAM
YES
NO
CODE
Containerized?
Fig. 2. MLPacker packaging and operationalization workflow.
utilization, network bytes in and disk read bytes (Dataset for
the example extracted from [16]).
For this purpose, a LSTM Autoencoder [17] model has been
trained to analyse the common distribution of the time-series
data generated (Example inspired in [18]). In this way, new
data generated is provided to the LSTM Autoencoder trained
model and then, the output obtained is contrasted with that
distribution, identifying the values far from it, upper a certain
threshold, as an anomaly in the specific device. Consequently,
three steps are defined to achieve this objective 1) prepare
data, 2) encode the data prepared and 3) check if the result of
the encoder is far from the distribution of the trained model
to detect outliers. Steps one (preparation) and three (outlier
detection) are addressed by blocks of code and step two by a
trained LSTM autoencoder model.
A. Case Study A: API mode
Initially, it is decided to deploy the model in a REST API
and invoke it from a client where the other two blocks of
code have been manually integrated. To this end, Listing 2
shows an excerpt of code of the required PADL definition that
is provided to the tool. Then, the client identifies the modes
package as api and deploy as remote, the containerized set
as true and that there is one model defined in the pipeline to
be deployed in machine m1. After, RestME component reads
the model properties and automatically generates a BentoML
service, which is executed to generate a docker image with
the model wrapped in a REST API. Finally, the Deploying
service pushes the image to a Docker container registry, pulls
it in the target machine, by using an Ansible script, and runs
the container to obtain the REST API in the target machine.
{"version": "1.0", "id": "1", "containerized": true,
"package-mode": "api", "deploy-mode": "remote",
"pipeline": {
"lstm": {"framework": "tensorflow", "type": "model",
"props": {"path": "/home/raul/argituml-ecosystem/packer/models/lstm.h5",
"input_format": "json","serializer": "h5"},
"infra": "m1"}}}
Listing 2. Excerpt of PADL extension modelling an pipeline with a model
to be deployed in an API
B. Case Study B: Atomic stream analytic pipeline
Later, an atomic analytic streaming pipeline is proposed to
be deployed as a whole in the same target machine. To this
end, the pipeline is composed by the two blocks of code and
the model between them and Kafka connectors are selected
for input and output data. Listing 3 shows and excerpt of the
PADL configurations showing the changes made from Listing
1.
{"pipeline": {
"preparation": {"queues": {"input": "q3", "output": "lstm"},"infra": "m2"},
"lstm": {"queues": {"input": "preparation","output": "outliers_filter"},"infra":
"m2"},
"outliers_filter": {"queues": {"input": "lstm","output": "q4"},"infra": "m2"}}}
Listing 3. Excerpt of PADL extension modelling an atomic pipeline
In this case, after parsing the input, StreamMe component
is executed, which creates a code with the necessary pipeline
utilizing the components Connectors, Code and Frameworks.
This pipeline consumes data from a Kafka broker and provides
it to the Preparation code block. Then, the LSTM Autoencoder
model is executed, the result is contrasted with the threshold
in the Outliers Filter code block and finally, the anomalies
detected are published in a different topic of the Kafka broker.
When the code for this pipeline is built, Bundler service
automatically creates a requirements.txt with the required
libraries, a main.py to execute the pipeline and a Dockerfile.
Subsequently, it creates a Docker image executing the resulting
Dockerfile and pushes it to a Docker container registry. Finally,
Deploying service manages the execution of the pipeline in
the target machine.
C. Case Study B: Distributed stream analytic pipeline
Finally, the pipeline requires to be deployed in a distributed
edge-cloud architecture. For this aim, the PADL showed in
Listing 1 is prepared. As a consequence, each step of the
pipeline requires an input and output connector to interact
with the rest of the steps. Mosquitto and Kafka connectors
are proposed. The process is similar to the outlined in previous subsection. However, distributed pipelines are treated
as distinct atomic pipelines which communicate among them.
Consequently, code for three pipelines is created, containerized
and deployed in the three distinct target machines.
D. Discussion
These case studies have shown the strength of the tool to
support different case studies, exemplifying the four highlighted characteristics. The deployment of a model in a REST
API is shown in Subsection IV-A. Deployment of streaming
and atomic and distributed analytic pipelines are respectively
shown in Subsections IV-B and IV-C. Finally, PADL syntax
enables the provision of the required meta-information for
each step of the pipeline. In this way, data scientists and
data engineers do not have to be thinking in the deployment
stage or integrating specific libraries while conceptualizing
their solutions.
Authorized licensed use limited to: Monash University. Downloaded on September 19,2023 at 11:11:45 UTC from IEEE Xplore. Restrictions apply. 
V. CONCLUSION
This paper has presented the MLPacker tool, in the area
of MLOps, aiming at packaging and deploying atomic and
distributed analytic pipelines. Various distinct configurations
are supported, changing the parameters package mode (API
or stream), deploy mode (local or remote) and containerized
(true or false). In addition, the tool is independent of the
training phase by providing the required meta-information,
instead of forcing a data scientist to be conscious of a possible
deployment in the future. As far as we are concern, and as
stated in Section II, there is no approach which considers these
four features: 1) deployment in API mode, 2) deployment in
streaming, 3) consideration for both atomic and distributed
analytic pipelines and 4) independence of the training phase.
Moreover, none of them provide support for packaging a
pipeline in streaming mode. Therefore, we can conclude that
there is an existing gap in research to deal with these features
at the same time in a unified fashion. Moreover, a scenario,
including the three main powerful configurations, has been
elaborated in Section IV to better illustrate the capabilities of
the tool.
VI. FUTURE WORK
There are numerous interesting research topics to consider
in the future work of this approach, mainly focused on two
large areas of research on the operationalization of AI such as
MLOps and IAOps. We have identified the following ones in
our roadmap:
• Support for ML training pipelines
• Creation of a wider methodology, integrating the missing
MLOps phases such as monitoring and retraining.
• Automatic adaptation of models to be deployed in the
edge, considering techniques such as weight pruning [19]
and quantizitation [20].
• Inclusion of labels in PADL to target a computing layer
instead of a specific machine to boost deployments in
technologies like Kubernetes.
• Support replicas of the pipeline steps and support for
pipelines distributed horizontally, where the workload
of a step of the pipeline could be divided in various
machines.
Additionally, MLPacker will be extended to support other programming languages, frameworks, connectors and deployment
of pipelines in API mode, as well as integrat
