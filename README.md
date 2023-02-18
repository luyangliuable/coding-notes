# Coding Notes and Snippets

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Coding Notes and Snippets](#coding-notes-and-snippets)
    - [Depth of Knowldege rating](#depth-of-knowldege-rating)
    - [Languages](#languages)
    - [Topics](#topics)
- [How to Use](#how-to-use)
    - [Contribute](#contribute)
    - [Procedure for Adding Notes](#procedure-for-adding-notes)
    - [Acknowledgments](#acknowledgments)

<!-- markdown-toc end -->

This repository contains my personal coding notes and snippets, organized by language and topic.
The approach is by helping you learn by looking at examples.

## Depth of Knowldege rating
The following is a rating system that demonstrates the level of depth in terms of knowledge covered in different skills. The rating system ranges from 1 to 5, with 5 being the highest level of coverage.

## Languages
* JavaScript 1/5
* Python 1/5
* C++ 0/5
* Java 0/5
* C# 1/5
* REST-api 5/5
* c 5/5
* c# 1/5
* code-smells 5/5
* crytography 3/5
* design-process 3/4
* expressjs 2/5
* flask 3/5
* git 4/5
* html-css 1/5
* javascript 4/5
* machine-learning 4/5
* macos 1/5
* nlp 1/5
* nodejs 2/5
* object-oriented-programming 4/5
* react 4/5
* rust 2/5
* shell/bash 2/5
* typescript 5/5
* ui-ux 2/5
* vim and emacs 1/5

## Topics
* Agile Methodology
* Algorithms
* cybersecuritt
* Software Testing
* Data Structures
* Design Patterns
* Web Development
* Database
* AI/ML

# How to Use
Clone the repository to your local machine
```sh
git clone https://github.com/yourusername/personal-coding-notes.git
```

Search for a specific topic
```sh
grep -rIi --exclude='*[A-Za-z0-9]{1000}*' --exclude-dir={.git,crytography_utility_tool,node_modules} "{TOPIC}" .
```


Search only file for a specific topic
```sh
grep -rIi --exclude='*[A-Za-z0-9]{1000}*' --exclude-dir={.git,crytography_utility_tool,node_modules} "{TOPIC}" . | awk '{print $1}'
```

Browse through the directory structure to find the notes you're looking for

You can also use the table of contents to navigate through the notes

## Contribute
If you would like to contribute to this repository, please feel free to create a pull request. I would love to have your input and contributions.

## Procedure for Adding Notes
1. Place note into a suitable topic organized for path name
    e.g. A topic for testing RPC and ActiveX apps goes under cybersecurity -> penetration-testing
2. If the topic is too large break it down into smaller topics by creating sub headings
3. Move all subheading to other appropriate places
    e.g. A malformed argument data that causes buffer overflow in RPC argument can go under software security -> vulnerabilities -> buffer-overflow-vulnerability
4. Place reference link <br />
> see [Buffer overflow](./cybersecurity/software-security/vulnerabilities/buffer-overflow-vulnerability/readme.md)

At original location of the note

## Acknowledgments
Codecademy
Exercism
Google
Stack Overflow
GitHub
MDN web docs
