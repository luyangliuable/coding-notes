#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  typedef struct {
    char *str;
  } test;

  test *t = (test *)malloc(sizeof(test));
  t->str = (char *)calloc(sizeof(char), 200);

  /* char *str; */
  /* str = (char *)malloc(20); */
  /* str = (char *)calloc(sizeof(char), 20); */
  /* str = (char *)calloc(sizeof(char), 200); */
  strcpy(t->str, "FIT3173 Software security");
  printf("String = %s\n", t->str);
  free(t);
  return (0);
}
