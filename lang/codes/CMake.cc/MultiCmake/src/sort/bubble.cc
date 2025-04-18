#include <iostream>
#include "bubble.h"

using namespace std;

Bubble::Bubble(int len, int[] numbers)
{
    this->len = len;
    this->numners = numbers;
}

void Bubble::sort(void)
{
    int i, j, temp;
        for (i = 0; i < this->len - 1; i++)
            for (j = 0; j < this->len - 1 - i; j++)
                if (arr[j] > arr[j + 1]) {
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
    for (i = 0; i < this->len; i++)
        cout << this->numbers[i] << endl;
}
