/**
 *   \file sequential_multi.c
 *   \brief Finds the matrix dot product of A and B
 *
 *  Code writen by Luyang Liu CopyRight
 *
 */

#include <math.h>
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int printm(int size, double ***arr);

int main(int argc, char *argv[]) {
#define SIZE 2
  /* double **A = (double**) malloc(sizeof(double*) * SIZE); */

  /* for (int i = 0; i < SIZE; i ++) { */
  /*   *A = ( double* ) malloc(sizeof(double) * SIZE); */
  /* }; */

  /* double A[SIZE][SIZE] = {{2, 2}, {2, 2}}; */
  /* double B[SIZE][SIZE] = {{3, 3}, {3, 3}}; */

  double A[SIZE][SIZE] = {{1, 2}, {3, 4}};
  double B[SIZE][SIZE] = {{5, 6}, {7, 8}};

  double ans[SIZE][SIZE];

  /***************************************************************************/
  /*                     Sequential matrix multiplication                     */
  /***************************************************************************/
  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < SIZE; j++) {
      ans[i][j] = 0;
      for (int k = 0; k < SIZE; k++)
        ans[i][j] += A[i][k] * B[k][j];
    }
  }

  for (int i = 0; i < SIZE; i++) {
    for (int j = 0; j < 2; j++) {
      printf("%.2f ", ans[i][j]);
    }
    printf("\n"); // new line
  }

  return 0;
}

int printm(int size, double ***arr) {
  // declare and initialize an array
  /* int arr[2][2] = {{50, 60}, {70, 80}}; */

  // display 2x2 matrix using for loop
  printf("The matrix elements are:\n");

  // outer loop for row
  for (int i = 0; i < size; i++) {
    // inner loop for column
    for (int j = 0; j < 2; j++) {
      printf("%.2f ", *arr[i][j]);
    }
    printf("\n"); // new line
  }

  return 0;
}
