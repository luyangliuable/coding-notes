# Stacks
<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Stacks](#stacks)
    - [Example](#example)
    - [Frame Pointer](#frame-pointer)
        - [Example](#example-1)
    - [Why Push Arguments in Reverse Order?](#why-push-arguments-in-reverse-order)

<!-- markdown-toc end -->

* Store data used in function invocations. A program executes as a series of function calls.
* Whenever a function is called.
    * Allocate some space on the stack.
    * Store arguments in reverse order.
    * Store the return address in text after execution.
    * Store previous Frame pointer.
    * Local variables are stored. Some compilers may randomise the order of the local variables or give extra space for this region.


## Example
```c
void func(int a, int b)
{
  int x, y;
  x = a + b;
  y = a - b;
}
```

```
(High address 0xffffffff)
    |----------------| --
    |   value of b   |   |
|   |----------------|   | arguments
|   |   value of a   |   |
|   |----------------| --
|   |   return addr. |
v   |----------------|
    |   prev. FP     |
    |----------------|  --  <--- current FP
    |   value of x   |    |
    |----------------|    | local variables
    |   value of y   |    |
    |----------------|  --
    |                |
    |----------------|
(Low address 0x00000000)
```

## Frame Pointer
* A register in CPU called frame pointer points to a fixed location in the stack frame
* The address of each argument and local variable on the stack frame can be **calculated using this register and an offset**.

### Example
* %ebp is the frame pointer, it always points to where the previous frame pointer is stored.
* Each register holds 4 bytes of memory
* %edx and %eax are 2 general puporse registers used for storing temporary results.
```asm
movl 12(%ebp), %eax ; store b at %ebp + 12
movl 8(%ebp), %edx  ; store a at %ebp + 8
addl %edx, $eax
    movl %eax, -8(%ebp) ; store x at %ebp - 8
```

* x is actually allocated 8 bytes below the frame pointer by the compiler, not 4 bytes as what is shown in the diagram.

## Why Push Arguments in Reverse Order?
* If push *a* first then the offset for *a* is larger than *b*, which does not make sense in assembly code.

## Function Call Chain (Previous frame pointers)

```

(High address 0xffffffff)
  |                                        |                |
   ----------------------------------------                 |
  |                                        |                | stack grows
   ----------------------------------------                 |
  |   main()'s  frame pointer              |                v
   ----------------------------------------
  |   foo()'s  frame pointer               |
   ----------------------------------------
  |                                        |
   ----------------------------------------
  |                                        |
(Low address 0x00000000)

```
