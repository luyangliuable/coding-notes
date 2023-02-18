#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define BITS_IN_BYTE 8

void printbits(int input);

int main(int argc, char *argv[]) {
  printf("%i bits in a byte.\n", BITS_IN_BYTE);
  printf("Size of integer %ld bytes.\n", sizeof(int));
  printf("Size of float %ld bytes.\n", sizeof(float));
  printf("Size of double %ld bytes.\n", sizeof(double) );
  return 0;
}

