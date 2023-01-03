#include <stdio.h>

typedef struct {
  int element;
} test;

int main(int argc, char *argv[]) {
  test a;
  a.element = 100;
  for (int i = 0; i < 10; i++) {
    printf("Hello world %i.\n", a.element);
  }
  return 0;
}
