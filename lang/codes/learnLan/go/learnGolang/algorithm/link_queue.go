package main

import (
	"fmt"
	"sync"
)

type LinkNode struct {
	Next *LinkNode
	Data interface{}
}

type LinkQueue struct {
	root *LinkNode  // 链表起点
	size int        // 队列元素数量
	lock sync.Mutex // 为了并发安全使用的锁
}

// 入队
func (q *LinkQueue) Add(data interface{}) {
	q.lock.Lock()
	defer q.lock.Unlock()

	// 如果栈顶为空,那么增加节点
	if q.root == nil {
		q.root = new(LinkNode)
		q.root.Data = data
	} else {
		// 否则新元素插入链表的末尾
		newNode := new(LinkNode)
		newNode.Data = data

		// 一直遍历到链表的尾部
		nowNode := q.root
		for newNode.Next != nil {
			newNode = newNode.Next
		}

		// 新节点放在链表尾部
		nowNode.Next = newNode
	}

	// 队列元素+1
	q.size += 1
}

// 出队
func (q *LinkQueue) Remove() interface{} {
	q.lock.Lock()
	defer q.lock.Unlock()

	// 队列元素已空
	if q.size == 0 {
		panic("queue is empty!")
	}

	//顶部元素出队
	topNode := q.root
	data := topNode.Data

	//将顶部元素后的后继连接上
	q.root = topNode.Next

	// 队列元素数量-1
	q.size -= 1

	return data
}

// 队列大小
func (q *LinkQueue) Size() int {
	return q.size
}

// 队列是否为空
func (q *LinkQueue) IsEmpty() bool {
	return q.size == 0
}

func main() {
	linkQueue := new(LinkQueue)
	linkQueue.Add("a")
	linkQueue.Add(1)
	linkQueue.Add("b")
	linkQueue.Add(2)
	linkQueue.Add("c")
	linkQueue.Add(3)

	fmt.Println("size: ", linkQueue.Size())
	fmt.Println("remove:", linkQueue.Remove())
	fmt.Println("size: ", linkQueue.Size())
	fmt.Println("remove: ", linkQueue.Remove())
	fmt.Println("size: ", linkQueue.Size())
}
