# Assignment 3 

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Assignment 3 ](#assignment-3)
    - [Task 1](#task-1)
        - [Interview One](#interview-one)
    - [Interview 2](#interview-2)
    - [Interview 3](#interview-3)
    - [Task 2](#task-2)
        - [Tasks](#tasks)

<!-- markdown-toc end -->


## Task 1

### Interview One

| Theme Name                                 | Code Name                           |
|:------------------------------------------:|:-----------------------------------:|
| Personal Background                        | CyberSecurity                       |
|                                            | Mahjong                             |
|                                            | Forensics                           |
| Tools                                      | Open Source                         |
|                                            | Paid                                |
|                                            | Free                                |
| Language Based Generative AI Tools         | Chatgpt                             |
|                                            | Bard                                |
| Image Based Generative AI Tools            | Adobe Image Editor                  |
|                                            | AI Art Generative Websites          |
|                                            | Language Based Tools                |
| Use Cases of AI Tools                      | Proofreading                        |
|                                            | Time Scheduling                     |
|                                            | Provide Simple Explanations         |
|                                            | Editing                             |
|                                            | Finding Synonyms                    |
| Potential Benefits of AI                   | Time-saving                         |
|                                            | Quick access to information         |
|                                            | Simplifying complex concepts (ELI5) |
| Issues With Generative AI                  | Correctness                         |
|                                            | AI Art does't look real             |
|                                            | Biased                              |
|                                            | Trust Issues                        |
|                                            | Transparency concerns               |
|                                            | Requirement of right prompts        |
|                                            | Degrades in correctness over time   |
|                                            |                                     |
| Extracurricular Activities                 | Meal Prep                           |
|                                            | Indian Cuisine                      |
|                                            | Western Cuisine                     |
| University Curricular                      | Group Assignments                   |
| AI with Cybersecurity                      | WormGPT                             |
| Cybersecurity                              | Trojan                              |
|                                            | Malicious Software                  |
| Strategies with dealing with Generative AI | Practice Common Sense               |

## Interview 2

| Theme                               | Code                                                  |
|:------------------------------------|:------------------------------------------------------|
| Personal Background                 | PhD                                                   |
|                                     | Digital Mental Health                                 |
|                                     | Medical Doctor                                        |
|                                     | IT                                                    |
| Generative AI                       | Chatgpt                                               |
|                                     | Chat Bot AI                                           |
|                                     | Google Bard                                           |
|                                     |                                                       |
| Use Cases of AI Tools               | Linguist assistance                                   |
|                                     | Learn about something quickly                         |
|                                     | Minimise repeititve tasks                             |
|                                     | Helps with time management                            |
| Risks associated with generative AI | Uncertain Policies                                    |
|                                     | May widen the gap between the rich and the poor       |
|                                     | Understanding the competencies of students            |
|                                     | Impact career of students                             |
|                                     | Personal information leaked to third party            |
|                                     | Evaluators can easily catch students                  |
|                                     | Answers can be completely out of context              |
| Students and generative AI          | Students need to know about university policies       |
|                                     | Sometimes can help increase the value of assignments? |

## Interview 3

| Theme                               | Code                                                   |
|:------------------------------------|:-------------------------------------------------------|
| Personal Background                 | Sociology                                              |
|                                     | IT                                                     |
| Generative AI                       | Chatgpt                                                |
|                                     | Google Bard                                            |
| Use Cases of Generative AI          | Admin Tasks                                            |
|                                     | Analyses Research Papers                               |
|                                     | Search data                                            |
|                                     | Analysing data                                         |
|                                     | Rephrasing something that is already Written           |
|                                     | Summarise Research Papers                              |
|                                     | Ask questions about day to day things                  |
|                                     | Gives advice on finance                                |
| Shortcomings of Generative AI       | Actually putting things into writing                   |
| Collobration                        | Colleagues use generative AI                           |
| Risks associated with generative AI | Plagiarism from using generative AI                    |
|                                     | Unfair to other students                               |
|                                     | challenge the intellectual capacity of students        |
|                                     | Intellectual property of others can be misappropriated |
| Prompting generative AI             | Need to ask the right questions/prompt                 |

## Task 2: "Telling a data story"

> Telling a **coherent story with your data is a core part of the research process**. Statistics can be used in myriad ways to describe any given dataset, so it is important to use the appropriate measures and visualisations to enrich and provide context to a narrative of your data. Although in a perfect world we would ask a question and then design a process to capture data that answered that question, in reality we often have to make use of 'secondary' data, or data captured previously. In this assignment, you will tell a story about some public data using the methods you have learned about.

### Tasks
1. [ ] Identify an open data source from one of the following open data repositories:
  * https://data.humdata.org/
  * https://data.gov.au/home
  * https://www.dosm.gov.my
  * https://data.go.id/topic-detail
  
* https://data.gov.au/dataset/ds-vic-fd720bba-22ee-45e0-b935-e89c829f0849/details?q=rent
* https://www.abs.gov.au/statistics/people/population/national-state-and-territory-population/mar-2023

2. [ ] Formulate a research question that you want to ask of this data - for example "What is the relationship between a persons age and if they carry an ID card?" (max. 50 words)

> "What is the relationships of population density in melbourne and price of rent in different Melbourne suburbs?"

3. [ ] Select 2 appropriate descriptive metrics (e.g. mean) that tell you something about the data, and calculate those metrics on your selected data, using a tool of your choice. Present the fields from the dataset used and the resulting calculated values (max. 50 words)

* Average price of rent by suburb by year
  * Year of range 2000-2023
  * Suburbs of Melbourne
  * Average price of rent
* Number of population per year
  * Year of range 2000-2023
  * Median population of Melbourne
  
4. [x] Create an appropriate visualisation to help a reader understand what you are saying about the data, which is fully annotated.

* Bubble chart of population vs median rent in Melbourne
![visualisation](2WRx.png ) 

* Link to visualisation which is integrative with a drop down created by me using vegalite:
https://luyangliuable.github.io#rent-by-suburb-year-line-chart

5. [ ] Write a short narrative description of your findings as they relate to you research question, referencing both your chosen metrics and visualisation. (max. 150 words)

There is an overall **positive correlations** of price of rent and the population density of Melbourne. By looking at the average price of rent of all suburbs in Melbourne combined, as the quantitative attribute of population density in Melbourne increases, rent increased as well.

However, in the year from 2020 to 2021 population decreased slightly but the price of rent has plummeted.

## Task 3: "Working with hypotheses"

In this exercise you will formulate a hypothesis, prepare a plan of your study (including statistical testing) and justify it, including the potential limitations of it. Consider the topic of the survey that you participated in during the unit. Imagine you are asked to develop this research area further.

1. Propose a hypothesis. It should be something you can realistically test using one or more of the statistical tests covered in this course. It can concern any topic or natural phenomena which relates in some way to the survey topic. (max. 50 words)

Hypothesis: "Engaging in remote work is associated with a decline in the quality of interpersonal relationships among employees."
Null Hypothesis: "Engaging in remote work has no significant effect on the quality of interpersonal relationships among employees."

3. Write down the independent and dependent variables as well as at least three confounding variables. (max. 50 words)

Independent variable: work setting

Dependent variable: Quality of interpersonal relationships, satisfaction of team, satisfaction of work

Confounding Variables: Personality of the employee, salary, job role and position, company, country, years of experience, team collaboration tools used, hours of work.

Variables like salary, job role, position, company, country and years of experience can be confounding variables because they are irrelevant to the research question and hypothesis but may alter the dependent variables which are the analysis of the study. In the end we want to uncover quality of interpersonal relationships, satisfaction of the team and satisfaction of the work.

4. Imagine you had a budget of up to 1000AUD (in addition to up to 100 hours of your time to conduct the study). Explain what data you will collect to investigate this hypothesis and how you would obtain the data in a practical fashion. (max. 100 words)

Data to collect:
* Work setting
* Salary
* Years of experience
* Collaborative tools
* Qualitative Employee satisfaction of their peers

These data helps us to understand

Methods:
* Disseminate information by sending emails out to all employees who work both remotely and from office more than half the time.
* Use surveys
  * Techniques like **likert-scale survey** items which can assess the closeness, trust, and communication among team members.
* Team performance metrics like ticket/task completion rates, bug rates and other qualitor indicators can help determine how well the employee works as a team.
* Use incentives so when employees participate in the survey will gain points on Workday that they can redeem to get gift cards or electronics.
* Anonymous review scores of peers can also be observed that are related to teamwork and communication.

5. What statistical test do you expect to conduct to test your hypothesis. Provide your assumptions of the data and why such tets(s) are appropriate. (max. 150 words)
If both groups (remote and in-person) are independent and the data is normally distributed, t-test can be performed for independent samples. '

Comparisons can be drawn for the two groups which are employees who work remotely and work from office to determine if there's a statistically significant difference between them.

## Analysis:

### If the sample is sufficiently large
1. Collect data through survey results
2. Check the data is sufficiently large and roughly normally distributed which is required for parametric test.
3. Perform t-testing which is a form of parametric test.
4. Calculate p-value which is a probability of obtaining results at least as extreme as the observed results of a statistical hypothesis test.
5. Compare the p-value against the significance level. If it is less or equal then the null hypothesis is rejected.
6. Report and draw conclusions

### If cannot make assumptions about the distribution of data
* Non-parametric test should be used

1. Collect data through survey results
2. Organise data in ascending order. Also need to deal with missing data by performing imputation. 
3. Sum all ranks of different groups (remote work and work from office)
4. Calculate the u statistics
5. Compare the p-value against the significance level. If it is less or equal then the null hypothesis is rejected.
6. Report and draw conclusions

6. What are the limitations of your study? Write a paragraph that explains these limitations as well as potential future investigations you might conduct. (max. 200 words)
One limitation is that there may be not enough samples to perform parametric testing due to challenges recruiting people who are willing to take part in the test and survey.

The results may suffer from bias from voluntary participants as they are disclosing information related to their employment so they may not be fully truthful.

confounding variables like the inherent personality of the employee may obfusticate the result because the independent variables may be attributed to it which is irrelevant to the study. Employees may also find working with others less enjoyable due to higher work hours despite remote work which is another confounding variable.

7. Present a different narrative that could have been presented from your results, highlighting how the data needs to be selected, methods changed, or process otherwise manipulated to support this different interpretation. (max. 50 words)

Hypothesis: "Engaging in remote work is associated with a increase in **employee satisfication** for **younger employees**."
Null Hypothesis: "Engaging in remote work has no significant effect on employee satisfaction for younger employees."

A different narrative or research question could be the effect of employee satisfaction instead of their interpersonal relationships among employees for remote work. The narrative can also be tweaked to address specifically for younger employees.

For data collection, the survey should be tailored and given to younger people of age below 25. Also the questions from the survey and interviews need to be changed in order to understand if they are satisfied with their work. 

The methods might include stratified sampling to ensure adequate representation of younger engineers, and subgroup analyses could be performed to focus on this demographic.
