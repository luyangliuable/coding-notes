#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  int rank, value = 0, p;
  double *pU = NULL, *pA = NULL, *pT = NULL, *pV = NULL;
  int dataCount = 0;
  MPI_Status status;

  MPI_Init(&argc, &argv);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &p);

  switch (rank) {
  case 0: // MPI process node 0
  {
    // Open file
    char *filename = "u_a.txt";
    FILE *fp = fopen(filename, "r+");
    int number_of_elements;
    fscanf(fp, "%i\n", &number_of_elements);
    printf("Rank %i: Num of elements %i.\n", rank, number_of_elements);
    char *tmp;
    fscanf(fp, "%s %s\n", &tmp, &tmp);
    double u[number_of_elements];
    double a[number_of_elements];
    for (int i = 0; i < number_of_elements; i++) {
      fscanf(fp, "%lf %lf\n", &u[i], &a[i]);
    }
    int work_each_process = number_of_elements / (p - 2);

    for (int i = 0; i < p-2; i++) {
      double *send_vals_u = malloc(sizeof(double) * work_each_process);
      double *send_vals_a = malloc(sizeof(double) * work_each_process);

      for (int j = 0; j < work_each_process; j++) {
        /* int tmp = i % number_of_elements; */
        send_vals_u[j] = u[i * work_each_process + j];
        send_vals_a[j] = a[i * work_each_process + j];
        printf("Rank %i: %.2f, %.2f\n", rank, send_vals_a[j], send_vals_u[j]);
      }

      MPI_Send(&work_each_process, 1, MPI_INT, i+2, 0, MPI_COMM_WORLD);

      printf("Rank %i: Sending %.2f, %.2f to rank %i.\n", rank, send_vals_a[0], send_vals_u[0], i+2);
      MPI_Send(send_vals_u, work_each_process, MPI_DOUBLE, i+2, 0, MPI_COMM_WORLD);
      MPI_Send(send_vals_a, work_each_process, MPI_DOUBLE, i+2, 0, MPI_COMM_WORLD);
    }
    break;
  }
  case 1: // MPI process node 1
  {
    char *filename = "t.txt";
    FILE *fp = fopen(filename, "r+");
    int number_of_elements;
    fscanf(fp, "%i\n", &number_of_elements);
    printf("Rank %i: Num of elements %i.\n", rank, number_of_elements);
    char *tmp;
    fscanf(fp, "%s\n", &tmp);
    double t[number_of_elements];
    for (int i = 0; i < number_of_elements; i++) {
      fscanf(fp, "%lf\n", &t[i]);
      printf("Rank %i: t at %i is %.2f.\n", rank, i, t[i]);
    }

    int work_each_process = number_of_elements / (p - 2);

    for (int i = 0; i < p-2; i++) {
      double *send_vals = (double *)malloc(sizeof(double) * work_each_process);
      for (int j = 0; j < work_each_process; j++) {
        send_vals[j] = t[i * work_each_process + j];
      }
      printf("Rank %i: Sending t: %.2f\n", rank, send_vals[0]);
      MPI_Send(send_vals, work_each_process, MPI_DOUBLE, i+2, 0, MPI_COMM_WORLD);
    }
    break;
  }
  default: // Remaining MPI process nodes
  {

    MPI_Status status[4];
    char *filename = "results.txt";
    FILE *fp = fopen(filename, "a+");
    int work_each_process;
    MPI_Recv(&work_each_process, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &status[0]);
    printf("Rank %i: Work each process %i.\n", rank, work_each_process);

    pT = malloc(sizeof(double) * work_each_process);
    pU = malloc(sizeof(double) * work_each_process);
    pA = malloc(sizeof(double) * work_each_process);
    pV = malloc(sizeof(double) * work_each_process);

    MPI_Recv(pU, work_each_process, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, &status[1]);
    MPI_Recv(pA, work_each_process, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, &status[2]);
    MPI_Recv(pT, work_each_process, MPI_DOUBLE, 1, 0, MPI_COMM_WORLD, &status[3]);

    for (int i = 0; i < work_each_process; i++)
      printf("Rank %i: u: %.2f, a: %.2f.\n", rank, pU[i], pA[i]);
    /* MPI_Recv(&t, work_each_process, MPI_DOUBLE, 1, 0, MPI_COMM_WORLD, &status[3]); */

    for (int i = 0; i < work_each_process; i++) {
      pV[i] = pU[i] + pA[i] * pT[i];
      fprintf(fp, "%.2f\n", pV[i]);
    }

    /* sleep(100); */
    break;
  }
  }
  MPI_Finalize();
  free(pU);
  free(pA);
  free(pV);
  return 0;
}
