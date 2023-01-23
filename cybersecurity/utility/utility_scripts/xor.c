/**
 *   \file xor.c
 *
 *  Xor one string with another string
 *
 */


#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

#define MIN(x, y) (((x) < (y)) ? (x) : (y))

char* stringToBinary(char* s) {
  if(s == NULL) return 0; /* no input string */
  size_t len = strlen(s);
  char *binary = malloc(len*8 + 1); // each char is one byte (8 bits) and + 1 at the end for null terminator
  binary[0] = '\0';
  for(size_t i = 0; i < len; ++i) {
    char ch = s[i];
    for(int j = 7; j >= 0; --j){
      if(ch & (1 << j)) {
        strcat(binary,"1");
      } else {
        strcat(binary,"0");
      }
    }
  }
  return binary;
}


int main(int argc, char *argv[])
{
  char *str1 = (char *) malloc(strlen(argv[1]));
  char *str2 = (char *) malloc(strlen(argv[2]));
  strncpy(str1, argv[1], strlen(argv[1]));
  strncpy(str2, argv[2], strlen(argv[2]));

  int minLength = MIN(strlen(argv[1]), strlen(argv[2]));

  char *output = (char *) malloc(minLength);

  for (int i = 0; i < minLength; i++) {
    output[i] = str1[i] ^ str2[i];
  }

  printf("%s\n", stringToBinary(str1));
  printf("%s\n", stringToBinary(str2));
  printf("%s\n", stringToBinary(output));


  return 0;
}
