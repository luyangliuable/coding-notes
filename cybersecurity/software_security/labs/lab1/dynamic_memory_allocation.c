#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
  // Allocate space for an array with n elements
  // of integer type where n is a variable */
  const int n = 5;
  int *ptr = (int *)malloc(n * sizeof(int));
  if (ptr == NULL) {
    /* Memory could not be allocated */
  } else {
    // Allocation is done
    for (int i = 0; i < sizeof(ptr)/sizeof(int); i++) {
      printf("%i.\n", ptr[i]);
    }
    free(ptr);  /* free the associated pointer. */
    ptr = NULL; /* The set NULL value to the pointer. */
  }
  return 0;
}
