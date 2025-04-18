# -*- coding: utf-8 -*-

"""
list使用
for k, v in enumerate(d):
        print(k, v)

for i, j in zip(list1, list2):
    print(i, j)
"""

def test_list(mlist: list) -> None:
    """
    测试list相关的方法
    """
    # 在列表末尾追加元素
    for i in range(5):
        mlist.append(i)   # <==> mlist[len(mlist):] = i

    l = ['a', 'b', 'c']
    # 在列表末尾追加一个可迭代的对象
    mlist.extend(l)
    print(mlist)          # <==> mlist[len(mlist):] = l

    # 在列表指定位置插入一个元素(在索引0处插入‘哈哈’)
    mlist.insert(0, "哈哈")
    print(mlist)

    # 删除列表中指定位置的元素并返回它(不指定索引,则删除最后一个元素)
    mlist.pop(2)
    print(mlist)

    # 移除列表中的第一个元素为x，没有该元素则跑出异常ValueError(若x = "哈哈")
    mlist.remove("哈哈")
    print(mlist)

    # 删除列表中所有元素
    mlist.clear()       # <==> del mlist[:]

    # 返回列表中指定索引区间的某个元素,如果没有该元素则跑出ValueError异常(list.index(x, [start[, end]]))
    mlist.index(3)

    # 返回x元素在列表中出现的次数
    mlist.count(1)

    # 对列表中的元素进行排序(list.sort(key=None, reverse=False))
    mlist.sort()

    # 反转列表中的元素
    mlist.reverse()

    # 返回列表的一个浅拷贝(注意区分浅拷贝和深度拷贝)
    mlist.copy()        # <==> a[:]



def test_list_stack() -> None:
    """
    列表作为栈使用(后进先出)
    """
    stack = [1, 2, 3, 4,]
    
    for item in range(5, 10):
        stack.append(item)

    for item in range(5):
        stack.pop()

    print(stack)


from collections import deque
def test_list_deque() -> None:
    """
    列表作为队列使用(先进先出)
    """
    queue = deque(['a', 'b', 'c', 'd'])

    # 操作queue右边(入队)
    queue.append("e")

    # 操作queue左边(出队)
    queue.popleft()

    print(queue)


def test_list_derive() -> None:
    """
    测试列表推导式
    """
    l = [1, 2, 3, 4, 5]
    l1 = [x ** 2 for x in l]

    l2 = [(x, y) for x in l for y in l1 if x != y]



if __name__ == "__main__":
    l = []
    test_list(l)