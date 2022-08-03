#include <stdio.h>

int main() {
  int i = 0;

  int square = 0;

  // Write a while loop here:
  while (i <= 9) {
    printf("%d\t%d\n", i, i * i);
    i++;
  }
  return 0;
}

int backwards() {
  int i = 9;

  int square = 0;

  // Write a while loop here:
  while (i >= 0) {
    printf("%d\t%d\n", i, i * i);
    i--;
  }
  return 0;
}
