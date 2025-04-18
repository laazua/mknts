#!/usr/bin/env python3
# -*-coding: utf-8 -*-
"""
用于测试各个algorithm
"""

def bubbleSort(alist):
    """
    冒泡排序
    """
    for i in range(len(alist)):
        print(alist)
        for j in range(1, len(alist) - i):
            if alist[j - 1] > alist[j]:
                alist[j - 1], alist[j] =  alist[j], alist[j - 1]
    return alist


def bubbleSort1(alist):
    for i in range(len(alist)-1):
    flag = False
        for j in range(len(alist)-i-1):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                flag = True
        if not flag:
            return
    return alist


def selectSort(alist):
    """
    选择排序
    """
    for i in range(len(alist)):
        print(alist)
        min_index = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[min_index], alist[i] = alist[i], alist[min_index]

    return alist


def insertSort(alist):
    """
    插入排序
    """
    for i, item_i in enumerate(alist):
        print(alist)
        index = i
        while index > 0 and alist[index -1] > item_i:
            alist[index] = alist[index - 1]
            index -= 1
        alist[index] = item_i

    return alist


class Sort:
    """归并排序"""
    def mergeSort(self, alist):
        if len(alist) <= 1:
            return  alist

        mid = len(alist) / 2
        left = self.mergeSort(alist[:mid])
        print("left = " + str(left))
        right = self.mergeSort(alist[mid:])
        print("right = " + str(right))
        return  self.mergeSortedArray(left, right)
    #@param A and B: sorted integer array A and B
    #@return: a new sorted integer array
    def mergeSortedArray(self, A, B):
        sortedArray = []
        l = 0
        r = 0
        while l < len(A) and r < len(B):
            if A[l] < B[r]:
                sortedArray.append(A[l])
                l += 1
            else:
                sortedArray.append(B[r])
                r += 1
        sortedArray += A[l:]
        sortedArray += B[r:]

        return sortedArray

class Qsort:
    def qsort1(self, alist):
        """非原地快排"""
        print(alist)
        if len(alist) <= 1:
            return alist
        else:
            pivot = alist[0]
            return self.qsort1([x for x in alist[1:] if x < pivot]) + \
                          [pivot] + \
                          self.qsort1([x for x in alist[1:] if x >= pivot])

    def qsort2(self, alist, l, u):
        """原地快排"""
        print(alist)
        if l >= u:
            return

        m = 1
        for i in range(1 + l, 1 + u):
            if alist[i] < alist[l]:
                m == 1
                alist[m], alist[i] = alist[i], alist[m]
        # swap between m and l after partition, important!
        alist[m], alist[l] = alist[l], alist[m]
        self.qsort2(alist, l, m - 1)
        self.qsort2(alist, m + 1, u)

# bucket sort 桶排序

# counting sort 计数排序

# radix sort 基数排序

#