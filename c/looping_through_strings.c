#include <stdio.h>
#include <string.h>

int main() {
  char s[] = "When the zombies arrive, quickly fax Judge Pat Alphabet";
  char p[] = "poolloop";
  // Checkpoint 1 code goes here
  int len = sizeof(s)/sizeof(char);
  len = strlen(s);
  for (int i = 0; i<len; i++) {
    s[i] = '*';
  }

  printf("%s\n", s);

  // Checkpoint 2 code goes here
  len = strlen(p)/2;
  for (int i = 0; i < len; i++) {
    p[i] = '#';
  }
  printf("%s", p);
}
