"""Elasticsearch接口"""
from fastapi import APIRouter
import service.www as service_www


api = APIRouter(
    prefix="/dev-api/es",
    tags=["elastic api"]
)


@api.get("/www")
async def get_all_www_count( 
    index, 
    start_time, 
    end_time):
    """     
    :start_time: 统计的起始时间点, 格式: 2023-07-01    
    :end_time: 统计的结束时间点, 格式: 2023-08-09    
    :index: ES集群中的索引名称, 示例: k8s-nginx    
    :coun_type: 统计的分类， 说明: 'total:总量'|'user:用户量'|'other:其他'    
    """
    return await service_www.get_total_count(index, start_time, end_time)


@api.get("/web")
async def get_www_count(
    index,
    start_time,
    end_time,
    keyword):
    return await service_www.get_time_count(index, start_time, end_time, keyword)