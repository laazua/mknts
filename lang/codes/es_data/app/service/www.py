from datetime import datetime, timedelta
from search.www import SiteConut
from core.enum import CountType
from core.response import Success
from core.response import Failure


async def get_total_count( 
    index, 
    start_time, 
    end_time):
    if not index:
        print("index参数不能为空")
        return Failure(code=40000, message="请传入正确的参数")
    if not start_time or not end_time:
        start_time = (datetime.now()-timedelta(days=120)).strftime("%Y-%m-%d")
        end_time = datetime.now().strftime("%Y-%m-%d")
    site = SiteConut(start_time, end_time)
    keywords = ["server_name", "response_code"]
    data = [ await site.get_www_count(index, keyword) for keyword in keywords]
    if not data:
        return Failure(code=40000, message="获取ES统计数据失败")
    return Success(data=data, message="获取ES统计数据成功")


async def get_time_count(
    index,
    start_time,
    end_time,
    keyword):
    if not index and not start_time and not end_time and not keyword:
        print("请传入正确的参数")
        return Failure(code=40000, message="请传入正确的参数")
    site = SiteConut(start_time, end_time)
    data = await site.get_www_count(index, keyword)
    print(data)