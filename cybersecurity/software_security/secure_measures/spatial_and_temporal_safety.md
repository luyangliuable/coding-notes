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

```
High address (0xffffffff)
 -----
|     |
 -----
|     |
 -----
|     |
 -----    <-- e - sizeof(typeof(pointer))
|     |
 -----
|     |
 -----    <-- Actual pointer
|     |
 -----
|     |
 -----
|     |
 -----    <--  Base of memory region it may access.
|     |
 -----
|     |
 -----
 Low Address (0x00000000)
```

## Temporal Safety
