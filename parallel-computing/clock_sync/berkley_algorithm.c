#include <math.h>
#include <mpi.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  MPI_Init(&argc, &argv);

  int rank, size;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);


  if (rank == 0) {
    int hour = 12;
    int minute = 50;
    MPI_Status status[size];

    int sum = minute;
    for (int i = 1; i < size; i++) {
      int tmp;
      MPI_Recv(&tmp, 1, MPI_INT, i, 0, MPI_COMM_WORLD, &status[rank]);
      printf("%i.\n", tmp);
      sum += tmp;
    }

    double new_average = ((double)sum) / ((float)size);


    printf("Rank %i: The average time is %.2f.\n", rank, new_average);
    for (int i = 1; i < size; i++) {
      MPI_Send(&new_average, 1, MPI_DOUBLE, i, 0, MPI_COMM_WORLD);
    }

  } else {
    int hour = 12;
    double new_minute;
    MPI_Status status[size];
    int minute = 50 + rank * 2;
    MPI_Send(&minute, 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
    MPI_Recv(&new_minute, 1, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, &status[rank]);
    printf("Rank %i: %i -> %i\n", rank, minute, (int)new_minute);
  }

  MPI_Finalize();
  return 0;
}
