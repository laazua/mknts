#!/usr/bin/env python3
#coding: utf-8

class Solution:
    """
    求给定一个整数数组nums和一个target值,找出数组中两个数和为target的两个整数,并返回它们的下标.
    """

    def find_target(self, array: list, target: int) -> list:
        result = []

        for k, v in enumerate(array):
            for element in array[1:]:
                print(v, element)
                if v + element == target:

                    return k, array.index(element)

        #return result


if __name__ == '__main__':
    array = [2,5,7,3,23,5,4]
    target = 7
    ob = Solution()
    rees = ob.find_target(array, target)
    print(rees)