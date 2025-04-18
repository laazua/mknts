package dao

import (
	"bnzt/global"
	"bnzt/models"
	"context"

	"github.com/olivere/elastic/v7"
)

type Operation interface {
	GetRechaRank(rrs models.Rrs) (*elastic.SearchResult, error)
	GetGradeDist(Gds models.Gds) (*elastic.SearchResult, error)
	GetCountData(dgs models.Dgs) (*elastic.SearchResult, error)
}

func NewOperation() Operation {
	return &operation{}
}

type operation struct{}

// 查询充值排行数据
func (operation) GetRechaRank(rrs models.Rrs) (*elastic.SearchResult, error) {
	// 创建查询对象
	b := elastic.NewBoolQuery()
	b.Filter(elastic.NewRangeQuery("@timestamp").
		Gte(rrs.Stime).Lte(rrs.Etime).Format("strict_date_optional_time"),
		elastic.NewExistsQuery("properties.pay_amount"),
		elastic.NewMatchPhraseQuery("properties.server_id", rrs.Zone))
	// 聚合条件
	paySum := elastic.NewSumAggregation().Field("properties.pay_amount")
	lasTime := elastic.NewMaxAggregation().Field("@timestamp")
	payNum := elastic.NewTermsAggregation().Size(1000).Field("#account_id").
		SubAggregation("paySum", paySum).SubAggregation("time", lasTime)
	// 发送请求
	// result, err := global.EsClient.Search().Index("gamelog-*").Query(b).
	// 	Sort("properties.pay_amount", false).Size(rrs.Page.Size).
	// 	From((rrs.Page.Num - 1) * rrs.Page.Size).Do(context.Background())
	result, err := global.EsClient.Search().Index("gamelog-*").Query(b).
		Size(0).Aggregation("payNum", payNum).Do(context.Background())
	if err != nil {
		return nil, err
	}
	return result, nil
}

// 查询等级分布数据
func (operation) GetGradeDist(gds models.Gds) (*elastic.SearchResult, error) {
	// 创建查询对象
	b := elastic.NewBoolQuery()
	b.Filter(elastic.NewRangeQuery("@timestamp").
		Gte(gds.Stime).Lte(gds.Etime).Format("strict_date_optional_time"),
		elastic.NewExistsQuery("properties.role_level"),
		elastic.NewMatchPhraseQuery("properties.server_id", gds.Zone))
	// 聚合条件
	paySum := elastic.NewSumAggregation().Field("properties.pay_amount")
	payNum := elastic.NewTermsAggregation().Field("#account_id").SubAggregation("payNum", paySum)
	// 发送请求
	result, err := global.EsClient.Search().Index("gamelog-*").Query(b).
		Aggregation("payNum", payNum).Size(1000).
		Do(context.Background())
	if err != nil {
		return nil, err
	}
	return result, nil
}

// 查询基础数据
func (operation) GetCountData(dgs models.Dgs) (*elastic.SearchResult, error) {
	// 创建查询对象
	b := elastic.NewBoolQuery()
	b.Filter(elastic.NewRangeQuery("@timestamp").
		Gte(dgs.Stime).Lte(dgs.Etime).Format("strict_date_optional_time"),
		elastic.NewExistsQuery("properties.register_time"),
		elastic.NewMatchPhraseQuery("properties.server_id", dgs.Zone))
	// 发送请求
	result, err := global.EsClient.Search().Index("gamelog-*").Query(b).Size(1000).
		Do(context.Background())
	if err != nil {
		return nil, err
	}
	return result, nil
}
