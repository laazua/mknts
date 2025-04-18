"""
date: 2024-01-05
"""
import asyncio
# import calendar
# import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

from src.count_es import req
from src.count_es import dsl
from src.count_es import xlsx
from src.count_es import utils
from src.count_es.log import Logger


def _week_task():
    """week count"""
    try:
        asyncio.run(_run(dsl.CntType.Week))
    except Exception as e:
        Logger.error("月任务结束: ", e)

def _month_task():
    """month count"""
    try:
        asyncio.run(_run(dsl.CntType.Month))
    except Exception as e:
        Logger.error("周任务结束: ", e)

async def _run(cnt_type):
    """request data from es"""
    
    tasks = [ asyncio.create_task(req.get_data(name, cnt_type)) for name in dsl.IDX_MAP.keys() ]
    for result in await asyncio.gather(*tasks):
        for key, value in result.items():
            xlsx.create_xlsx(f"{key}.xlsx", value)
            # print(key, value)
            if cnt_type == dsl.CntType.Month:
                for data in req.format_index_data(value):
                    req.post_index_data(data)


def main():
    Logger.info("running...")
    scheduler = BlockingScheduler()
    # scheduler = AsyncIOScheduler()
    #####################################月定时任务######################################
    #每月第一天09:10统计数据
    scheduler.add_job(_month_task, 'cron', day=1, hour=9, minute=10)
    #每月的第一天09:20发送邮件
    scheduler.add_job(utils.send_email, 'cron', day=1, hour=9, minute=20, args=("上月数据统计",))
    #备份每月数据统计的xlsx文件
    scheduler.add_job(utils.back_xlsx, 'cron', day=1, hour=9, minute=25, args=("month",))
     
    #####################################周定时任务######################################
    #每周五早上09:26统计数据
    scheduler.add_job(_week_task, 'cron', day_of_week='fri', hour=9, minute=26)
    #每周五早上09:36发送邮件
    scheduler.add_job(utils.send_email, 'cron', day_of_week='fri', hour=9, minute=36, args=("当前七天内数据统计",), kwargs={'people': "rd_huheng"})
    scheduler.add_job(utils.send_email, 'cron', day_of_week='fri', hour=9, minute=36, args=("当前七天内数据统计",), kwargs={'people': "rd_jiangshuangquan"})
    #备份每周数据统计的xlsx文件
    scheduler.add_job(utils.back_xlsx, 'cron', day_of_week='fri', hour=9, minute=40, args=("week",))

    scheduler.start()

    #==== test ====#
    #_month_task()
    # utils.send_email("上月数据统计", people="rd_huheng")