#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
  sem_t *sem1 = sem_open("/fit2100sem1", O_CREAT | O_EXCL, S_IRUSR | S_IWUSR, 1);
  if (sem1 == SEM_FAILED) {
    perror("Semaphore");
    exit(1);
  };

  sem_t *sem2 = sem_open("/fit2100sem2", O_CREAT | O_EXCL, S_IRUSR | S_IWUSR, 1);
  if (sem2 == SEM_FAILED) {
    perror("Semaphore");
    exit(1);
  };

  printf("Process 1 is seeking to enter critical section...\n\n");

  sem_wait(sem1);
  sleep(1);
  sem_wait(sem2);

  printf("Process 1 in critical section. \n");
  for (int i =0; i < 10; i++) {
    sleep(1);
    printf("%i\n", i);
  }

  printf("Process 1 leaving critical section. \n");
  sem_post(sem2);
  sem_post(sem1);

  /* close the smephamores */

  sem_close(sem1);
  sem_close(sem2);
  printf("Process 1 finished.\n");

}


