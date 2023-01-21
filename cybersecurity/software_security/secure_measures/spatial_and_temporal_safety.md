# Safety

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
* Reference counting
  * Each block of memory has a reference count, which is incremented and decremented as it is used, and the memory is freed when the count reaches zero.

