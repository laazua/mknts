#include <stdio.h>
#include "sort.h"

int* bubble(int* nums, int len)
{
    int tmp;
    for(int i=0; i<len; i++) {
        for(int j=0; j<len-i-1; j++) {
            if(nums[i] > nums[j]) {
               tmp = nums[j];
               nums[j] = nums[j+1];
               nums[j+1] = tmp;
            }
        }
    }

    return nums;
}
