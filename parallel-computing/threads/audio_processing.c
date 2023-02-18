// Starter code:
#include <memory.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
/*****************************************************************************/
/*       Changed short to int because not large enough to contain mix         */
/*****************************************************************************/

// Data
#define SAMPLE_COUNT 10000
#define NUM_THREADS 3

int *pAudioBufferOne = NULL;
int *pAudioBufferTwo = NULL;
int *pAudioBufferThree = NULL;

int *pMixBuffer = NULL;

pthread_mutex_t g_Mutex;
int g_MixBufferSum = 0;

void *MixBufferFunc(void *);
int generate_rand(int lo, int hi, unsigned int *seed);

pthread_mutex_t mutex[3];
pthread_mutex_t mix_mutex;

int main() {
  /* unsigned int seed = time(NULL); */
  /* printf("%i.\n", rand_num); */
  /* MixBufferFunc(NULL); */
  for (int i = 0; i < 3; i++)
    pthread_mutex_init(&mutex[i], NULL);

  pthread_mutex_init(&mix_mutex, NULL);

  pthread_t id[3];
  int which_audio;
  // audio 0 means 1, 1 means 2, 2 means 3.
  for (int i = 0; i < 3; i++) {
    which_audio = i;
    /* sleep(1); */
    pthread_create(&id[i], NULL, MixBufferFunc, (void *)&which_audio);
  }

  int *buffers[3] = {pAudioBufferOne, pAudioBufferTwo, pAudioBufferThree};
  int total = 0;

  for (int i = 0; i < 3; i++) {
    pthread_join(id[i], NULL);
    total += *buffers[i];
  }
    pthread_mutex_lock(&mix_mutex);
    g_MixBufferSum = total;
    pthread_mutex_unlock(&mix_mutex);

  return 0;
}

void *MixBufferFunc(void *pArg) {
  int *buffers[3] = {pAudioBufferOne, pAudioBufferTwo, pAudioBufferThree};
  int *which_audio = (int *)pArg;
  int audioOne[SAMPLE_COUNT];
  int audioTwo[SAMPLE_COUNT];
  int audioThree[SAMPLE_COUNT];
  int buffer[SAMPLE_COUNT];
  unsigned int seed;
  int internalBuffer[SAMPLE_COUNT];
  int *internalBufferSum = malloc(sizeof(int)*1);
  *internalBuffer = 0;

  for (int i = 0; i < SAMPLE_COUNT; i++) {
    seed = time(NULL) + i;
    audioOne[i] = generate_rand(0, 10, &seed);
  }

  for (int i = 0; i < SAMPLE_COUNT; i++) {
    seed = time(NULL) + i;
    audioTwo[i] = generate_rand(0, 10, &seed);
  }

  for (int i = 0; i < SAMPLE_COUNT; i++) {
    seed = time(NULL) + i;
    audioThree[i] = generate_rand(0, 10, &seed);
  }

  for (int i = 0; i < SAMPLE_COUNT; i++) {
    internalBuffer[i] = audioOne[i] + audioTwo[i] + audioThree[i];
  }

  for (int i = 0; i < SAMPLE_COUNT; i++) {
    *internalBufferSum += internalBuffer[i];
  }

  pthread_mutex_lock(&mutex[*which_audio]);
  buffers[*which_audio] = internalBufferSum;
  pthread_mutex_unlock(&mutex[*which_audio]);

  printf("Sum of audio %i: %i.\n", *which_audio, *buffers[*which_audio]);

  return 0;
}

int generate_rand(int lo, int hi, unsigned int *seed) {

  int num = (rand_r(seed) % (lo - hi + 1)) + lo;

  return num;
}
