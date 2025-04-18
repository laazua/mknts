# -*- coding:utf-8 -*-
"""
堆(heap)是一个树形数据结构,其中字节点与父节点有一种有序关系,二叉堆(binary heap)可以使用一个有组织的列表或数组表示,其中元素N的子元素位于
2*N+1和2*N+2(索引从0开始)。这种布局允许原地重新组织堆,从而不必在增加或删除元素时重新分配大量内存.
最大堆(max-heap)确保父节点大于或等于其两个字节点.最小堆(min-heap)要求父节点小于或等于 其字节点.python的heapq模块实现了一个最小堆
"""


# this data was generated with the random
data = [19, 9, 4, 10, 11]
