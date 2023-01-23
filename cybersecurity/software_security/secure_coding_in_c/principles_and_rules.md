# C Design Principles and Rules

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [C Design Principles and Rules](#c-design-principles-and-rules)
    - [Principle](#principle)
    - [Rules](#rules)
        - [Enforce Input Compliance](#enforce-input-compliance)
        - [Use Safe String Functions](#use-safe-string-functions)
        - [Do not forget NUL Terminator](#do-not-forget-nul-terminator)
        - [Understand Pointer Arithmetic](#understand-pointer-arithmetic)
        - [Use Null After Free](#use-null-after-free)

<!-- markdown-toc end -->


## Principle
* Denfensive
  * Avoid depending on anyone else around you.
  * If someone does something unexpected, your program will not crash.
  * It is minimising trust.
* Pessimistically Check Preconditions
  * Better to throw an exception than run malicious code.
  * e.g. Check even though user not likely will input a NULL pointer.


## Rules
### Enforce Input Compliance

### Use Safe String Functions
    * Traditional string library routines assume target buffers have sufficient length. (e.g. strcpy vs strlcpy and strncpy)
    * strcat -> strlcat
    * strcpy -> strlcpy
    * strncat -> strlcat
    * strncpy -> strlcpy
    * sprintf -> snprintf
    * vsprintf -> vsnprintf
    * get -> fgets

### Do not forget NUL Terminator
* Strings require one additional character to store the NUL terminator.
```c
int main(int argc, char *argv) {
    char str[4]; // Strings require one additional character to store the NUL terminator.
    strcpy(str, "bye");
    int x = strlen(str);
}
```

### Understand Pointer Arithmetic
* Pointer arithmetic multiplies by the size of the type.
    * int_ptr++ increments by sizeof(int) not 1

### Use Null After Free
* To defend against bad deref
```c
int main(int argc, char *argv) {
  int *p = malloc(sizeof(int));
  free(p);
  p=NULL;
}
```

* Use Safe Libraries (despite some performance loss)
    * Safe String Libs
    * Networking (e.g. Google protocol buffers, apache thrift)
