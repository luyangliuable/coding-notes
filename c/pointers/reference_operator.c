#include <stdio.h>

int main() {
  // Reference pointer is &

  double g = 9.81;
  double pi = 3.14;
  double *dblPtr;

  // Checkpoint 1 code goes here.
  dblPtr = &g;

  // Checkpoint 2 code goes here.
  printf("%p\n", dblPtr);

  // Pointer of a pointer wtf
  printf("%p", &dblPtr);

  // Checkpoint 3 code goes here.
  dblPtr = &pi;
}
