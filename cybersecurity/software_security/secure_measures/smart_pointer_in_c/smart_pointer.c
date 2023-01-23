#include <stdlib.h>
#include <stdio.h>

struct SimpleSmartPointer {
  int* ptr;
  /* Function pointer: deleter is a pointer to a function that takes a single argument of type int *and returns void. */
  void (*deleter)(int **);
};

void int_deleter(int ** ptr) {
  free(*ptr);
  *ptr = NULL;
}

int main() {
  // Create a new int and wrap it in a smart pointer
  struct SimpleSmartPointer myInt;
  myInt.ptr = (int*)malloc(sizeof(int));
  *myInt.ptr = 5;
  myInt.deleter = &int_deleter;

  // Use the smart pointer
  printf("Value to ptr %i: %d\n", (int) myInt.ptr, *myInt.ptr);

  // Release the memory when done
  myInt.deleter(&myInt.ptr);

  printf("Pointer to value after deleted: %i\n", myInt.ptr);

  return 0;
}
