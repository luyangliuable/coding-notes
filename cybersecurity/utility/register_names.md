# List of Register Names and Their Purpose

* **EAX (Accumulator Register):** used for arithmetic and logical operations
* **EBX (Base Register):** used as a base pointer for memory access
* **ECX (Counter Register):** used as a counter for loops and string operations
* **EDX (Data Register):** used for arithmetic and logical operations, as well as I/O operations
* **EBP (Base Pointer):** used as a base pointer for stack access
* **ESP (Stack Pointer):** used as a pointer to the top of the stack
* **EIP (Instruction Pointer):** used as a pointer to the current instruction being executed
* **EFLAGS (Flags Register):** used to store information about the state of the processor, such as the results of arithmetic and logical operations
* **ECS (Code Segment Register):** used to store the base address of the code segment
* **EDS (Data Segment Register):** used to store the base address of the data segment
* **ESS (Stack Segment Register):** used to store the base address of the stack segment
* **EFS (F Segment Register):** used to store the base address of the FPU data segment
* **GS (GS Segment Register):** used to store the base address of the thread-local storage segment
* **FS (FS Segment Register):** used to store the base address of the thread-local storage segment

ESP register is decremented to reserve space on the stack, and when deallocating space for a stack frame, the ESP register is incremented to release the reserved space. This is typically done using the "SUB ESP, value" and "ADD ESP, value" assembly instructions, where value is the number of bytes of space to reserve or release.

ESP (Extended Stack Pointer) is the register that holds the memory address of the end of the stack frame. When allocating space for a new stack frame, the ESP register is decremented by the amount of space needed. When deallocating space for a stack frame, the ESP register is incremented by the same amount, effectively removing the space that was previously allocated. This is done using the instruction "SUB ESP, [value]" to allocate space and "ADD ESP, [value]" to deallocate space.

When creating a new stack frame, the current value of the stack pointer (ESP) is saved in the base pointer (EBP) register, and then the stack pointer is adjusted to create space for the new stack frame. This is typically done by subtracting the desired amount of space from ESP. This operation is also known as "pushing" the stack frame. Once the function execution is complete, the stack pointer is then adjusted again by adding the same amount of space that was subtracted earlier, this operation is also known as "popping" the stack frame. The base pointer is then restored to its original value, which is now stored in the stack pointer, thus returning the stack to its original state.
