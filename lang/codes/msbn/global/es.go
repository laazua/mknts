package global

import (
	"log"
	"time"

	"github.com/olivere/elastic/v7"
)

var (
	EsClient *elastic.Client
	err      error
)

// 初始化es连接
func init() {
	EsClient, err = elastic.NewClient(
		elastic.SetSniff(false),
		elastic.SetURL(AppCon.GetString("es.url")),
		// elastic.SetBasicAuth(AppCon.GetString("es.user"), AppCon.GetString("es.pass")),
		elastic.SetGzip(true),
		elastic.SetHealthcheckInterval(10*time.Second),
	)
	if err != nil {
		log.Println(err)
		panic("ES客户端创建失败!")
	}
	log.Println("ES客户端连接成功!")
	esv, _ := EsClient.ElasticsearchVersion(AppCon.GetString("es.url"))
	log.Println("ES版本: ", esv)
}
