#!/usr/bin/env python3
# -*- coding: uftf-8 -*-

class Slution:
    def binary_search(self, array, target):
        if not array:
            return -1

        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if array[mid] == target:
                start = mid
            elif array[mid] < target:
                start = mid
            else:
                end =  mid

        if array[start] == target:
            return start
        if array[end] ==  target:
            return end

        return -1