# -*- cdding:utf -*-
"""
deque是一种序列容器支持list的一些操作
双端队列或deque支持从任意一端增加和删除元素.常用的两种结构:栈和队列 是双端队列的退化形式,它们的输入输出被限制在某一端.
双端队列是线程安全迭代,可以在不同线程中同时从双端队列两端消费队列里的数据.
"""
import collections


d = collections.deque('abcdefg')
print('Deque: ', d)
print('Length: ', len(d))
print('Left end: ', d[0])
print('Right end: ', d[-1])


d.remove('c')
print('remove(c): ', d)


dq = collections.deque(maxlen=10)
dq.extend('abcdefg')

dq.append('h')
dq.appendleft('1')
dq.pop()
dq.popleft()

# 将队列末尾的两个元素旋转到开头
dq.rotate(2)



# 保留最后N个元素
def search(lines, pattern, history=5):
    previous_lines = collections.deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open('filename') as fd:
        for line, prevlines in search(fd, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)