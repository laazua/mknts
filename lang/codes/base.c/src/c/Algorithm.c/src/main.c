#include <stdio.h>
#include "sort.h"

int main()
{
    int nums[] = {83, 2, 45, 78, 24};
    int* result = bubble(nums, 5);
    for(int i=0; i<5; i++) {
        printf("%d ", result[i]);
    }
    printf("\n");

    return 0;
}
