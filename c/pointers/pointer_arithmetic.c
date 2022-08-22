#include <stdio.h>
#include <string.h>

int main() {
  int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  char s[] = "Farmer Jack realized that big yellow quilts were expensive!!";

  int *ptr = &arr[9];

  for (int i = 0; i < 10; i++) {
    printf("%i\n", *ptr);
    ptr--;
  }

  char *ptr2 = &s[0];

  for (int i = 0; i < strlen(s); i++) {
    *ptr2 = '#';
    ptr2++;
  }

  printf("%s\n", s);
}
