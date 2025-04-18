package utils

import (
	"context"
	"msbn/global"
	"strconv"
	"strings"
	"time"

	"github.com/olivere/elastic/v7"
)

// 充值排行
func GetRechargeRank(stime, etime time.Time, zone string, size, num int) (*elastic.SearchResult, error) {
	// fmt.Println("xxxxx", client)
	// stime = formatTime(stime)
	// etime = formatTime(etime)
	// 组合查询
	b := elastic.NewBoolQuery().Must()
	b.Filter(elastic.NewRangeQuery("@timestamp").Gte(stime).Lte(etime).Format("strict_date_optional_time"),
		elastic.NewExistsQuery("properties.pay_amount"),
		elastic.NewMatchPhraseQuery("properties.server_id", zone))
	// 获取查询结果
	res, err := global.EsClient.Search().
		Index("gamelog-*").
		Query(b).
		Sort("properties.pay_amount", false).
		Size(size).
		From((num - 1) * size).
		Do(context.Background())
	if err != nil {
		return nil, err
	}
	return res, nil
}

// 等级分布
func GetGradeDistribution(stime, etime time.Time, zone string, size, num int) (*elastic.SearchResult, error) {
	// stime = formatTime(stime)
	// etime = formatTime(etime)
	// 组合查询
	b := elastic.NewBoolQuery().Must()
	b.Filter(elastic.NewRangeQuery("@timestamp").Gte(stime).Lte(etime),
		elastic.NewExistsQuery("properties.role_level"),
		elastic.NewMatchPhraseQuery("properties.server_id", zone))
	// 聚合指标
	a := elastic.NewTermsAggregation().Field("properties.role_level").OrderByCountDesc().Size(100)
	n := elastic.NewNestedAggregation().Path("")
	// 获取查询结果
	res, err := global.EsClient.Search().
		Index("gamelog-*").
		Query(b).
		Aggregation("roleLevel", a).
		Aggregation("Netsted", n).
		Size(size).
		From((num - 1) * size).
		Do(context.Background())
	if err != nil {
		return nil, err
	}

	return res, nil
}

// 数据查询
func GetData(stime, etime time.Time, zone string, size, num int) (*elastic.SearchResult, error) {
	// stime = formatTime(stime)
	// etime = formatTime(etime)

	// 组合查询
	b := elastic.NewBoolQuery().Must()
	b.Filter(elastic.NewRangeQuery("@timestamp").Gte(stime).Lte(etime),
		elastic.NewMatchPhraseQuery("properties.server_id", zone))

	// 获取查询结果
	resp, err := global.EsClient.Search().Index("gamelog-*").Query(b).
		Size(size).From((num - 1) * size).Do(context.Background())
	if err != nil {
		return nil, err
	}
	return resp, nil
}

// 获取滚服数据
func GetRollData() (*elastic.SearchResult, error) {
	stime := "2022-01-01"
	etime := "2022-02-22"
	zone := 997

	// 组合查询
	b := elastic.NewBoolQuery()
	b.Filter(
		elastic.NewMatchPhraseQuery("properties.server_id", zone),
		elastic.NewRangeQuery("@timestamp").Gte(stime).Lte(etime),
	)
	// 获取结果
	resp, err := global.EsClient.Search().Index("gamelog-*").Query(b).Do(context.Background())
	if err != nil {
		return nil, err
	}

	return resp, nil
}

// 时间格式转换
func formatTime(stime string) string {
	s := make([]string, 0)
	for _, v := range strings.Split(stime, "-") {
		vv, err := strconv.Atoi(v)
		if err != nil {
			panic(err)
		}
		if vv <= 9 {
			v = "0" + v
		}
		s = append(s, v)
	}
	return strings.Join(s, "-")
}
