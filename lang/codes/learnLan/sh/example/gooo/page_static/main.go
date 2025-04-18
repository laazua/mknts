package main

import(
	"fmt"
	"github.com/gin-gonic/gin"
	"html/template"
	"net/http"
	"os"
	"path/filepath"
)

type Product struct {
	Id		int64	`json:"id"`
	Name 	string	`json:"name"`
}

//模拟从数据库查询过来的消息
var allproduct []*Product = []*Product {
	{1, "苹果手机"},
	{2, "苹果电脑"},
	{2, "苹果耳机"},
}

var (
	//生成的html保存目录
	htmlOutPath = "./tem"
	//静态文件模板目录
	templatePath = "./tem"
)

func main() {
	r := gin.Default()
	r.LoadHTMLGlob("tem/*")
	r.GET("/index", func(c *gin.Context) {
		GetGenerateHtml()
		c.HTML(http.StatusOK, "index.html", gin.H{
			"allproduct": allproduct,
		})
	})
	r.GET("/index2", func(c *gin.Context) {
		c.HTML(http.StatusOK, "htmlindex.html", gin.H{})
	})

	r.Run("0.0.0.0:8080")
}

//生成静态文件的方法
func GetGenerateHtml() {
	//获取模板
	contenstTmp, err := template.ParseFiles(filepath.Join(templatePath, "index.html"))
	if err != nil {
		fmt.Println("获取模板文件失败")
	}

	//获取html生成路径
	fileName := filepath.Join(htmlOutPath, "htmlindex.html")

	//生成静态文件
	generateStaticHtml(contenstTmp, fileName, gin.H{"allporduct": allproduct})
}

//生成静态文件
func generateStaticHtml(template *template.Template, fileName string, product map[string]interface{}) {
	//判断静态文件是否存在
	if exist(fileName) {
		err := os.Remove(fileName)
		if err != nil {
			fmt.Println("移除文件失败")
		}
	}

	//生成静态文件
	file, err := os.OpenFile(fileName, os.O_CREATE|os.O_WRONLY, os.ModePerm)
	if err != nil {
		fmt.Println("打开文件失败")
	}
	defer  file.Close()
	template.Execute(file, &product)
}

func exist(fileName string) bool{
	_, err := os.Stat(fileName)
	return  err == nil || os.IsExist(err)
}