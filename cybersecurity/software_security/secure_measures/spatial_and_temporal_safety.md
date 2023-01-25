# Safety

## Memory safety
Ability to prevent illegal access to memory data.
* Prevents buffer overflow and dangling pointer
* Prevents attacker from reading sensitive data and executing malicious code.

### Measures
* Garbage collections
    * Use a thread to periodically scan and automatically deallocate unused object.
* Pointer Safety
    * Safety and predictable pointers created through standard means.
    * Dereference only non-null pointers (belong to that pointer)
    * Prevent dangling pointers, wild pointers, double freeing pointers.
    * Example: Rust's Non-null pointer
        * std::ptr::NonNull used to indicate that a pointer will never be null
        * ensure that a pointer is only dereferenced when it is non-null.
* Bounds checking
* Enforce Type Safety

### Is C/C++ Memory Safe?
* C/C++ is not memory safe but you can write memory safe programs.
    * Compiler can check for violations.
    * Speed is a shortcoming for compiler check.

## Spatial Safety


```c
void copy(char *src, char *dst, int len) {
    int i;

    for (i = 0; i < len; i++) {
        *dst = *src;
        src++;
        dst++;
    }
}
```

* Legitimate Access
  * iff b <= p <= e - sizeof(typeof(p))
  * p is the actual pointer
  * "b" represents the lower bound or the starting address of a valid memory region.
  * "e" represents the upper bound or the ending address of a valid memory region.
  * e-sizeof(typeof(p)) we calculate the last valid memory address within the region

```
High address (0xffffffff)
 -----
|     |
 -----
|     |
 -----
|     |
 -----    <-- e - sizeof(typeof(pointer))
|||||||
 -----
|||||||
 -----    <-- Actual pointer
|||||||
 -----
|||||||
 -----
|||||||
 -----    <--  Base of memory region it may access.
|     |
 -----
|     |
 -----
 Low Address (0x00000000)
```

## Temporal Safety
* Program should only access memory that is still allocated and not already freed.
* To prevent illegal access to memory after it has been deallocated.

### Methods
* Keep track of the lifetime of allocated memory, only access memory still valid.
* Smart pointers
  * automatically deallocate the memory when object is no longer in use.
* Garbage collection
  * program automatically free memory that is no longer being used.
  * Often a background process running periodically that checks for memory blocks that are no longer reachable by the program.
  * [Example](/home/blackfish/Documents/coding-notes/cybersecurity/software_security/secure_measures/garbage_collection_in_cc/garbage_collection_with_bdwgc.c )
* Reference counting
  * Each block of memory has a reference count, which is incremented and decremented as it is used, and the memory is freed when the count reaches zero.
