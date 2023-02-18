#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>
typedef struct {
  int id;
  int min;
  int max;
  int arr[10];
} thread_args;

void * threaded_task(void * threaded_args) {
  thread_args *params = ( thread_args * ) threaded_args;
  params->max = 1000;
  printf("working %i, %i. \n", params->max, params->id);
}
int main(int argc, char *argv[]){

  thread_args arguments;
  arguments.min = 0;
  arguments.max = 10;
  int number_of_threads = 2;

  thread_args retval;
  pthread_t thread_id;

  for (int i = 0; i < 10; i++) {
    arguments.id=thread_id;
    pthread_create(&thread_id, NULL, threaded_task, (void *) &arguments);
  }

  pthread_join(thread_id, NULL);
  printf("%i.\n", arguments.max);
  exit(0);
}

