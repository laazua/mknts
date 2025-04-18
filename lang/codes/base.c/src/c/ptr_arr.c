//
// 指针与数组
//
#include <stdio.h>
#include <stdlib.h>

void ptr_max_arr();
void dynamic_arry(int size);

int main()
{
    int arr[5] = {2, 3, 4};

    // 注意区分与下面dynamic_arr动态数组的大小
    printf("原生数组大小: %ld\n", sizeof(arr));

    printf("%d  %d\n", arr[1], arr[3]);

    printf("%p\n", arr);

    int *ptr = arr;
    printf("%d  %d\n", *(ptr+1), *(ptr+3));

    printf("%p\n", ptr);

    dynamic_arry(6);

    ptr_max_arr();

    return 0;
}

// 指针与多维数组
void ptr_max_arr()
{
    int arr[3][5] = {
        {12, 32, 45},
	{33, 90, 45, 57, 98},
	{24, 27, 87, 67, 64}
    };

    // 指向一维数组的指针
    int (*ptr)[5] = arr;

    for (int i=0; i<3; i++) {
        for (int j=0; j<5; j++) {
	    printf("arr[%d][%d]: %d\n", i, j, arr[i][j]);
	    printf("ptr->arr[%d][%d]: %d\n", i, j, *(*(ptr + i)+j));
	}
    }
}

// 动态数组
void dynamic_arry(int size)
{
    int *dynamic_arr = (int *)malloc(size * sizeof(int));

    if (dynamic_arr == NULL) {
        printf("malloc memory failure!");
	return;
    }

    for (int i=0; i<size; i++) {
        dynamic_arr[i] = i*i;
    }

    printf("动态数组大小: %ld\n", sizeof(dynamic_arr));

    for (int i=0; i<size; i++) {
        printf("%d\n", dynamic_arr[i]);
	printf("动态数组元素%d大小: %ld\n", i, sizeof(dynamic_arr[i]));
    }

    free(dynamic_arr);
}

/////// 输出结果 //////
// 原生数组大小: 20
// 3  0
// 0x7fffa60cd1d0
// 3  0
// 0x7fffa60cd1d0
// 动态数组大小: 8
// 0
// 动态数组元素0大小: 4
// 1
// 动态数组元素1大小: 4
// 4
// 动态数组元素2大小: 4
// 9
// 动态数组元素3大小: 4
// 16
// 动态数组元素4大小: 4
// 25
// 动态数组元素5大小: 4
