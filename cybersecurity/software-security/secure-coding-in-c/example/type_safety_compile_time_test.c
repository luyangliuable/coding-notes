/*
    File: not_type_safe.c
    Description: This program demonstrates how C can be less type-safe than other languages.
                 The program declares an int variable x and assigns it the value 5.
                 Then it assigns the address of x to a void pointer and attempts to dereference it as an int and assigns the result to y.
                 It then assigns another variable 'c' of type char to the same pointer and attempts to dereference it again as an int and assigns the result to z.
                 This program will compile and run but will produce unexpected results.

    Author: Luyang Liu
    Date: 2023-01-22T22:30:26+11:00
*/

#include <stdio.h>

int main() {
    int x = 5;
    void *ptr = &x; // Assign an integer address to a void pointer

    // Attempt to dereference the void pointer as an int
    // Works
    int y = *(int *)ptr;
    printf("x: %d, y: %d\n", x, y);

    // Now assign a different type address to the same void pointer
    char c = 'a';
    ptr = &c;

    // Attempt to dereference the void pointer as an int again
    // Won't work
    int z = *(int *)ptr;
    printf("c: %c, z: %d\n", c, z);

    return 0;
}
