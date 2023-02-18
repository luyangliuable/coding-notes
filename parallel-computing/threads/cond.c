#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

pthread_mutex_t mutx = PTHREAD_MUTEX_INITIALIZER; // NOTE: This needs to be global!
pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
int number = 0;

void *increment(void * args) {
  int *param = (int *) args;
  pthread_mutex_init(&mutx, NULL);
  pthread_mutex_lock(&mutx);
  printf("Thread %i is hogging up everything.\n", *param);
  sleep(2 + *param*2);
  number++;
  pthread_cond_signal(&cond);
  pthread_mutex_unlock(&mutx);
  printf("Hogger Thread %i is done. Number is now %i.\n", *param, number);
  return 0;
}

void *increment2(void * args) {
  const int *param = (int*) args;

  /***************************************************************************/
  /*                                   Lock                                  */
  /***************************************************************************/
  printf("Thread %i is trying to be productive.\n", *param);
  pthread_mutex_lock(&mutx);
  while(number != 2) pthread_cond_wait(&cond, &mutx);
  pthread_mutex_init(&mutx, NULL);
  number++;
  printf("Thread %i is done. Number is now %i.\n", *param, number);
    pthread_mutex_unlock(&mutx);
  /***************************************************************************/
  /*                                  Unlock                                 */
  /***************************************************************************/

  return 0;
}

int main(int argc, char *argv[])
{

  pthread_t id[10];
  int values[10];

  int id1= 0;
  int id2 = 1;
  int id3 = 2;

  pthread_create(&id[0], NULL, increment, (void * ) &id1);
  pthread_create(&id[1], NULL, increment, (void *)&id2);
  pthread_create(&id[2], NULL, increment2, (void *) &id3);
  pthread_join(id[0], NULL);
  pthread_join(id[1], NULL);
  pthread_join(id[2], NULL);

  /* printf("Final Value: %i\n", number); */
  return 0;
}
