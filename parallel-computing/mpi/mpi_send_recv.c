#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  MPI_Init(&argc, &argv);

  int rank, size;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);

  int prev;
  if (rank - 1 < 0) {
    prev = size - 1;
  } else {
    prev = rank - 1;
  }

  int next = ( rank + 1 ) % size;

  int tmp;
  MPI_Status status;
  while (1) {
    MPI_Sendrecv(&rank, 1, MPI_INT, next, 0, &tmp, 1, MPI_INT, prev, 0, MPI_COMM_WORLD, &status);
    printf("Rank %i: Received from %i, sent %i.\n", rank, tmp, rank);
    sleep(1);
  }

  MPI_Finalize();
  return 0;
}
