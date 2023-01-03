#include <stdio.h>

int main(int argc, char *argv[]) {

  int a = 0;
  while (a < 10) {
    /* ... */
    a++;
    printf("%i.\n", a);
    /* cont:; */
  }

  /* do { */
  /* /\* ... *\/ */
  /* cont:; */
  /* } while (expression); */
  return 0;
}
