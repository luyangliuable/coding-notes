#include <stdio.h>

int main() {

  int evens[] = {2, 4, 6, 8, 10, 12};
  int odds[] = {1, 4, 5, 7, 10, 11}; // Do not modify this line.

  printf("%i\n", evens[5]); // Checkpoint 1. Fix this error.

  // Code for checkpoint 2 goes here.
  printf("%d\n", evens[2]); // TODO What is the different between %d and %i?

  // Code for checkpoint 3 goes here.
  odds[1] = 3;
  odds[4] = 9;
  return 0;
}
