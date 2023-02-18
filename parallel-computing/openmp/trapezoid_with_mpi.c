#include <math.h>
#include <mpi.h>
#include <stdio.h>

double f(double x);
double trapezoidBook(double a, double b);

int main(int argc, char *argv[]) {
  int rank, value = 0, processorCount;
  int n = 10;

  MPI_Init(&argc, &argv);

  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &n);

  double a = 1, b = 10, integralValue = 0;

  /* double result = trapezoidBook(a, b, n); */
  /* printf("%.2f\n", result); */
  MPI_Aint address;
  MPI_Get_address(rank, &address);


  if (rank == 0) {
    double delta = (b - a)/n;
    printf("%i number of segments, delta is %.2f.\n", n, delta);
    double area = 0.0;
    for (int i = 1; i < n; i++) {
      double send[2] = {(float)i, delta};
      MPI_Send(&send, 2, MPI_DOUBLE, i, 0, MPI_COMM_WORLD);
    }

    for (int i = 1; i < n; i++) {
      /* double send[2] = {(float)i, delta}; */
      double tmp = 0.0;
      MPI_Status status;
      MPI_Recv(&tmp, 1, MPI_DOUBLE, i, 0, MPI_COMM_WORLD, &status);
      area += tmp;
    }

    printf("Total area is %.2f.\n", area);

  } else {
    double tmp[2];
    MPI_Status status;
    MPI_Recv(&tmp, 2, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, &status);
    double start = a + ( tmp[0] )*tmp[1];
    double end = start + tmp[1];
    double result = trapezoidBook(start, end);
    printf("Rank %i: Start is %.2f, end is %.2f. Area is %.2f.\n", rank, start, end, result);
    MPI_Send(&result, 1, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD);
    /* printf("Rank %i: Received from rank %i: %i.\n", rank, status.MPI_SOURCE, (int)tmp[0]); */
  }

  MPI_Finalize();
  return 0;
}

double f(double x) { return 1 + pow(x, 2); }

double trapezoidBook(double a, double b) {

  double area = 0.0;

  double tmp = (0.5 * (f(a) - f(b)));
  area += tmp;

  return area;
}
