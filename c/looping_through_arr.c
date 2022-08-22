#include <stdio.h>

int main() {
  int arr[] = {3,  4,  5,  6,  7,  8,  9,  10, 11, 12,
               13, 14, 15, 16, 17, 20, 22, 26, 28, 29};
  int arr2[100];

  // Code for Checkpoint 1 goes here
  for (int i=0; i<20; i++) {
    printf('%i\n', arr[i]);
  }

  Code for Checkpoint 2 goes here
  for (int x = 0; x < 100; x++) {
    arr2[x] = x + 4;
  }

  return 0;
}
