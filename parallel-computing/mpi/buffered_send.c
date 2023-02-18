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
    int buffer_attached_size = MPI_BSEND_OVERHEAD + sizeof(int);
    char *buffer_attached = (char *)malloc(buffer_attached_size);
    MPI_Buffer_attach(buffer_attached, buffer_attached_size);
    // Buffered send puts the data into process two's system buffer while the process is not ready to receive.
    // So process 0 can continue on with other stuff.
    // Tested don't need to attach buffer

    printf("Buffered send...\n");
    MPI_Bsend(&val, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    printf("Buffered send done...\n");
    MPI_Buffer_detach(&buffer_attached, &buffer_attached_size);
    free(buffer_attached);
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
