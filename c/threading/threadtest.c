#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>

pthread_t tid;
void *arg;
int ret;
int check = 0;
int *checkptr = &check;
void *status;

void *start_routine() {
  *checkptr = 112;
  void * a;
  return a;
}

int test_fork() {
  ret = pthread_create(&tid, NULL, start_routine, arg);
  sleep(3);
  printf("Exiting %i.\n", *checkptr);
  exit(0);
  if (pthread_join(tid, &status) == 0) {
    sleep(1);
    printf("%i\n", *checkptr);
    return 0;
  }
}

int main() {
  int pid = fork();

  if (pid == 0) {
    test_fork();
  } else {
    sleep(4);
    printf("%i\n", *checkptr);
  }
  sleep(100);

  exit(0);
}
