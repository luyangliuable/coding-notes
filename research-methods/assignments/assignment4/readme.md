# Assignment 4

Paper 1

Towards Transparent Behavior of Automated Vehicles: Design and Evaluation of HUD Concepts to Support System Predictability Through Motion Intent Communication

https://dl.acm.org/doi/10.1145/3447526.3472041


Paper 2: Chosen

Explaining Software Bugs Leveraging Code Structures in Neural Machine Translation

https://dl.acm.org/doi/10.1109/ICSE48619.2023.00063


Paper 3

Nebula: An Affordable Open-Source and Autonomous Olfactory Display for VR Headsets

https://dl.acm.org/doi/10.1145/3562939.3565617

Paper 4

Peeves: Physical Event Verification in Smart Homes

https://dl.acm.org/doi/10.1145/3319535.3354254.

## Pain Points
* Bugs consume up to 40% of the total budget in software development
* Bugs cost the global economy billions of dollars each year
* Currently tools identify certain parts of th code as buggy without offering any meaningful explanation.
* Developers spend roughly 50% of their time comprehending the code during software maintenance.
* Current tools either give too many false-positive with generic explanations or too many false negatives like static analysis tools.
* Traiditional NMT techniques treat source code as a sequence of tokens which fail to capture the structure of the source code.

## How
* Train and evaluate model with 150K bug-fix commits collected from github using three different metrics - BLEU.
  * Corrected code + corresponding explanation written by human developers. 
  * Benchmark dataset
  * First benchmark of its kind
* A novel transformer based technique
* A replication package that includes working prototype, experimental dataset and other configuration details for replication.
* Autoregressive process
  * Decoder starts to generate the target sequence
  * All previously generated tokens are passed to the decoder
  * All current outputs are based n previously generated outputs
* Attention mechanism
  * Bahdanau et al. [34] demonstrate how certain locations of the input sequence can be emphasized over others for an effective translation, which is known as the attention mechanism. The attention mechanism makes the training process faster and helps the NMT models translate long sequences 
* Structure-based traversal
  * Instead of representing input as sequential data like English language 
  * To leverage this structural information, several studies represent the tree structure into a sequence of code tokens and use it as the input to sequence-to- sequence models [19], [24]. Hu et al
* Compare bug free abstract syntax tree and bugged AST and get buggynodes and compare. Then train a model with it.

## Result
* Participants find the explanations from Bugsplainer to be the most accurate, most precise, most concise and most useful. Based on the median and mode values, we see that the participants agree the most with explanations from Bugsplainer. 
* Bugsplainer achieves a BLEU score of 33.15, which is considered as understandable to good translation ac- cording to Google’s AutoML Translation documentation
* Bugsplainer 220M (larger model) achieves a big bump of ≈ 39% in BLEU score and ≈ 117% in Exact Match.
* We note that the participants find the explanations from Bugsplainer to be the most accurate, most precise, most concise and most useful. Based on the median and mode values, we see that the participants agree the most with explanations from Bugsplainer

## “Creating a Video Communication Plan”
