# 统计字段频率
day_sql = """
    SELECT DATE_TRUNC('day', your_date_field) as day, COUNT(*) as frequency
    FROM your_index_name
    WHERE your_date_field >= 'start_date' AND your_date_field <= 'end_date'
    GROUP BY day
    ORDER BY day;
    """
# 统计字段并排除一些字段的特定值
exclude_sql = """
    SELECT DATE_TRUNC('day', your_date_field) as day, COUNT(*) as count
    FROM your_index_name
    WHERE your_date_field >= 'start_date' AND your_date_field <= 'end_date'
    AND your_field_name NOT IN ('excluded_value_1', 'excluded_value_2', ...)
    GROUP BY day
    ORDER BY day;
    """
# 统计频率
freq_sql = """
    SELECT HISTOGRAM("@timestamp", INTERVAL 1 DAY) as d, clientip, count(*) as doc_count
    FROM "k8s-nginx"
    WHERE "@timestamp" >= '2023-07-01'
    AND "@timestamp" <= '2023-08-09'
    AND "clientip" IS NOT NULL
    GROUP BY d, clientip
    """
# 统计每个地区ip次数
eara_ip_sql = """
    SELECT geoip.region_name AS region, COUNT(*) AS access_count
    FROM "k8s-nginx"
    WHERE "@timestamp" >= '2023-07-01' 
    AND "@timestamp" <= '2023-08-09'
    AND region IS NOT NULL
    GROUP BY region
    ORDER BY access_count DESC
    """

total = """
    SELECT "{0}", count(*) as total
    FROM "{1}" WHERE "@timestamp" >= '{2}'
    AND "@timestamp" <= '{3}' 
    AND "{0}" IS NOT NULL
    GROUP BY "{0}"
    """
users = """
    SELECT "{0}", count(*) as user 
    FROM "{1}" WHERE "@timestamp" >= '{2}'
    AND "@timestamp" <= '{3}'
    AND "UA_device" NOT IN ('Other', 'Spider')
    AND "{0}" IS NOT NULL
    GROUP BY "{0}"
    """
other = """
    SELECT "{0}", count(*) as other 
    FROM "{1}" WHERE "@timestamp" >= '{2}'
    AND "@timestamp" <= '{3}'
    AND "UA_device" IN ('Other', 'Spider')
    AND "{0}" IS NOT NULL
    GROUP BY "{0}"
    """

day_freq_sql = """
    SELECT HISTOGRAM("@timestamp", INTERVAL 1 DAY) as d, "{}", count(*) as doc_count
    FROM "{}"
    WHERE "@timestamp" >= '{}'
    AND "@timestamp" <= '{}'
    AND "{}" IS NOT NULL
    GROUP BY d, {}
    """
week_freq_sql = """
    SELECT HISTOGRAM("@timestamp", INTERVAL 1 WEEK) as d, "{}", count(*) as doc_count
    FROM "{}"
    WHERE "@timestamp" >= '{}'
    AND "@timestamp" <= '{}'
    AND "{}" IS NOT NULL
    GROUP BY d, {}
    """