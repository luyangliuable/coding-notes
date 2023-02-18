#include <mpi.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#define COORDINATOR 0

int main(int argc, char *argv[]) {
  // Initialise MPI environment
  MPI_Status stat;
  int send_buffer = 1123123;
  int receive_buffer;
  int numtasks, rank, rc;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  if (numtasks == 3) {
    if (rank == COORDINATOR) {
      for (int i = 1; i < numtasks; i++) {
        rc = MPI_Send(&send_buffer, 1, MPI_INT, i, 1, MPI_COMM_WORLD);
      }
      printf("process %i finished.\n", rank);
    } else if (rank == 1) {
      rc = MPI_Recv(&receive_buffer, 1, MPI_INT, COORDINATOR, 1, MPI_COMM_WORLD,
                    &stat);
      printf("%i.\n", receive_buffer);
      printf("process %i with tag %i finished.\n", rank, 1);
    } else {
      printf("process %i with different tag %i is starting. Because it has a "
             "different tag it will never receive anything\n",
             rank, 2);
      rc = MPI_Recv(&receive_buffer, 1, MPI_INT, COORDINATOR, 2, MPI_COMM_WORLD,
                    &stat);
      printf("%i.\n", receive_buffer);
      printf("process %i with tag %i finished.\n", rank, 2);
    }
  } else {
    printf("Not enough tasks %i.\n", numtasks);
  }

  MPI_Finalize();
  exit(EXIT_SUCCESS);
}
