package utils

import (
	"context"
	"msbn/global"

	"github.com/olivere/elastic/v7"
)

// 订单查询
func GetOrder(zone, uid, order string) (*elastic.SearchResult, error) {
	// 组合查询
	b := elastic.NewBoolQuery().Must()
	b.Filter(
		elastic.NewMatchPhraseQuery("properties.server_id", zone),
		elastic.NewMatchPhraseQuery("properties.order_id", order),
		elastic.NewMatchPhraseQuery("properties.uid", uid),
	)
	// 获取结果
	res, err := global.EsClient.Search().
		Index("gamelog-*").
		Query(b).
		Do(context.Background())
	if err != nil {
		return nil, err
	}

	return res, nil
}

// 货币查询
func GetCurrency() {

}

// 角色查询
func GetRole(zone, uid string) (*elastic.SearchResult, error) {
	// 组合查询
	b := elastic.NewBoolQuery()
	b.Filter(
		elastic.NewMatchPhraseQuery("properties.server_id", zone),
		elastic.NewMatchPhraseQuery("properties.uid", uid),
	)
	res, err := global.EsClient.Search().
		Index("gamelog-*").
		Query(b).
		Do(context.Background())
	if err != nil {
		return nil, err
	}
	return res, nil
}

func GetLog() {

}

// 详细信息
func GetDetail() {

}
