#include <stdio.h>

int main(int argc, char *argv[]) {
  int x[12];       // define an array for 4 elements only
  int *px = &x[0]; // let the pointer px to point to x[0]

  *px = 0;         // this is equivalent to x[0] = 0;
  *(px + 1) = 1;   // this is equivalent to x[1] = 1;
  *(px + 2) = 2;   // this is equivalent to x[2] = 2;
  *(px + 3) = 3;   // this is equivalent to x[3] = 3;
  *(px + 4) = 124; // this is equivalent to x[4] = 4;
  *(px + 10) = 10; // what would happen if this statement is

  /* printf("%i.\n", x[10]); */

  int *ptr = &x[0];

  /* ptr += 1000; */ // If the number gets to high causes segmentation fault.

  for (int i = 0; i < 5; i++) {
    // Iterating through an array using pointers.
    printf("%i\n", *ptr);
    ptr++;
  }

  return 0;
}
