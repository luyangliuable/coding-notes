// Code listing implementing the aforementioned description
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

#define NUM_ROBOT_THREADS 2
pthread_mutex_t g_CRSignal;
int g_SignalVal = -1;

pthread_cond_t g_CMEvt;
pthread_mutex_t g_CMMutex;

int g_RobotOnOffArr[NUM_ROBOT_THREADS];

pthread_cond_t g_RobotEvtArr[NUM_ROBOT_THREADS];
pthread_mutex_t g_RobotMutexArr[NUM_ROBOT_THREADS];

void *ControlModuleFunc(void *pArg) {
  int tRes_0, tRes_1;
  while (1) {

    pthread_mutex_lock(&g_CMMutex);
    pthread_cond_wait(&g_CMEvt, &g_CMMutex);
    /* sleep(3); */

    switch (g_SignalVal) {
    case -1: {
      tRes_0 = -1;
      tRes_1 = -1;
      break;
    }
    case 0: {
      tRes_0 = 0;
      tRes_1 = 0;
      break;
    }
    case 1: {
      tRes_0 = 1;
      tRes_1 = 0;
      break;
    }
    case 2: {
      tRes_0 = 0;
      tRes_1 = 1;
      break;
    }
    case 3: {
      tRes_0 = 1;
      tRes_1 = 1;
      break;
    }
    default: {
      break;
    }
    }
    pthread_mutex_lock(&g_RobotMutexArr[0]);
    g_RobotOnOffArr[0] = tRes_0;
    pthread_mutex_unlock(&g_RobotMutexArr[0]);
    pthread_cond_signal(&g_RobotEvtArr[0]);

    pthread_mutex_lock(&g_RobotMutexArr[1]);
    g_RobotOnOffArr[1] = tRes_1;
    pthread_mutex_unlock(&g_RobotMutexArr[1]);
    pthread_cond_signal(&g_RobotEvtArr[1]);

    if (g_SignalVal == -1) {
      /* pthread_mutex_unlock(&g_CMMutex); */
      break;
    }
    g_SignalVal = -2;
    pthread_mutex_unlock(&g_CMMutex);
  }
  return 0;
}

void *RobotFunc(void *pArg) {
  int *pThreadData = (int *)pArg;
  int threadID = *pThreadData;

  while (1) {

    pthread_mutex_lock(&g_RobotMutexArr[threadID]);
    pthread_cond_wait(&g_RobotEvtArr[threadID], &g_RobotMutexArr[threadID]);

    if (g_RobotOnOffArr[threadID] == 0) {
      printf("Robot :%d OFF\n", threadID);
    } else if (g_RobotOnOffArr[threadID] == 1) {
      printf("Robot :%d ON\n", threadID);
    } else if (g_RobotOnOffArr[threadID] == -1) {
      pthread_mutex_unlock(&g_RobotMutexArr[threadID]);
      break;
    }
    pthread_mutex_unlock(&g_RobotMutexArr[threadID]);
  }
  return 0;
}

int main() {
  pthread_t hCMThread;
  pthread_t hRobotThreads[NUM_ROBOT_THREADS];
  int RobotThreadIDs[NUM_ROBOT_THREADS];

  pthread_mutex_init(&g_CMMutex, NULL);
  pthread_cond_init(&g_CMEvt, NULL);
  pthread_create(&hCMThread, NULL, ControlModuleFunc, NULL);

  for (int i = 0; i < NUM_ROBOT_THREADS; i++) {

    pthread_mutex_init(&g_RobotMutexArr[i], NULL);
    pthread_cond_init(&g_RobotEvtArr[i], NULL);

    RobotThreadIDs[i] = i;
    pthread_create(&hRobotThreads[i], NULL, RobotFunc, &RobotThreadIDs[i]);
  }

  puts("\tMenu");
  puts("\t[0] Turn OFF both Robots");
  puts("\t[1] Turn ON Robot 0 only");
  puts("\t[2] Turn ON Robot 1 only");
  puts("\t[3] Turn ON both Robots");
  puts("\t[-1] Exit");

  int choice = 0;
  while (choice != -1) {
    printf("Choice>> ");
    scanf("%d", &choice);

    switch (choice) {
    case -1: {
      // Part (c)(iii) – To be completed.
      printf("Locking cmmutex for updating choice");
      pthread_mutex_lock(&g_CMMutex);
      g_SignalVal = choice;
      pthread_mutex_unlock(&g_CMMutex);
      pthread_cond_signal(&g_CMEvt);

      for (int i = 0; i < NUM_ROBOT_THREADS; i++) {
        pthread_join(hRobotThreads[i], NULL);
      }
      pthread_join(hCMThread, NULL);
      printf("Program terminated\n");
      break;
    }
    case 0:
    case 1:
    case 2:
    case 3: {
      // Part (c) (iv) – To be completed.
      pthread_mutex_lock(&g_CMMutex);
      g_SignalVal = choice;
      pthread_mutex_unlock(&g_CMMutex);
      pthread_cond_signal(&g_CMEvt);
      break;
    }
    default: {
      break;
    }
    }
  }
  return 0;
}
