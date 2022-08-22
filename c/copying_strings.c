#include <stdio.h>
#include <string.h>

int main() {

  char src[] = "banana";
  char dst[7];

  char pan[] = "How vexingly quick daft zebras jump!";
  int len = 0; // Checkpoint 2
  char dst2[len];

  // Code for checkpoint 1 goes here
  // strcpy(dst, src) copies dst string into empty src.
  strcpy(src, dst);
  printf("%s\n", dst);

  // Code for checkpoint 3 goes here

  printf("%s", dst2);
}
