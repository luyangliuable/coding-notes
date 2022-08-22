#include <stdio.h>

// Write your code below
void incrementAge(int* agePointer) {
  *agePointer += 1;
}


int main(void) {
  int age = 12;
  incrementAge(&age);

  printf("%i\n", age);
  return age;
}
