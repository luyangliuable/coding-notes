//---------------------------------------------------------------------------------------------------------------------
// PThreadBasic.c
//
//---------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
#include <pthread.h>
#define NUM_THREADS 4


void* ProcessFunc(void *pArg) // Common function prototype
{
	int* p = (int*)pArg;
	int myNum = *p; // Dereferences the pointer
	printf( "Thread number %d\n", myNum);

	return 0;
}

int main()
{
	pthread_t tid[NUM_THREADS];
	int threadNum[NUM_THREADS];
	int i = 0;

	printf( "Main process starts\n");


    // Fork
	for (i = 0; i < NUM_THREADS; i++)
	{
	    threadNum[i] = i;
		pthread_create(&tid[i], 0, ProcessFunc, &threadNum[i]); // &i
	}

	// Join
	for(i = 0; i < NUM_THREADS; i++)
	{
	    pthread_join(tid[i], NULL);
	}
	// All threads have safely been safely terminated


	printf( "Main process ends\n");
	return 0;
}
