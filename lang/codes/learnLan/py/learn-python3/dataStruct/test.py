# -*- coding:utf-8 -*-


def drop_first_last(obj: iter) -> list:
    """
    解压可迭代对象给多个变量
    """
    firs, *middle, last = obj
    return middle


import heapq
def search_element(obj:list) -> list:
    """
    从集合中获取最大或最小的N个元素
    heap.heapify(obj) && heap.heappop(obj): 一次从obj中获取最小的元素
    """
    maxs = heapq.nlargest(3, obj)    #从obj中获取最大的3个元素
    mins = heapq.nsmallest(3, obj)   #从obj中获取最小的3个元素

    print(heapq.heapify(list(obj)))
    print(heapq.heappop(list(obj)))

    return maxs     # 或者返回mins



if __name__ == "__main__":
    l = (1,2,3,4,5,6,7,8,9)
    
    print(drop_first_last(l))

    print(search_element(l))


