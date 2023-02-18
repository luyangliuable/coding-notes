#include <omp.h>
#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <stdlib.h>

double generate_rand(double lo, double hi, int decimal_place,
                     unsigned int *seed);
int main(int argc, char *argv[]) {
  int num_threads = omp_get_num_threads();
  int number[num_threads];
#pragma omp parallel
  {
    int tid = omp_get_thread_num();
    unsigned int seed = time(NULL) + tid;
    number[tid] = generate_rand(0, 10, 2, &seed);
    printf("Random number is %i.\n", number[tid]);
  }

  return 0;
}

double generate_rand(double lo, double hi, int decimal_place,
                     unsigned int *seed) {
  int precision = 100000;
  int low = (int)(lo * precision);
  int high = (int)(hi * precision);
  /* int was_neg = 0; */

  /* if ( high < 0 && low < 0) { */
  /*   was_neg = 1; */
  /*   high = -high; */
  /*   low = -low; */
  /* } */

  if (high < low) {
    double tmp = low;
    low = high;
    high = tmp;
  }

  double num = (rand_r(seed) % (high - low + 1)) + low;

  num = num / precision;

  return num;
}
