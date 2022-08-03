#include <stdio.h>

int main() {

  for (int i = 99; i > 0; i--) {
    printf("%d bottles of pop on the wall.\n", i);
    printf("Take one down and pass it around.\n");
    printf("%d bottles of pop on the wall.\n", i - 1);
  }

  return 0;
}
