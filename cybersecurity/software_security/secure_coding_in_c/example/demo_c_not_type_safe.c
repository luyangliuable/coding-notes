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
