#!/bin/bash

### postman es增删改查

## es创建索引
# postman 向http://ip:9200/indexname 发送put请求

## es获取单个索引
# postman 向http://ip:9200/indexname 发送get请求
## es获取所有索引
# postman 向http://ip:9200/_cat/indices?v 发送get请求

## es删除索引
# postman 向http://ip:9200/indexname 发送delete请求

## es向索引添加文档数据
# postman 向http://ip:9200/indexname/_doc 发送post请求


## match match_all match_phrase

:<<!
{
    "query": {
        "bool": {
            "must": [
                {
                    "match": {
                        "itemName": "itemValue"
                    }
                },
                {
                    "match": {
                        "itemName": "itemValue"
                    }
                }
            ],
            "filter": {
                "range": {
                    "timeName": {
                        "gt": 1000
                    }
                }
            }
        }
    }
}

{
    "query": {
        "bool": {
            "should": [
                {
                    "match": {
                        "itemName": "itemValue"
                    }
                },
                {
                    "match": {
                        "itemName": "itemValue"
                    }
                }
            ]
        }
    }
}


{
    "aggs": { // 聚合操作
        "item_group": {  // 名称,自起
            "terms": {
                "field":
            }
        }
    },
    "size": 0
}
!