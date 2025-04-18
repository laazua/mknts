#include <omp.h>
#include <iostream>

void computeTaskA() {
    for (int i=0;i<5;i++) {
        std::cout << "task a is processing"
	    << i << " by thread "
	    << omp_get_thread_num()
	    << std::endl; 
    }
}

void computeTaskB() {
    for (int i=0;i<5;i++) {
        std::cout << "task b is processing"
            << i << " by thread "
            << omp_get_thread_num()
            << std::endl;
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
	    std::cout << "all tasks completed" << std::endl;
	}
    }
    return 0;
}

// 编译: g++ -fopenmp threads.cc -o thread
