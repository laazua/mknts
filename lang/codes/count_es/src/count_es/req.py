"""
date: 2024-01-05
"""

import json
import http
import datetime
import calendar

import requests

from src.count_es import dsl
from src.count_es.log import Logger
from src.count_es.config import config


async def get_data(name, cnt_type):
    """Get data from ES"""
    data, params = None, None
    index = _format_index(name)
    if not index:
        raise "Format Index Error!"
    url = config.get("es", "addr") + f"/{index}/_search"
    auth = (config.get("es", "user"), config.get("es", "passwd"))
    if cnt_type == dsl.CntType.Week:
        params = _format_dsl(name, dsl.CntType.Week)
    else:
        params = _format_dsl(name, dsl.CntType.Month)
    if not params:
        raise "Format DSL Error!"
    try:
        resp = requests.get(url, auth=auth, json=params, timeout=60)
        data = json.loads(resp.content.decode("utf-8"))["aggregations"]["server_name"][
            "buckets"
        ]
        Logger.info("Get ES data success.")
        resp.close()
    except Exception as e:
        Logger.error("Get ES data error! ", e)

    return {name: data}


def _format_month_date():
    # 获取当前日期和时间
    current_date = datetime.datetime.now()

    # 计算上一个月的年份和月份
    if current_date.month == 1:
        prev_month_year = current_date.year - 1
        prev_month = 12
    else:
        prev_month_year = current_date.year
        prev_month = current_date.month - 1

    # 获取上一个月的第一天和最后一天
    first_day = datetime.datetime(prev_month_year, prev_month, 1)
    _, last_day = calendar.monthrange(prev_month_year, prev_month)
    last_day = datetime.datetime(prev_month_year, prev_month, last_day, 23, 59, 59)

    # 格式化日期
    formatted_first_day = first_day.strftime("%Y-%m-%dT%H:%M:%S")
    formatted_last_day = last_day.strftime("%Y-%m-%dT%H:%M:%S")
    return formatted_first_day, formatted_last_day


def _foramt_week_date():
    # 获取当前日期和时间
    current_date = datetime.datetime.now().date()

    # 计算前7天的日期和时间
    start_date = current_date - datetime.timedelta(days=7)
    end_date = current_date - datetime.timedelta(days=1)

    # 将时间设置为 00:00:00
    start_datetime = datetime.datetime.combine(start_date, datetime.datetime.min.time())
    end_datetime = datetime.datetime.combine(
        end_date, datetime.datetime.strptime("23:59:59", "%H:%M:%S").time()
    )

    return start_datetime.strftime("%Y-%m-%dT%H:%M:%S"), end_datetime.strftime(
        "%Y-%m-%dT%H:%M:%S"
    )


def _format_dsl(name, cnt_type):
    """Format dsl statement"""
    _dsl = None
    format_week = _foramt_week_date()
    format_month = _format_month_date()
    if cnt_type == dsl.CntType.Week:
        dsl.WEEK_CNT["query"]["bool"]["must"][1]["range"]["@timestamp"]["gte"] = (
            format_week[0]
        )
        dsl.WEEK_CNT["query"]["bool"]["must"][1]["range"]["@timestamp"]["lte"] = (
            format_week[1]
        )
        dsl.WEEK_CNT["query"]["bool"]["must"][0]["wildcard"]["server_name.keyword"] = (
            f"*.{name}.com"
        )
        _dsl = dsl.WEEK_CNT
    if cnt_type == dsl.CntType.Month:
        dsl.MOUTH_CNT["query"]["bool"]["must"][1]["range"]["@timestamp"]["gte"] = (
            format_month[0]
        )
        dsl.MOUTH_CNT["query"]["bool"]["must"][1]["range"]["@timestamp"]["lte"] = (
            format_month[1]
        )
        dsl.MOUTH_CNT["query"]["bool"]["must"][0]["wildcard"]["server_name.keyword"] = (
            f"*.{name}.com"
        )
        _dsl = dsl.MOUTH_CNT

    return _dsl


def _format_index(name):
    """Format index name"""
    try:
        if name in dsl.IDX_MAP:
            return dsl.IDX_MAP[name]
    except Exception as _:
        return None


def post_index_data(data):
    now_time = datetime.datetime.now().strftime("%Y-%m")
    url = f"{config.get('es', 'addr')}/{data['index']}-count-es-{now_time}"
    headers = {"Content-Type": "application/json"}
    auth = (config.get("es", "user"), config.get("es", "passwd"))
    if not _check_index(f"{data['index']}-count-es-{now_time}"):
        _put_index(url, auth, data["mapping"])
    with requests.post(
        f"{url}/_doc", auth=auth, json=data["data"], headers=headers, timeout=60
    ) as resp:
        if resp.status_code == http.HTTPStatus.CREATED:
            Logger.info("添加索引数据成功")
        else:
            Logger.error("添加索引数据失败")


def _check_index(index):
    url = config.get("es", "addr") + f"/_cat/indices/{index}"
    auth = (config.get("es", "user"), config.get("es", "passwd"))
    try:
        resp = requests.get(url, auth=auth, timeout=60)
        if "green" in resp.content.decode("utf-8"):
            return True
    except Exception as error:
        Logger.error("检查索引是否存在出错: ", error)
    return False


def _put_index(url, auth, index):
    try:
        with requests.put(url, auth=auth, json=index, timeout=60) as resp:
            if resp.status_code == http.HTTPStatus.OK:
                Logger.info("创建索引成功")
            else:
                Logger.error("创建索引失败")
    except Exception as e:
        Logger.error("_put_index: 创建索引失败", e)


def format_index_data(data):
    """格式化索引数据"""
    ## 有问题mapping跟data对不上
    list_data = []
    for d in data:
        codes = []
        dict_data = {}
        dsl.TotalIndex["mappings"]["properties"]["code"]["properties"] = {}
        for c in d["code"]["buckets"]:
            codes.append({f"{c['key']}": c["doc_count"]})
            dsl.TotalIndex["mappings"]["properties"]["code"]["properties"][
                f"{c['key']}"
            ] = {"type": "integer"}
        dict_data["domain"] = d["key"]
        dict_data["count"] = d["doc_count"]
        dict_data["code"] = codes
        index = f"{d['key']}".split(".")[-2]
        list_data.append({"mapping": dsl.TotalIndex, "data": dict_data, "index": index})
    # print(list_data)
    return list_data
