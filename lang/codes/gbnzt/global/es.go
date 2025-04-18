package global

import (
	"log"
	"time"

	"github.com/olivere/elastic/v7"
)

var (
	EsClient *elastic.Client
)

// 初始化es连接
func init() {
	num := 0
	for {
		esClient, err := elastic.NewClient(
			elastic.SetSniff(false),
			elastic.SetURL(AppCon.GetString("es.url")),
			elastic.SetBasicAuth(AppCon.GetString("es.user"), AppCon.GetString("es.pass")),
			elastic.SetGzip(true),
			elastic.SetHealthcheckInterval(10*time.Second),
		)
		if err != nil {
			log.Println(err)
			log.Println("ES客户端创建失败!")
			num += 1
			if num > 3 {
				panic("ES连接失败, 请检查用户密码是否正确!")
			}
			time.Sleep(3 * time.Second)

		} else {
			// esv, _ := EsClient.ElasticsearchVersion(AppCon.GetString("es.url"))
			// log.Println("ES客户端连接成功, 版本: ", esv)
			EsClient = esClient
			break
		}
	}
}
