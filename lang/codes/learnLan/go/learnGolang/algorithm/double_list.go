package main

import (
	"fmt"
	"sync"
)

// 双端列表,双端队列
type DoubleList struct {
	head *ListNode  //指向链表头部
	tail *ListNode  //指向链表尾部
	len  int        //列表长度
	lock sync.Mutex // 为了进行并发安全使用的锁
}

// 列表节点
type ListNode struct {
	pre  *ListNode   // 指向前驱节点
	next *ListNode   // 指向后驱节点
	data interface{} // 存放数据
}

// 获取节数据
func (n *ListNode) GetData() interface{} {
	return n.data
}

// 获取前驱节点
func (n *ListNode) GetPre() *ListNode {
	return n.pre
}

// 获取后驱节点
func (n *ListNode) GetNext() *ListNode {
	return n.next
}

// 是否存在后驱节点
func (n *ListNode) HasNext() bool {
	return n.next != nil
}

// 是否存在前驱节点
func (n *ListNode) HasPre() bool {
	return n.pre != nil
}

// 是否为空节点
func (n *ListNode) IsNil() bool {
	return n == nil
}

// 返回列表长度
func (list *DoubleList) Len() int {
	return list.len
}

// 从头部开始某个位置插入新节点
func (l *DoubleList) AddNodeFromHead(n int, data interface{}) {
	// 加并发锁
	l.lock.Lock()
	defer l.lock.Unlock()

	// 索引超过列表长度,一定找不到,panic
	if n > l.len {
		panic("index out!")
	}

	// 先找出头部
	node := l.head

	//往后遍历拿到第n+1个位置元素
	for i := 1; i <= n; i++ {
		node = node.next
	}

	// 新节点
	newNode := new(ListNode)
	newNode.data = data

	// 如果定位到的节点为空,表示列表为空,将新节点设置为新头部和新尾部
	if node.IsNil() {
		l.head = newNode
		l.tail = newNode
	} else {
		// 定位到的节点,它的前驱
		pre := node.pre

		// 如果定位到的节点前驱为nil,那么定位到的节点为链表头部,需要换头部
		if pre.IsNil() {
			// 将新节点连接在老头部之前
			newNode.next = node
			node.pre = newNode
			// 新节点成为头部
			l.head = newNode
		} else {
			// 将新节点插入到定位到的节点之前
			// 定位到的节点的前驱节点pre现在连接到新节点上
			pre.next = newNode
			newNode.pre = pre

			// 定位到的节点的后驱节点node.next现在连接到新节点上
			node.next.pre = newNode
			newNode.next = node.next
		}
	}

	// 列表长度+1
	l.len += 1
}

// 从尾部开始某个位置后插入新节点
func (l *DoubleList) AddNodeFromTail(n int, data interface{}) {
	l.lock.Lock()
	defer l.lock.Unlock()

	// 索引超过列表长度一定找不到,panic
	if n >= l.len {
		panic("index out!")
	}

	// 先找出尾部
	node := l.tail

	// 往前遍历拿到第N+1个位置的元素
	for i := 1; i <= n; i++ {
		node = node.pre
	}

	// 新节点
	newNode := new(ListNode)
	newNode.data = data

	// 如果定位到的节点为空,表示列表为空,将新节点设置为新头部和新尾部
	if node.IsNil() {
		l.head = newNode
		l.tail = newNode
	} else {
		// 定位到的节点，它的后驱
		next := node.next

		// 如果定位到的节点后驱为nil,那么定位的节点为链表尾部,需要换尾部
		if next.IsNil() {
			// 将新节点链接在老尾部之后
			node.next = newNode
			newNode.pre = node

			// 新节点成为尾部
			l.tail = newNode
		} else {
			// 将新节点插入到定位到的节点之后
			// 新节点链接到定位到的节点之后
			newNode.pre = node
			node.next = newNode

			// 定位到的节点的后驱节点链接在新节点之后
			newNode.next = next
			next.pre = newNode
		}
	}
	// 列表长度加1
	l.len += 1
}

// 从头部开始往后找，获取第N+1个位置的节点，索引从0开始
func (l *DoubleList) IndexFromHead(n int) *ListNode {
	// 索引超过或等于列表长度，一定找不到，返回空指针
	if n >= l.len {
		return nil
	}

	// 获取头部节点
	node := l.head

	//  往后遍历拿到第 N+1 个位置的元素
	for i := 1; i <= n; i++ {
		node = node.next
	}

	return node
}

