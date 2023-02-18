#include <math.h>
#include <mpi.h>
#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
  MPI_Init(&argc, &argv);
  int rank, size;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);

  int time = 30 + rank * 3;
  int new_time;

  int total_sum;

  /***************************************************************************/
  /*                           With only send recv                           */
  /***************************************************************************/
  /* for (int i = 0; i < size; i++) { */
  /*   MPI_Send(&time, 1, MPI_INT, i, 0, MPI_COMM_WORLD); */
  /* } */

  /* for (int i = 0; i < size; i++) { */
  /*   if (i != rank) { */
  /*     int tmp; */
  /*     MPI_Status status; */
  /*     MPI_Recv(&tmp, 1, MPI_INT, i, 0, MPI_COMM_WORLD, &status); */
  /*     total_sum += tmp; */
  /*   } */

  /* } */

  /***************************************************************************/
  /*                          Only reduce on rank 0                          */
  /***************************************************************************/
  /* MPI_Reduce(&time, &total_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD); */

  /***************************************************************************/
  /*               Make reduction result avalaible on all ranks              */
  /***************************************************************************/
  MPI_Allreduce(&time, &total_sum, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);
  new_time = (int)((float)(total_sum + time) / (float)size);

  printf("Rank %i: %i -> %i.\n", rank, time, new_time);

  MPI_Finalize();
  return 0;
}
