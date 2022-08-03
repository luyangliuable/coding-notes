#include <stdio.h>

/* symbol type */
/* % d or % i int*/
/*% f double or float */
/* % c char */

int main() {

  int ageLearnedToRide = 5;

  printf("I was %d years old when I learned to ride a bike.\n",
         ageLearnedToRide);
  printf("I hope I still remember how to ride.");
}

int initialisation() {
  int numOfBooks;
  char favLetter;
  char favDigit;
  double costOfCandyBar;

  numOfBooks = 112;
  favLetter = 'z';
  favDigit = '2';
  costOfCandyBar = 2.221231;

  printf("Number of books: %d\n", numOfBooks);
  printf("Your Favorite Letter is: %c\n", favLetter);
  printf("Your Favorite Digit is: %c\n", favDigit);
  printf("You expect to pay $%.2f for a candy bar.\n", costOfCandyBar);
}
