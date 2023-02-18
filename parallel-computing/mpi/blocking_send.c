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
    int val = 10;
    // Blocking send blocks only during other process is receiving.
    // stuff. Tested don't need to attach buffer

    printf("Buffered sending...\n");
    MPI_Rsend(&val, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    printf("Buffered send done...\n");
  } else if (rank == 1) {
    int tmp;
    MPI_Status status;
    sleep(5);
    MPI_Recv(&tmp, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
    printf("Rank %i: Received %i.\n", rank, tmp);
  }

  MPI_Finalize();
  return 0;
}
