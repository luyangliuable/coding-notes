/**
 *   \file sequential_multi.c
 *   \brief Finds the matrix dot product of A and B using FOX method
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

  double tmp[SIZE][SIZE];

  // tmp matrix for shifting B rows up each iteration
  for (int i = 0; i < SIZE; i++)
    for (int j = 0; j < SIZE; j++)
      tmp[i][j] = B[i][j];

  double ans[SIZE][SIZE];

  double *send_a = malloc(sizeof(double) * SIZE * 2 * 2);
  double *send_b = malloc(sizeof(double) * SIZE * 2 * 2);

  double tmp_row[SIZE];
  double tmp_col[SIZE];

  int steps = 2;

  if (rank == 0) {
    for (int step = 0; step < steps; step++) {
      /***********************************************************************/
      /*                   Rotate block up by step block up                  */
      /***********************************************************************/

      for (int k = 0; k < step; k++) {
        for (int i = 0; i < SIZE; i++) {
          for (int j = 0; j < SIZE; j++) {
            tmp[( i+1 ) % SIZE][j] = B[i][j];
          }
        }
      }

      for (int i = 0; i < SIZE; i++) {
        // inner loop for column
        for (int j = 0; j < 2; j++) {
          printf("%.2f ", tmp[i][j]);
        }
        printf("\n"); // new line
      }
      printf("\n"); // new line

      for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
          int idx = (i + (step * SIZE) / 2) % SIZE;
          /* printf("%i, %i\n", idx, idx); */
          double send[3] = {A[i][j], tmp[i][j], A[i][idx]};
          MPI_Send(&send, 3, MPI_DOUBLE, 1 + i + j * SIZE, 0, MPI_COMM_WORLD);
        }
      }
    }
  } else {
    double curr_cell_result = 0;
    for (int step = 0; step < steps; step++) {
      /* MPI_Barrier(MPI_COMM_WORLD); */
      /* if (rank == 1) */
      /*   printf("---------------------------\n"); */
      MPI_Status status[size - 1];
      double recv[3];
      MPI_Recv(&recv, 3, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, &status[rank - 1]);
      printf("Step %i Rank %i: %.2f, %.2f, %.2f.\n", step, rank, recv[0], recv[1],
             recv[2]);
      curr_cell_result += recv[1] * recv[2];
      printf("Step %i Rank %i: %.2f.\n", step, rank, curr_cell_result);
    }
  }

  /* double cell_result = 0; */
  /* for (int i = 0; i < SIZE; i++) { */
  /*   /\* printf("Rank %i: multi %.2f %.2f.\n", rank, tmp_row[i], tmp_col[i]);
   */
  /* *\/ */
  /*   cell_result += tmp_row[i] * tmp_col[i]; */
  /* } */

  /* printf("Rank %i: %.2f.\n", rank, cell_result); */

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
