# SQL接口查询

* **文档**    
Elasticsearch的sql接口[参考这里](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/sql-rest-overview.html)

* **示例**
```
# 模型
SELECT DISTINCT "your_field_name", COUNT(*) as doc_count
FROM "your_index_name"
WHERE "your_date_field" >= '{start_date}' 
AND "your_date_field" <= '{end_date}'
GROUP BY "your_field_name"
ORDER BY doc_count DESC
--------------------------------------------------------
# kibana的接口查询示例format支持多种文件(json,yaml等等)
GET /_sql?format=txt
{
  "query": """
  SELECT server_name, count(*) as doc_count  FROM "access-www-bobao" 
  WHERE "@timestamp" >= '2023-07-01' 
  AND  "@timestamp" <= '2023-08-05'
  GROUP BY server_name
  ORDER BY doc_count
  """
}
```