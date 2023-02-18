#include <math.h>
#include <omp.h>
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

#pragma parallel for shared(area)
  {
    for (double x = a; x < b; x += delta) {
      double tmp = (0.5 * delta * (f(x) - f(x + delta)));
#pragma critical
      { area += tmp; }
    }
  }

  return area;
}
