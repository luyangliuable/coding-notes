#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

pthread_mutex_t mutx; // NOTE: This needs to be global!
int number = 0;

void *increment(void * args) {
  int* param = (int*) args;

  /***************************************************************************/
  /*                                   Lock                                  */
  /***************************************************************************/
  pthread_mutex_init(&mutx, NULL);
  pthread_mutex_lock(&mutx);
  int tmp = *param;
  tmp++;
  *param = tmp;
  pthread_mutex_unlock(&mutx);
  /***************************************************************************/
  /*                                  Unlock                                 */
  /***************************************************************************/

  printf("%i\n", *param);
  return param;
}

int main(int argc, char *argv[])
{

  pthread_t id[10];

  for (int i = 0; i < 10; i ++) {
    pthread_create(&id[i], NULL, increment, (void * ) &number);
    /* pthread_join(id[i], NULL); */
  }

  printf("Waiting for all threads to finish.\n");
  for (int i = 0; i < 10; i++) {
    pthread_join(id[i], NULL);
    /* pthread_join(id[i], NULL); */
  }

  printf("Final Value: %i\n", number);
  return 0;
}
