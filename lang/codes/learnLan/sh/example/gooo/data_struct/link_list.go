package main

import(
	"fmt"
)

type  LinkNode struct {
	Data 		int64
	NextNode	*LinkNode
}

func main() {
	node1 := new(LinkNode)
	node1.Data = 2

	node2 := new(LinkNode)
	node2.Data = 3
	node1.NextNode = node2

	node3 := new(LinkNode)
	node3.Data = 4
	node2.NextNode = node3

	node3.NextNode = node1

	nowNode := node1

	for {
		if nowNode != nil {
			fmt.Println(nowNode.Data)
			nowNode = nowNode.NextNode
		}
		break
	}
}