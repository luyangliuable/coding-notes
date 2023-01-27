#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <sys/file.h> /* change to <sys/fcntl.h> for System V */
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

void foo(char *str) {
  char buffer[15]; // Fix by making the buffer larger
  /* The following statement will result in buffer overflow */
  if (strlen(str) > 15) {
    char *errMsg = "Error: String too long to fit inside buffer.\n";
    write(2, errMsg, strlen(errMsg));
    exit(1);
  }
  strcpy(buffer, str);
  /* printf("%i.\n", stdout); */
  /* fprintf(stdout, "%s\n", buffer); */
  write(1, buffer, strlen(buffer));
}

int main() {
  char *str = "This is definitely longer than 12.\n";
  str = "Works!\n";
  foo(str);
  return 1;
}
