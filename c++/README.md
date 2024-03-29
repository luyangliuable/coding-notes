# C++

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [C++](#c)
    - [Case sensitive](#case-sensitive)
    - [Comments](#comments)
        - [Multi-line comments](#multi-line-comments)
    - [Pre-processor directive](#pre-processor-directive)
    - [Code → Save → Compile → Execute](#code--save--compile--execute)
    - [Compile](#compile)

<!-- markdown-toc end -->


## Case sensitive

**Simple hello-world app:** <br />
```C++
// This program outputs the message "Hello World!" to the monitor
 
#include <iostream>
 
int main() {
 
   std::cout << "Hello World!\n";
 
   return 0;
 
}
```

C++ is a case-sensitive language. If you were to type Cout or COUT, the compiler would not know that your intention was to use the keyword cout.

## Comments

```C++
// This program outputs the message "Hello World!" to the monitor
```

### Multi-line comments

```c++
/* This is all commented.
std::cout << "hi!";
None of this is going to run! */
```

## Pre-processor directive
```C++
#include <iostream>
```

## Code → Save → Compile → Execute

When you program in C++, you mainly go through 4 phases during development:

**Code** — writing the program <br />
**Save** — saving the program <br />
**Compile** — compiling via the terminal <br />
**Execute** — executing via the terminal <br />
And repeat (debug the errors if needed). <br />

## Compile

```bash
g++ hello.cpp
./a.out
```
-o specifies the name of the program to be compiled to.

```bash
g++ hello.cpp -o hello
```
C++ is a **compiled language**. That means that to get a program to run, you must first translate it from the human-readable form to something a machine can “understand.” That translation is done by a program called a compiler.

What you read and write is called source code (usually it’s in an English-like language like C++), and what the computer executes is called executable, object code, or machine code (a machine language).

Typically C++ source code files are given the suffix:

.cpp (ex: hello.cpp) or
.h (ex: std_lib_facilities.h).
