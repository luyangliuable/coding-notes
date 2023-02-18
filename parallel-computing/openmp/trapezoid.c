#include <math.h>
#include <stdio.h>
/* #include <mpi.h> */

double f(double x);
double trapezoidBook(double a, double b, int n);

int main(int argc, char *argv[]) {
  int rank, value = 0, processorCount;

  /* MPI_Init(&argc, &argv); */

  double a = 1, b = 10, integralValue = 0;
  int n = 10;

  double result = trapezoidBook(a, b, n);
  printf("%.2f\n", result);

  /* if (rank == 0) { */
  /*   fflush(stdout); */
  /* } */
}

double f(double x) { return 1 + pow(x, 2); }

double trapezoidBook(double a, double b, int n) {

  double delta = (b - a) / (float)n;

  double area = 0.0;

  for (double x = a; x < b; x += delta) {
    area += (0.5 * delta * (f(x) - f(x + delta)));
  }

  return area;
}
