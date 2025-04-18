package main

import (
	"fmt"
	"sync"
)

type ArrayQueue struct {
	array []interface{} // 底层切片
	size  int           // 队列的元素数量
	lock  sync.Mutex    // 为了并发安全使用
}

// 入队
func (q *ArrayQueue) Add(data interface{}) {
	q.lock.Lock()
	defer q.lock.Unlock()

	// 放入切片中,后进的元素放在切片最后面
	q.array = append(q.array, data)

	// 队列中元素数量加 1
	q.size += 1
}

// 出队
func (q *ArrayQueue) Remove() interface{} {
	q.lock.Lock()
	defer q.lock.Unlock()

	// 队列中的元素已空
	if q.size == 0 {
		panic("queue is empty!")
	}

	// 队列最前面元素
	data := q.array[0]

	/* 直接原位移动,但缩容后继的空间不会被释放
	for i := 1; i < q.size; i ++ {
		// 从第一位开始进行数据移动
		q.array[i-1] = q.array[i]
	}
	// 原数组缩容
	q.array = q.array[0:q.size-1]
	*/

	// 创建新的数组,移动次数过多
	newArray := make([]interface{}, q.size-1, q.size-1)
	for i := 1; i < q.size; i++ {
		// 从老数组的第一位开始进行数据移动
		newArray[i-1] = q.array[i]
	}
	q.array = newArray

	// 队列中元素数量减 1
	q.size -= 1
	return data
}

// 队列大小
func (q *ArrayQueue) Size() int {
	return q.size
}

// 队列是否为空
func (q *ArrayQueue) IsEmpty() bool {
	return q.size == 0
}

func main() {
	arrayQueue := new(ArrayQueue)
	arrayQueue.Add(1)
	arrayQueue.Add(2)
	arrayQueue.Add(3)
	fmt.Println("size: ", arrayQueue.Size())
	fmt.Println("remove: ", arrayQueue.Remove())
	fmt.Println("size: ", arrayQueue.Size())
}
