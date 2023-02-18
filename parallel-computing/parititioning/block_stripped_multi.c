
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

  int rank, size;
  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  double A[SIZE][SIZE] = {{1, 2}, {3, 4}};
  double B[SIZE][SIZE] = {{5, 6}, {7, 8}};

  double ans[SIZE][SIZE];


  double *send_a = malloc(sizeof(double) * SIZE * 2 * 2);
  double *send_b = malloc(sizeof(double) * SIZE * 2 * 2);

  if (rank == 0) {
    // Row

    /* for (int k = 0; k < 2; k++) { */
    for (int k = 0; k < 2; k++) {
      for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
          int idx = i + 2 * j + 2 * 2 * k;
          send_a[i + 2 * j + 2 * 2 * k] = A[k][i];
          /* printf("Rank %i (%i, %i): idx %i %.2f\n", rank, i, j, idx, */
          /*        send_a[idx]); */
        }
      }
    }

    // Column
    for (int k = 0; k < SIZE; k++) {
      for (int j = 0; j < SIZE; j++) {
        for (int i = 0; i < SIZE; i++) {
          int idx = k * SIZE * SIZE + j * SIZE + i;
          send_b[idx] = B[i][j];
          /* printf("Rank %i (%i, %i): idx %i %.2f\n", rank, i, j, idx, */
          /*        send_b[j * 2 + i]); */
        }
      }
    }
  }

  double tmp_row[SIZE];
  double tmp_col[SIZE];

  MPI_Scatter(send_a, SIZE, MPI_DOUBLE, &tmp_row, SIZE, MPI_DOUBLE, 0,
              MPI_COMM_WORLD);
  MPI_Scatter(send_b, SIZE, MPI_DOUBLE, &tmp_col, SIZE, MPI_DOUBLE, 0,
              MPI_COMM_WORLD);

  double cell_result = 0;
  for (int i = 0; i < SIZE; i++) {
    /* printf("Rank %i: multi %.2f %.2f.\n", rank, tmp_row[i], tmp_col[i]); */
    cell_result += tmp_row[i] * tmp_col[i];
  }

  printf("Rank %i: %.2f.\n", rank, cell_result);

  MPI_Finalize();
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
