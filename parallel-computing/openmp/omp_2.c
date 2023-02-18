#include<stdio.h>
#include <omp.h>

int main( int ac, char **av){

	int num;
	#pragma omp parallel
	{
		int tid = omp_get_thread_num();
		int num_threads = omp_get_num_threads();
		int i, res;
		if(tid == 0){
			printf("Enter a number: ");
			scanf("%d", &num);
		}

		#pragma omp barrier
		//printf( "Thread number %d out of %d. Read Number: %d\n", tid, num_threads, num);

		/*
		int epp = num / num_threads;
		int eppr = num % num_threads;
		int sp = tid * epp;
		int ep = sp + epp;
		if(tid == num_threads - 1){
			ep += eppr;
		}
		*/
		#pragma omp for
		for(i = 0; i < num; i++){
			res = (i * i) + 1;
			printf("Thread No.: %d. Res: %d\n", tid, res);
		}

	}

	return 0;

}
