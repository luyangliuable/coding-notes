#include <stdlib.h>

struct SimpleSmartPointer {
  int* ptr;
  void (*deleter)(int*);
};

void int_deleter(int* ptr) {
  free(ptr);
}

int main() {
  // Create a new int and wrap it in a smart pointer
  struct SimpleSmartPointer myInt;
  myInt.ptr = (int*)malloc(sizeof(int));
  *myInt.ptr = 5;
  myInt.deleter = &int_deleter;

  // Use the smart pointer
  printf("Value: %d\n", *myInt.ptr);

  // Release the memory when done
  myInt.deleter(myInt.ptr);
  return 0;
}
