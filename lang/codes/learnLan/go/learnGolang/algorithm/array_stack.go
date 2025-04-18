package main

import (
	"fmt"
	"sync"
)

type ArrayStack struct {
	array []string   // 底层切片
	size  int        // 栈的元素数量
	lock  sync.Mutex // 为了并发安全使用的锁
}

// 入栈
func (s *ArrayStack) Push(v string) {
	s.lock.Lock()
	defer s.lock.Unlock()

	s.array = append(s.array, v)

	s.size += 1
}

// 出栈
func (s *ArrayStack) Pop() string {
	s.lock.Lock()
	defer s.lock.Unlock()

	if s.size == 0 {
		panic("stack is empty!")
	}

	// 栈顶元素
	v := s.array[s.size-1]

	// 切片收缩, 但可能占用空间越来越大
	//s.array = s.array[0:s.size-1]

	// 创建新的数组,空间占用不会越来越大,但可能移动元素次数过多
	newArray := make([]string, s.size-1, s.size-1)
	for i := 0; i < s.size-1; i++ {
		newArray[i] = s.array[i]
	}
	s.array = newArray

	// 栈中元素数量-1
	s.size -= 1
	return v
}

// 获取栈顶元素
func (s *ArrayStack) Peek() string {
	if s.size == 0 {
		panic("stack is empty!")
	}

	return s.array[s.size-1]
}

// 栈大小
func (s *ArrayStack) Size() int {
	return s.size
}

// 栈是否为空
func (s *ArrayStack) IsEmpty() bool {
	return s.size == 0
}

func main() {
	arrayStack := new(ArrayStack)
	arrayStack.Push("aaa")
	arrayStack.Push("bbb")
	arrayStack.Push("ccc")

	fmt.Println("size: ", arrayStack.Size())
	fmt.Println("pop: ", arrayStack.Pop())
	fmt.Println("size: ", arrayStack.Size())
}
