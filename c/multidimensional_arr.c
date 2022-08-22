#include <stdio.h>

int main() {

  // Checkpoint 1 code goes here.
  int arr[9][9];

  // Checkpoint 2 code goes here.
  int matrix1[3][3] = {{2,9,11}, {3,1,4}, {8,3,1}};



  /* Element Access in multidimensional arrays */
  int matrix[][4] = {
      {14, 10, 6, 4}, {3, 7, 18, 11}, {13, 9, 5, 17}, {19, 12, 2, 1}};

  // 4th row 2nd column of matrix
  printf("%i\n", matrix[3][1]);

  int r = sizeof(matrix)/sizeof(matrix[0]);
  int l = sizeof(matrix[0]) / sizeof(int);

  int sum = 0;
  for (int i = 0; i < r; i++){
    for (int j = 0; i < l; i++){
      sum += matrix[i][j];
    }
  }

  return 0;
}
