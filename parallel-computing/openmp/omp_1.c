#include<stdio.h>
#include <omp.h>



int main( int ac, char **av){

	int num;
	#pragma omp parallel
	{
		int tid = omp_get_thread_num();
		int num_threads = omp_get_num_threads();

		if(tid == 0){
			printf("Enter a number: ");
			scanf("%d", &num);
		}

		#pragma omp barrier

		printf( "Thread number %d out of %d. Read Number: %d\n", tid, num_threads, num);
	}

	return 0;

}
