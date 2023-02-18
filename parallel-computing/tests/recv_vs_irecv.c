#include <mpi.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define COORDINATOR 0

int main(int argc, char *argv[]) {
  // Initialise MPI environment
  MPI_Status stat[4];
  MPI_Status tmp[4];
  MPI_Request reqs[4];
  int send_buffer = 1123123;
  int receive_buffer[3] = {0, 0, 0};
  int numtasks, rank, rc;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  if (numtasks == 3) {
    if (rank == COORDINATOR) {
      rc = MPI_Isend(&send_buffer, 1, MPI_INT, 2, 2, MPI_COMM_WORLD, &reqs[0]);
      MPI_Wait(&reqs[0], &tmp[0]);
      rc = MPI_Irecv(&receive_buffer[0], 1, MPI_INT, 2, 1, MPI_COMM_WORLD,
                     &reqs[1]);
      MPI_Wait(&reqs[1], &tmp[1]);
      printf("Sending to task 2 with asynchronous send complete %i.\n",
             receive_buffer[0]);
      rc = MPI_Send(&send_buffer, 1, MPI_INT, 1, 1, MPI_COMM_WORLD);
      printf("Sending to task 1 with synchronous send complete.\n");
    } else if (rank == 1) {
      rc = MPI_Recv(&receive_buffer[1], 1, MPI_INT, COORDINATOR, 1,
                    MPI_COMM_WORLD, &stat[1]);
      printf("process %i finished. Received %i.\n", rank, receive_buffer[1]);

    } else {
      rc = MPI_Irecv(&receive_buffer[2], 1, MPI_INT, COORDINATOR, 2,
                     MPI_COMM_WORLD, &reqs[2]);
      MPI_Wait(&reqs[2], &tmp[2]);
      rc = MPI_Isend(&rank, 1, MPI_INT, COORDINATOR, 1, MPI_COMM_WORLD,
                     &reqs[3]);
      MPI_Wait(&reqs[3], &tmp[3]);
      printf(
          "process %i finished. Received %i, source is %i and error is %i.\n",
          rank, receive_buffer[2], tmp[2].MPI_SOURCE, tmp[2].MPI_ERROR);
    }
  } else {
    printf("Needs 3 tasks not %i tasks.\n", numtasks);
  }

  /* MPI_Waitall(sizeof(reqs)/sizeof(MPI_Request), reqs, tmp); */

  MPI_Finalize();
  exit(EXIT_SUCCESS);
}
