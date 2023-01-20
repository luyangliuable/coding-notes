#include <stdio.h>
#include <string.h>
#include <unistd.h>

void vul(char *str) {
  char buff[12];

  strcpy(buff, str);
}

int main(int argc, char *argv[]) {
  vul("Suspendisse potenti.");
  return 0;
}
