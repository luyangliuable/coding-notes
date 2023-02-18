#include <mpi.h>
#include <stdio.h>

#define TIME_SERVER 0

int main(int argc, char *argv[]) {
  double start_time = MPI_Wtime(); // Initialise time clock
  double time = 0.;
  double start_request = 0.;
  double round_trip_time = 0.;
  double time_buffer = 0.;
  int numtasks, rank, rc;
  int send_buffer = 1;
  int receive_buffer;
  int time_request = 1;
  int time_reply = 2;

  // Initialise MPI environment
  MPI_Status stat;

  MPI_Init(&argc, &argv);
  MPI_Comm_size(MPI_COMM_WORLD, &numtasks);
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  // Central time server process
  if (rank == TIME_SERVER) {
    // Synthetic loop expecting to receive
    // synchronisation requests from all
    // remaining processes
    for (int i = 0; i < numtasks - 1; i++) {
      rc = MPI_Recv(&receive_buffer, 1, MPI_INT, MPI_ANY_SOURCE, time_request,
                    MPI_COMM_WORLD, &stat);

      // Current time is now - start
      time = MPI_Wtime() - start_time;

      rc = MPI_Send(&time, 1, MPI_DOUBLE, stat.MPI_SOURCE, time_reply,
                    MPI_COMM_WORLD);
    }
  }
  // Remaining processes synch with the time server
  else {
    start_request = MPI_Wtime();
    rc = MPI_Send(&send_buffer, 1, MPI_INT, TIME_SERVER, time_request,
                  MPI_COMM_WORLD);
    rc = MPI_Recv(&time_buffer, 1, MPI_DOUBLE, TIME_SERVER, time_reply,
                  MPI_COMM_WORLD, &stat);

    time = MPI_Wtime();
    round_trip_time = time - start_request; // Calculate round trip time for use
                                            // with Cristian's algorithm

    printf(
        "Setting time to ----------> %f, \nRank %i thought it should be %f\n",
        time_buffer + 0.5 * round_trip_time, rank, time - start_time);
  }

  MPI_Finalize();

  return 0;
}
