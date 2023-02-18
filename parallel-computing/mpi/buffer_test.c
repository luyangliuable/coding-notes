#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  MPI_Init(&argc, &argv);

  int rank, size;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);

  if (rank == 0) {
    int *val = malloc(sizeof(int) * 100);
    for (int i = 0; i < 100; i++)
      val[i] = 10;

    printf("Buffered send...\n");
    MPI_Request request;
    MPI_Status status;
    MPI_Isend(val, 100, MPI_INT, 1, 0, MPI_COMM_WORLD, &request);
    free(val);
    /* val = 10000; */
    sleep(10);
    MPI_Wait(&request, &status);
  } else if (rank == 1) {
    int tmp[100];
    /* sleep(5); */
    MPI_Request request;
    MPI_Status status;
    MPI_Irecv(&tmp, 100, MPI_INT, 0, 0, MPI_COMM_WORLD, &request);
    sleep(5);
    MPI_Wait(&request, &status);
    printf("Rank %i: Received %i.\n", rank, tmp[99]);
  }

  MPI_Finalize();
  return 0;
}
