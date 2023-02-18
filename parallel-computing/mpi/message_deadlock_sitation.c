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
    int tmp;

    printf("Buffered sending...\n");
    MPI_Status status;
    /*
     * This is a simple example of deadlock in the communication. Process A
     * waiting on recv from process B and process B is waiting on receive from
     * process A.
     *
     */
    (&tmp, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, &status);
    MPI_Send(&val, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    printf("Buffered send done...\n");
  } else if (rank == 1) {
    int tmp;
    int val = 12;
    MPI_Status status;
    MPI_Recv(&tmp, 1, MPI_INT, 0, 0, MPI_COMM_WORLD, &status);
    MPI_Send(&val, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
    printf("Rank %i: Received %i.\n", rank, tmp);
  }

  MPI_Finalize();
  return 0;
}
