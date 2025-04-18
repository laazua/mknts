#!/usr/bin/env python3
#coding:utf-8

# 插入排序,对于少量元素排序,此排序比较高效.

class Solution:
    """
    将一个待排序的数组从中一次取出元素插入一个新的数组,插入过程中比较排序
    """

    def insert_sort(self,array:list) -> list:
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key

        return array


if __name__ == '__main__':
    l = [1,3,2,4]
    ob = Solution()
    n = ob.insert_sort(l)
    print(n)