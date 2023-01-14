#include <stdio.h>
#include <stdlib.h>

int main() {
  int num, othernum;
  FILE *fptr;
  /* open a file with write mode
   *
   */
  fptr = fopen("data.txt", "w");
  // unable to open the file, handle the error here

  if (fptr == NULL) {
    printf("Error!");
    exit(1);
  }

  printf("Please enter a number : ");
  scanf("%d %d", &num, &othernum); // read data from keyboard
  fprintf(fptr, "%d", num);        // write to the file
  printf("Your other number is %i.\n", othernum);        // write to the file
  fclose(fptr);                    // close the file
  return 0;
}
