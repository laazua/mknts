package main

import "fmt"

type Ring struct {
	next, prev *Ring
	Data       interface{}
}

// 初始化一个空的循环链表
func (r *Ring) init() *Ring {
	r.next = r
	r.next.prev = r
	return r
}

func main() {
	//r := new(Ring)
	//r.init()

	linkNewTest()
}

// 创建N个节点的循环链表
func New(n int) *Ring {
	if n <= 0 {
		return nil
	}
	r := new(Ring)
	p := r
	for i := 1; i < n; i++ {
		p.next = &Ring{prev: p}
		p = p.next
	}
	p.next = r
	r.prev = p
	return r
}

// 获取下一个节点
func (r *Ring) Next() *Ring {
	if r.next == nil {
		return r.init()
	}
	return r.next
}

// 获取上一个节点
func (r *Ring) Prev() *Ring {
	if r.next == nil {
		return r.init()
	}
	return r.prev
}

// 获取第n个节点
func (r *Ring) Move(n int) *Ring {
	if r.next == nil {
		return r.init()
	}
	switch {
	case n < 0:
		for ; n < 0; n++ {
			r = r.prev
		}
	case n > 0:
		for ; n > 0; n-- {
			r = r.next
		}
	}
	return r
}

// 往节点A，链接一个节点，并且返回之前节点A的后驱节点
func (r *Ring) Link(s *Ring) *Ring {
	n := r.Next()
	if s != nil {
		p := s.Prev()
		r.next = s
		s.prev = r
		n.prev = p
		p.next = n
	}
	return n
}

// 删除节点后面的 n 个节点
func (r *Ring) Unlink(n int) *Ring {
	if n < 0 {
		return nil
	}
	return r.Link(r.Move(n + 1))
}

// 查看循环链表长度
func (r *Ring) Len() int {
	n := 0
	if r != nil {
		n = 1
		for p := r.Next(); p != r; p = p.next {
			n++
		}
	}
	return n
}

func linkNewTest() {
	//第一个节点
	r := &Ring{Data: -1}

	//链接5个新节点
	r.Link(&Ring{Data: 1})
	r.Link(&Ring{Data: 2})
	r.Link(&Ring{Data: 3})
	r.Link(&Ring{Data: 4})

	node := r
	for {
		fmt.Println(node.Data)
		node = node.Next()
		if node == r {
			return
		}
	}
}
