#include <pthread.h>
#include <stdio.h>
#include <unistd.h>
#define NUM_THREADS 2

// Global variables
pthread_mutex_t g_Mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t g_Cond = PTHREAD_COND_INITIALIZER;
int g_Val = 0;

// Thread 1 Callback Function
void *Thread1Func(void *pArg) {
  int *p = (int *)pArg;
  int myNum = *p; // myNum = 0

  sleep(2);

  pthread_mutex_lock(&g_Mutex);
  printf("Thread Id: %d. Global value before updated by Thread2Func: %d\n",
         myNum, g_Val);

  while(g_Val < 3) {
    pthread_cond_wait(&g_Cond, &g_Mutex);
    printf("Thread Id: %d. Global value after updated by Thread2Func: %d\n",
          myNum, g_Val);

    g_Val += 1;
    pthread_mutex_unlock(&g_Mutex);
  }

  return NULL;
}

// Thread 2 Callback Function
void *Thread2Func(void *pArg) {
  int *p = (int *)pArg;
  int myNum = *p; // myNum = 1

  // sleep(0.1); // 100ms sleep

  pthread_mutex_lock(&g_Mutex);
  g_Val += 2;
  printf("Thread Id: %d. Global value increased by 2!\n", myNum);
  pthread_mutex_unlock(&g_Mutex);
  pthread_cond_signal(&g_Cond);

  // Workaround if Thread 1 Callback function is delayed
  pthread_mutex_lock(&g_Mutex);
  while (g_Val < 3) {
  pthread_mutex_unlock(&g_Mutex);
  pthread_cond_signal(&g_Cond);
  sleep(1);
  pthread_mutex_lock(&g_Mutex);
  }
  pthread_mutex_unlock(&g_Mutex);

  return NULL;
}

// Main program
int main() {
  pthread_t hThread[NUM_THREADS]; // Stores the POSIX thread IDs
  int threadNum[NUM_THREADS];     // Pass a unique thread ID
  int i = 0;

  // Initialize the mutex & condition variable
  pthread_mutex_init(&g_Mutex, NULL);
  pthread_cond_init(&g_Cond, NULL);

  // Create both threads
  threadNum[0] = 0;
  pthread_create(&hThread[0], NULL, Thread1Func, &threadNum[0]);

  threadNum[1] = 1;
  pthread_create(&hThread[1], NULL, Thread2Func, &threadNum[1]);

  // Wait for all threads to finish
  for (i = 0; i < NUM_THREADS; i++) {
    pthread_join(hThread[i], NULL);
  }
  printf("Global Value: %d\n", g_Val);

  // Clean up
  pthread_cond_destroy(&g_Cond);
  pthread_mutex_destroy(&g_Mutex);
  return 0;
}
