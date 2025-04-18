### DSL 查询

- **描述**  
  Elasticsearch 提供了一种 JSON 样式的域特定语言,可用于执行查询,这称为查询 DSL.  
  详细的教程说明[参考这里](https://www.elastic.co/guide/en/elasticsearch/reference/index.html)

- **复合查询类型**

1. bool 查询

```
{
    "query": {
        "bool": {
            "must": {},
            "should": {},
            "must_not": {},
            "filter": {}
        }
    }
}
```

2. boosting 查询

```
{
    "query": {
        "boosting": {
            "positive": {},
            "negative": {},
            "negative_boost": 0.5
        }
    }
}
```

3. constant_score 查询

```
{
    "query": {
        "constant_score": {
            "filter": {},
            "boost": 1.2
        }
    }
}
```

4. dis_max 查询

```
{
    "query": {
        "dis_max": {
            "queries": {},
            "tie_breaker": 0.7
        }
    }
}
```

5. function_score 查询

```
{
  "query": {
    "function_score": {
      "query": { "match_all": {} },
      "boost": "5",
      "random_score": {},
      "boost_mode": "multiply"
    }
  }
}
```

```
{"query":{"bool":"must":[{"match":{"server_name":f"{domain}"}},{"range":{"@timestamp":{"gte":st_time,"lte":ed_time}}}]}},"size":0,"aggs":{"count":{"date_histogram":{"field":"@timestamp","interval":"day"}}}}
```

```
"aggs": {
    "code_cnt": {
      "terms": {
        "field": "response_code.keyword",
        "size": 10
      }
    },
    "city_cnt": {
      "terms": {
        "field": "geoip.city_name",
        "size": 10
      }
    },
    "ip_count": {
      "terms": {
        "field": "clientip",
        "size": 10
      },
      "aggs": {
        "response_200": {
          "filter": {
            "term": {
              "response_code": 200
            }
          }
        }
      }
    }
  }
```

6. 创建索引

```
PUT /cnt_test_2023-12
{
  "settings": {
    "number_of_shards": 1,
    "number_of_replicas": 0
  },
  "mappings": {
    "dynamic": false,
    "properties": {
      "domain": {
        "type": "text"
      },
      "path": {
        "type": "text"
      },
      "count": {
        "type": "text"
      },
      "code": {
        "type": "keyword"
      }
    }
  }
}

# 往索引中写入数据(一条数据对应一个_id)
POST /cnt_test_2023-12/_bulk
{ "index" : { "_index" : "cnt_test_2023-12", "_type" : "_doc", "_id" : "1" } }
{"domain": "www.hancong.com", "path": "/a/b", "count": "125", "code": [["200", 141702], ["403", 1378], ["429", 16], ["499", 10], ["422", 1]]}
{ "index" : { "_index" : "cnt_test_2023-12", "_type" : "_doc", "_id" : "2" } }
{"domain": "www.yuzhua.com", "path": "/a/b", "count": "125", "code": [["200", 141702], ["403", 1378], ["429", 16], ["499", 10], ["422", 1]]}

GET /cnt_test_2023-12/_search
```
