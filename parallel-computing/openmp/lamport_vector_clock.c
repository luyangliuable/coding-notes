#include <math.h>
#include <mpi.h>
#include <stdio.h>
#include <unistd.h>

int *get_vector_clock(int *prev, int no_of_msg, int current_rank, int size);
void print_v(int *vector, int size);

int main(int argc, char *argv[]) {
  MPI_Init(&argc, &argv);

  int rank, size;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);

  if (rank == 0) {
    int namelen;
    char processor_name[MPI_MAX_PROCESSOR_NAME];
    MPI_Get_processor_name(processor_name, &namelen);
    printf("Processor name is %s.\n", processor_name);
  }

  int vector_clock[size];
  int no_of_messages = 1;

  for (int i = 0; i < size; i++)
    vector_clock[i] = 0;

  get_vector_clock(vector_clock, no_of_messages, rank, size);

  MPI_Finalize();
  return 0;
}

int *get_vector_clock(int *prev, int no_of_msg, int current_rank, int size) {
  prev[current_rank] = no_of_msg;

  /* printf("<"); */
  /* for (int i = 0; i < size; i++) { */
  /*   printf("%i", prev[i]); */
  /*   if (i != size - 1) { */
  /*     printf(", "); */
  /*   } */
  /* } */
  /* printf(">\n"); */

  return prev;
}

void print_v(int *vector, int size) {
  printf("<");
  for (int i = 0; i < size; i++) {
    printf("%i", vector[i]);
    if (i != size - 1) {
      printf(", ");
    }
  }
  printf(">\n");
}
