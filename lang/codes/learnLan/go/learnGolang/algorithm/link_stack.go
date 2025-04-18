package main

import (
	"fmt"
	"sync"
)

type LinkStack struct {
	root *LinkNode  // 链表起点
	size int        // 栈的元素数量
	lock sync.Mutex // 为了并发安全使用的锁
}

type LinkNode struct {
	Next *LinkNode
	Data string
}

// 入栈
func (s *LinkStack) Push(data string) {
	s.lock.Lock()
	defer s.lock.Unlock()

	// 如果栈顶为空,那么增加节点
	if s.root == nil {
		s.root = new(LinkNode)
		s.root.Data = data
	} else {
		// 否则新元素插入链表头部
		// 原来的链表
		preNode := s.root

		// 新节点
		newNode := new(LinkNode)
		newNode.Data = data

		// 原来的链表接到新元素后面
		newNode.Next = preNode

		// 将新节点放在头部
		s.root = newNode
	}

	// 栈中元素数量加 1
	s.size += 1
}

// 出栈
func (s *LinkStack) Pop() string {
	s.lock.Lock()
	defer s.lock.Unlock()

	// 栈中元素已空
	if s.size == 0 {
		panic("stack is empty!")
	}

	// 顶部元素出栈
	topNode := s.root
	data := topNode.Data

	// 将顶部元素的后继链接链上
	s.root = topNode.Next

	// 栈中元素减 1
	s.size -= 1
	return data
}

// 获取栈顶元素
func (s *LinkStack) Peek() string {
	// 栈中元素已为空
	if s.size == 0 {
		panic("stack is empty!")
	}

	return s.root.Data
}

// 栈大小
func (s *LinkStack) Size() int {
	return s.size
}

// 栈是否为空
func (s *LinkStack) IsEmpty() bool {
	return s.size == 0
}

func main() {
	linkStack := new(LinkStack)
	linkStack.Push("AAA")
	linkStack.Push("BBB")
	linkStack.Push("CCC")
	fmt.Println("size: ", linkStack.Size())
	fmt.Println("pop: ", linkStack.Pop())
	fmt.Println("size: ", linkStack.Size())
}
