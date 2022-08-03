#include <stdio.h>
#include <math.h>

int main() {

  int guess;
  int tries = 0;

  printf("I’m thinking of a number in the range 1-10.\n");
  printf("Try to guess it: ");
  scanf("%d", &guess);

  // Write a while loop here:
  while (guess != 8 && tries < 50) {
    tries++;
    printf("Wrong guess try again please\n");
    scanf("%d", &guess);
  }

  if (guess == 8) {
    printf("You got it!\n");
  }
}


