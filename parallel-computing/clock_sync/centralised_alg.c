#include <mpi.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define COORDINATOR 0

int main(int argc, char *argv[]) {
  double start_time = MPI_Wtime();
  double time = 0.;
  double start_request = 0.;
  double round_trip_time = 0.;
  double time_buffer = 0.;
  int numtasks, rank, rc;
    sleep(2);

    // Let the coordinator know we have finished with the
    // critical section
    rc = MPI_Send(&send_buffer, 1, MPI_INT, COORDINATOR, mutex_release,
                  MPI_COMM_WORLD);
  }

  MPI_Finalize();

  return 0;
