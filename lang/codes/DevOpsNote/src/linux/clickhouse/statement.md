
```
### 查看数据库中具体表大小
SELECT 
    table,
    sum(rows) AS total_rows,
    sum(bytes_on_disk) AS total_bytes
FROM 
    system.parts
WHERE 
    database = 'db_name' 
    AND table = 'table_name'
    AND active = 1
GROUP BY 
    table;

### 查看数据库大小
SELECT 
    database,
    sum(bytes_on_disk) AS total_database_size
FROM 
    system.parts
WHERE 
    active = 1
GROUP BY 
    database
ORDER BY 
    total_database_size DESC;


### 查看数据库中表大小
SELECT
    table,
    sum(bytes_on_disk) AS total_bytes
FROM system.parts
WHERE (database = 'system') AND (active = 1)
GROUP BY table
ORDER BY total_bytes DESC


### 查询表指定日期范围数据大小
select count(*) from trace_log where event_date >= '2023-06-25' and  event_date <= '2024-06-20';
# 删除表指定日期范围内数据
alter table trace_log delete where event_date >= '2023-09-30' and  event_date <= '2024-05-31';

### 设置表TTL
ALTER table `system`.query_log MODIFY TTL event_date + toIntervalDay(30);

### 查询任务队列
select database,table,command,create_time,is_done from mutations order by create_time desc limit 10

### 查询表结构
show create table part_log;

### 设置表ttl
ALTER table query_log MODIFY TTL event_date + toIntervalDay(15);

### 根据日志中的uuid查询执行的语句
select * from system.tables where uuid = '';

### 取消未完成的执行语句
1. 先查询出未完成的执行语句
SELECT
    database,
    table,
    command,
    create_time,
    is_done
FROM system.mutations
WHERE is_done = 0
ORDER BY create_time DESC

2. 取消未完成的执行语句
KILL MUTATION WHERE database = 'your_database_name' AND table = 'your_table_name' AND command = 'your_command';

### 查询任query日志
1. DESCRIBE TABLE system.query_log;
2. SELECT * FROM system.query_log WHERE query_id ='b3000b06-57dc-41a0-8a42-d7293d972f26' 
```
