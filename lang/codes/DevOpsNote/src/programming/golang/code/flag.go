package code

// import (
// 	"flag"
// 	"fmt"
// 	"os"
// )

// func init() {

// 	fsAdd := flag.NewFlagSet("add", flag.PanicOnError)
// 	fsList := flag.NewFlagSet("list", flag.PanicOnError)
// 	// 为add命令定义参数
// 	addName := fsAdd.String("name", "", "Name of the item")
// 	addPriority := fsAdd.Int("priority", 0, "Priority of the item")

// 	// 检查是否至少有一个子命令
// 	if len(os.Args) < 2 {
// 		fmt.Println("expected 'add' or 'list' subcommands")
// 		os.Exit(1)
// 	}

// 	switch os.Args[1] {
// 	case "add":
// 		fsAdd.Parse(os.Args[2:])
// 		fmt.Println("Adding item...")
// 		fmt.Printf("Name: %s, Priority: %d\n", *addName, *addPriority)
// 	case "list":
// 		fsList.Parse(os.Args[2:])
// 	default:

// 	}

// }
