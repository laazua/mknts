#include <stdio.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) 
{
    for(int i=0;i<numsSize;i++){
        int an = target - nums[i];
        for(int j=0;j<numsSize;j++){
            if (nums[j] == an){
                returnSize[0] = j;
                returnSize[1] = i;
            }
        }
    }
    return returnSize;
}

int main()
{
    int nums[] = {3, 2, 4};
    int numsSize = 3;
    int target = 6;
    int returnSize;
    int *ret = twoSum(nums, numsSize, target, &returnSize);
    printf("%d  %d\n", ret[0], ret[1]);

    return 0;
}
