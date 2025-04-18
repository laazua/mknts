package main

import "fmt"

type LinkNode struct {
	Data     int
	NextNode *LinkNode
}

func main() {
	// 新节点
	node_1 := new(LinkNode)
	node_1.Data = 100

	node_2 := new(LinkNode)
	node_2.Data = 200
	node_1.NextNode = node_2

	node_3 := new(LinkNode)
	node_3.Data = 300
	node_2.NextNode = node_3

	now_node := node_1

	for {
		if now_node != nil {
			fmt.Println(now_node.Data)
			now_node = now_node.NextNode
			continue
		}
		break
	}
}
