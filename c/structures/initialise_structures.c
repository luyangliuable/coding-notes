#include <stdio.h>

int main(void) {
  struct Person {
    char firstName[25];
    // Write your code below
    char lastName[40];
    int age;
  };

  // Write your code below
  struct Person person1 = {"Ada", "Lovelace", 28};
  struct Person person2 = {"Marie", "Curie", 44};
}
