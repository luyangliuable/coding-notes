#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
  srand(time(NULL));
  // Generate a number between 1 and 20 so add 1.
  int randomNumber = rand() % 20 + 1;

  printf("%i", randomNumber);
}
