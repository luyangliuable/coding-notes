#include <omp.h>
#include <stdio.h>
#include <string.h>

int checkPN(int inNumber) {
  char strNumber[50];
  int len, i, rev;
  if (inNumber < 10) {
    return 1;
  } else {
    sprintf(strNumber, "%d", inNumber);
    len = strlen(strNumber);
    rev = len - 1;
    for (i = 0; i < len; i++) {
      if (strNumber[i] != strNumber[rev])
        return 0;
      rev--;
    }
    return 1;
  }
}

int main() {
  omp_set_num_threads(4);
  int i, upLimit, threadID;
  char fileName[32];
  FILE *pFile;
  printf("Enter the upper limit (> 0) of the search for palindromic numbers: ");
  scanf("%d", &upLimit);
  pFile = fopen("File_Palindromic.txt", "w");

#pragma omp parallel
  {
  int num_threads = omp_get_num_threads();
  int thread_no = omp_get_thread_num();
#pragma omp barrier

int test = -1;
#pragma omp for schedule(static)
    for (i = 0; i <= upLimit; i++) {
      /*
       * Shared Variables:
       * upLimit
       * thread_no
       * pFile
       *
       * Can be private Variables:
       * i
       */
      if (checkPN(i)) {
        fprintf(pFile, "Thread %i: %d\n", thread_no, i);
      }
    }
    fclose(pFile);
  }
  return 0;
}
