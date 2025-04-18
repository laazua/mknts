#include <omp.h>
#include <stdio.h>

void computeTaskA() {
    for (int i=0;i<5;i++) {
        printf("task a is processing by thread %d\n", omp_get_thread_num());
    }
}

void computeTaskB() {
    for (int i=0;i<5;i++) {
        printf("task b is processing by thread %d\n", omp_get_thread_num());
    }
}

int main()
{
#pragma omp parallel
    {
#pragma omp sigle
	{
#pragma omp task
	    {
	        computeTaskA();
	    }
#pragma omp task
	    {
	        computeTaskB();
	    }
#pragma omp taskwait
	    printf("all tasks completed\n");
	}
    }
    return 0;
}

// 编译: g++ -fopenmp threads.cc -o thread
