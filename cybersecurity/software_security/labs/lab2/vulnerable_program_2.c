#include <string.h>
void foo(char *str) {
  char buffer[12];
  /* The following statement will result in buffer overflow */
  strcpy(buffer, str);
}

int main() {
  char *str = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
  foo(str);
  return 1;
}