// 从尾部开始往前找，获取第N+1个位置的节点，索引从0开始。
func (l *DoubleList) IndexFromTail(n int) *ListNode {
	// 索引超过或等于列表长度，一定找不到，返回空指针
	if n >= l.len {
		return nil
	}

	// 获取尾部节点
	node := l.tail

	// 往前遍历拿到第 N+1 个位置的元素
	for i := 1; i <= n; i++ {
		node = node.pre
	}

	return node
}

// 从头部开始往后找，获取第N+1个位置的节点，并移除返回
func (l *DoubleList) PopFromHead(n int) *ListNode {
	// 加并发锁
	l.lock.Lock()
	defer l.lock.Unlock()

	// 索引超过或等于列表长度，一定找不到，返回空指针
	if n >= l.len {
		return nil
	}

	// 获取头部
	node := l.head

	// 往后遍历拿到第 N+1 个位置的元素
	for i := 1; i <= n; i++ {
		node = node.next
	}

	// 移除的节点的前驱和后驱
	pre := node.pre
	next := node.next

	// 如果前驱和后驱都为nil，那么移除的节点为链表唯一节点
	if pre.IsNil() && next.IsNil() {
		l.head = nil
		l.tail = nil
	} else if pre.IsNil() {
		// 表示移除的是头部节点，那么下一个节点成为头节点
		l.head = next
		next.pre = nil
	} else if next.IsNil() {
		// 表示移除的是尾部节点，那么上一个节点成为尾节点
		l.tail = pre
		pre.next = nil
	} else {
		// 移除的是中间节点
		pre.next = next
		next.pre = pre
	}

	// 节点减一
	l.len -= 1
	return node
}

// 从尾部开始往前找，获取第N+1个位置的节点，并移除返回
func (l *DoubleList) PopFromTail(n int) *ListNode {
	// 加并发锁
	l.lock.Lock()
	defer l.lock.Unlock()

	// 索引超过或等于列表长度，一定找不到，返回空指针
	if n >= l.len {
		return nil
	}

	// 获取尾部
	node := l.tail

	// 往前遍历拿到第 N+1 个位置的元素
	for i := 1; i <= n; i++ {
		node = node.pre
	}

	// 移除的节点的前驱和后驱
	pre := node.pre
	next := node.next

	// 如果前驱和后驱都为nil，那么移除的节点为链表唯一节点
	if pre.IsNil() && next.IsNil() {
		l.head = nil
		l.tail = nil
	} else if pre.IsNil() {
		// 表示移除的是头部节点，那么下一个节点成为头节点
		l.head = next
		next.pre = nil
	} else if next.IsNil() {
		// 表示移除的是尾部节点，那么上一个节点成为尾节点
		l.tail = pre
		pre.next = nil
	} else {
		// 移除的是中间节点
		pre.next = next
		next.pre = pre
	}

	// 节点减一
	l.len -= 1
	return node
}

// 返回列表链表头结点
func (list *DoubleList) First() *ListNode {
	return list.head
}

// 返回列表链表尾结点
func (list *DoubleList) Last() *ListNode {
	return list.tail
}

func main() {
	list := new(DoubleList)
	// 在列表头部插入新元素
	list.AddNodeFromHead(0, "aaa")
	list.AddNodeFromHead(0, "bbb")
	list.AddNodeFromHead(0, "ccc")
	// 在列表尾部插入新元素
	list.AddNodeFromTail(0, "AAA")
	list.AddNodeFromHead(0, "BBB")
	list.AddNodeFromTail(0, "CCC")

	// 正常遍历, 比较慢
	for i := 0; i < list.Len(); i++ {
		// 从头部开始索引
		node := list.IndexFromHead(i)

		// 节点为空不可能,因为list.Len()使得索引不会越界
		if !node.IsNil() {
			fmt.Println(node.GetData())
		}
	}

	fmt.Println("=================")

	// 正常遍历,特别快
	// 先取出第一个元素
	first := list.First()
	for !first.IsNil() {
		// 如果非空就一直遍历
		fmt.Println(first.GetData())
		// 接着下一个节点
		first = first.GetNext()
	}

	fmt.Println("=================")

	// 元素一个一个pop出来
	for {
		node := list.PopFromHead(0)
		if node.IsNil() {
			// 没有元素了.直接返回
			break
		}
		fmt.Println(node.GetData())
	}

	fmt.Println("=================")
	fmt.Println("len: ", list.Len())
}
