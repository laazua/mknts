package main


import(
	"fmt"
	"log"
	"syscall"
)

func main() {
	endless.DefaultReadTimeOut = 600
	endless.DefaultWritTimeOut = 600
	endless.DefaultMaxHeaderBytes = 1 << 20
	endPoint := fmt.Sprintf(":%d", 9999)

	var r  *gin.Engine = SetRouter()

	server := endless.NewServer(endPoint, r)
	server.BeforeBegin = func(add string) {
		log.Printf(":Actual pid is %d", syscall.Getegid())
	}

	err := server.ListenAndServer()
	if err != nil {
		log.Printf("Server err: %v", err)
	}
}

func SetRouter() *gin.Engine{
	r := gin.Default()

	return r
}
