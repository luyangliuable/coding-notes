#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void repeatDigit(int);
int getRandomNumber(int);

// Define prototypes above
// the function definitions
void repeatDigit(int repetitions) {
  int digit = getRandomNumber(9);
  for (int i = 0; i < repetitions; i++) {
    printf("%d ", digit);
  }
  printf("\n");
}

int getRandomNumber(int maxNumber) {
  int randomNumber = rand() % maxNumber + 1;
  return randomNumber;
}

int main(void) {
  srand(time(NULL));
  int repetitions = getRandomNumber(10);
  repeatDigit(repetitions);
}
