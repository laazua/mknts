import asyncio
import app.search.sql as sql
from app.core.enum import CountType
from app.core.elastic import ESConn


class SiteConut:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    async def execute_query(self, query):
        """es数据查询"""
        # 控制并发数量为5个协程
        semaphore = asyncio.Semaphore(5)
        async with semaphore:
            with ESConn() as conn:
                return await asyncio.to_thread(conn.sql.query, body={"query": query}) 

    async def get_www_count(self, index, keyword):
        """统计访问次数"""
        counts  = {"name": keyword}
        queries = [
            sql.total.format(keyword, index, self.start_time, self.end_time),
            sql.users.format(keyword, index, self.start_time, self.end_time),
            sql.other.format(keyword, index, self.start_time, self.end_time),
            ]
        tasks = [ self.execute_query(query) for query in queries ]
        results =  await asyncio.gather(*tasks)
        for result in results:
            match result["columns"][1]["name"]:
                case CountType.TOTAL.value:
                    counts[CountType.TOTAL] = result["rows"]
                case CountType.USER.value:
                    counts[CountType.USER]  = result["rows"]
                case CountType.OTHER.value:
                    counts[CountType.OTHER] = result["rows"]
        return counts
    
    async def get_www_frequency(self):
        """统计指定字段的频率"""
        pass
