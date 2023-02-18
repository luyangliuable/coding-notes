# Hard Things to Remember


## Where things are stored

```c
float a = 1.2; 
int main ()

{
    unsigned int b = 10;
    char message[] = “Hello”;
    static float c = 3;
    static int y;
    int *ptr = (int *)malloc (8);
    free (ptr);

    return 1;
}
```
* float a: Inside data segment (because it is global variable)
* unsigned int b: on stack
* message: on stack (because it is a pointer)
* message[1]: on heap
* static float c: in data segment (because it is a static variable)
* static int y: stored in BSS segment (because it is uninstalised)
* int *ptr: on stack

## Primitive Sizes

### 32-bit Architecture
Char: 8 bits
Int: 32 bit
Unsigned-Int: 32 bits
Short: 16 bits
Long: 32 bit
Float: 32 bit
Double: 32 bit
Long long: 32 bit

### 64-bit Architecture
Char: 8 bits
Int: 32 bits
long: 64 bits
Float: 32 bits
Double: 64 bits
long long: 64 bits


