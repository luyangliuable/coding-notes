#include <stdio.h>

struct Person {
  char name[40];
  int age;
};

int main(void) {
  struct Person person1 = {"Martin", 57};
  struct Person person2 = {"Michelle", 27};
  // Write your code below
  struct Person *person1Pointer = &person1;
  struct Person *person2Pointer = &person2;
  ( *person1Pointer ).age++;
  person2Pointer->age += 10;

  printf("Hello my name is %s and I am %d years old.\n", person1.name,
         person1.age);
  printf("Hello my name is %s and I am %d years old.\n", person2.name,
         person2.age);
}
