package utils

// import (
// 	"bnzt/global"
// 	"context"
// 	"strconv"
// 	"strings"

// 	"github.com/olivere/elastic/v7"
// )

// // EsApi
// type EsApi interface {
// 	GetRechargeRank(stime, etime, zone string, size, num int) interface{}
// }

// func NewEsApi() EsApi {
// 	return &es{}
// }

// type es struct {
// }

// // 充值排行查询
// func (e *es) GetRechargeRank(stime, etime, zone string, size, num int) interface{} {
// 	// 组合查询条件
// 	b := elastic.NewBoolQuery().Must(
// 		elastic.NewMatchQuery("role_zone_id", zone))
// 	b.Filter(elastic.NewRangeQuery("@timestamp").Gte(formatTime(stime)).
// 		Lte(formatTime(etime)),
// 		elastic.NewExistsQuery("vmall_real_money"))
// 	// 查询并获取结果
// 	res, err := global.EsClient.Search().Index("gamelog-*").Query(b).
// 		Sort("vmall_real_money", false).Size(size).From((num - 1) * size).
// 		Do(context.Background())
// 	if err != nil {
// 		return err
// 	}

// 	return res
// }

// // 时间格式化
// func formatTime(stime string) string {
// 	s := make([]string, 0)
// 	for _, v := range strings.Split(stime, "-") {
// 		vv, err := strconv.Atoi(v)
// 		if err != nil {
// 			panic(err)
// 		}
// 		if vv <= 9 {
// 			v = "0" + v
// 		}
// 		s = append(s, v)
// 	}
// 	return strings.Join(s, "-")
// }
