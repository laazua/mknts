"""
date: 2024-01-08
"""
import os

import xlsxwriter

from src.count_es.log import Logger
from src.count_es.config import config


def _format_cnt(data=None):
    """format es domain's data"""
    if data is None:
        Logger.error("Need ES data!")
        return None
    cnt = []
    for cnt_data in data:
        if cnt_data["key"] in ("r-clear-1.xxxx.com", "r-clear-2.xxxx.com"):
            continue
        mdata = []
        mdata.append(["日期", "域名", "次数"])
        for d in cnt_data["day"]["buckets"]:
            mdata.append([d["key_as_string"], cnt_data["key"], d["doc_count"]])
        cnt.append(mdata)
    # Logger.info(f"站点访问统计: {cnt}")
    return cnt


def _format_code(data=None):
    """format es code's data"""
    if data is None:
        Logger.error("Need ES data!")
        return None
    code = []
    for code_data in data:
        if code_data["key"] in ("r-clear-1.xxxx.com", "r-clear-2.xxxx.com"):
            continue
        mdata = []
        mdata.append(["域名", "状态码", "次数"])
        for d in code_data["code"]["buckets"]:
            mdata.append([code_data["key"], d["key"], d["doc_count"]])
        code.append(mdata)
    return code


def _format_path(data=None):
    """format es path's data"""
    if data is None:
        Logger.error("Need ES data!")
        return None
    path = []
    for path_data in data:
        if path_data["key"] in ("r-clear-1.xxxx.com", "r-clear-2.xxxx.com"):
            continue
        mdata = []
        mdata.append(["域名", "路由", "次数"])
        for d in path_data["path"]["buckets"]:
            mdata.append(
                [
                    path_data["key"],
                    d["key"],
                    d["doc_count"],
                    d["code"]["buckets"],
                    d["time"]["values"],
                ]
            )
        path.append(mdata)
    return path


def _format_city(data=None):
    """format es city's data"""
    if data is None:
        Logger.error("Need ES data!")
        return None
    city = []
    for city_data in data:
        if city_data["key"] in ("r-clear-1.xxxx.com", "r-clear-2.xxxx.com"):
            continue
        mdata = []
        mdata.append(["域名", "地区", "次数"])
        for d in city_data["city"]["buckets"]:
            mdata.append([city_data["key"], d["key"], d["doc_count"]])
        city.append(mdata)
    return city


def _format_ip(data=None):
    """format es ip's data"""
    if data is None:
        Logger.error("Need ES data!")
        return None
    ips = []
    for ip_data in data:
        if ip_data["key"] in ("r-clear-1.xxxx.com", "r-clear-2.xxxx.com"):
            continue
        mdata = []
        mdata.append(["域名", "IP地址", "次数"])
        for d in ip_data["clientip"]["buckets"]:
            mdata.append([ip_data["key"], d["key"], d["doc_count"]])
        ips.append(mdata)
    return ips


def _format_comment(data1, data2):
    comment = "状态码    次数\n"
    for d in data1:
        comment = comment + f"    {d['key']}    {d['doc_count']}\n"
    comment = comment + "\n请求时间(百分位,秒)\n"
    for d in data2.items():
        comment = comment + f"    {d[0]}    {round(d[1], 5)}\n"
    return comment


def create_xlsx(name, data):
    """create data of sheet and data of chart"""
    xlsxpath = config.get("app", "xlsxpath")
    if not os.path.exists(xlsxpath):
        os.makedirs(xlsxpath)
    workbook = xlsxwriter.Workbook(f"{xlsxpath}/{name}")

    cnt_sheet = workbook.add_worksheet("访问量")
    code_sheet = workbook.add_worksheet("状态码")
    path_sheet = workbook.add_worksheet("路由")
    city_sheet = workbook.add_worksheet("城市地区")
    ip_sheet = workbook.add_worksheet("访问IP")

    # cell_format = workbook.add_format({'bold': True})
    # cell_format.set_bg_color('green')

    cnt_data = _format_cnt(data)
    if cnt_data is None:
        Logger.error("未获取到ES数据")
        raise Exception("未获取到ES数据")
    cnt_chart = workbook.add_chart({"type": "line"})
    cnt_sheet_line(cnt_sheet, cnt_chart, cnt_data)

    code_data = _format_code(data)
    if code_data is None:
        Logger.error("未获取到ES数据")
        raise Exception("未获取到ES数据")
    code_sheet_column(code_sheet, workbook, code_data)

    path_data = _format_path(data)
    if path_data is None:
        Logger.error("未获取到ES数据")
        raise Exception("未获取到ES数据")
    sheet_and_pie(path_sheet, workbook, path_data, "路由")

    city_data = _format_city(data)
    if city_data is None:
        Logger.error("未获取到ES数据")
        raise Exception("未获取到ES数据")
    sheet_and_pie(city_sheet, workbook, city_data, "城市地区")

    ip_data = _format_ip(data)
    if ip_data is None:
        Logger.error("未获取到ES数据")
        raise Exception("未获取到ES数据")
    sheet_and_pie(ip_sheet, workbook, ip_data, "访问IP")

    workbook.close()


def cnt_sheet_line(worksheet, chart, data):
    flag = 0
    for idx, item in enumerate(data, start=1):
        worksheet.add_table(f"A{idx*1+flag}:C{len(item)+idx*1+flag}", {"data": item})
        chart.add_series(
            {
                "name": f"=访问量!$B{idx*1+flag+3}",
                "categories": f"=访问量!$A{idx+2+flag}:$A${len(item)+idx*1+flag}",
                "values": f"=访问量!$C{idx+2+flag}:$C${len(item)+idx*1+flag}",
            }
        )
        flag = flag + len(item)
    chart.set_title({"name": "站点访问量"})
    chart.set_style(10)
    chart.set_size({"width": 720, "height": 480})
    worksheet.insert_chart("E3", chart, {"x_offset": 25, "y_offset": 15})
    worksheet.autofit()


def code_sheet_column(worksheet, workbook, data):
    flag = 0
    for idx, item in enumerate(data, start=1):
        chart = workbook.add_chart({"type": "doughnut"})
        worksheet.add_table(f"A{idx*1+flag}:C{len(item)+idx*1+flag}", {"data": item})
        chart.add_series(
            {
                "name": f"=状态码!$A{item[2][0]}",
                "categories": f"=状态码!$B{idx+2+flag}:$B${len(item)+idx*1+flag}",
                "values": f"=状态码!$C{idx+2+flag}:$C${len(item)+idx*1+flag}",
            }
        )
        # print(f"$B{idx+2+flag}:$B${len(item)+idx*1+flag}")
        chart.set_title(
            {
                "name": f"=状态码!$A{idx*1+flag+2}",
                "num_font": {"name": "Arial", "size": 16, "italic": True},
            }
        )
        chart.set_style(10)
        chart.set_size({"width": 340, "height": 180})
        worksheet.insert_chart(
            f"E{idx+1+flag}", chart, {"x_scale": 1.0, "y_scale": 1.0}
        )
        flag = flag + len(item)
    worksheet.autofit()


def sheet_and_pie(worksheet, workbook, data, tbname):
    flag = 0
    for idx, item in enumerate(data, start=1):
        chart = workbook.add_chart({"type": "pie"})
        worksheet.add_table(f"A{idx*1+flag}:C{len(item)+idx*1+flag}", {"data": item})
        chart.add_series(
            {
                "name": f"={tbname}!$A${idx*1+flag+3}",
                "categories": f"={tbname}!$B${idx+2+flag}:$B${len(item)+idx*1+flag}",
                "values": f"={tbname}!$C${idx+2+flag}:$C${len(item)+idx*1+flag}",
            }
        )
        for i, m in enumerate(item[1:]):
            if len(m) == 5:
                comment = _format_comment(m[3], m[4])
                if flag == 0:
                    worksheet.write_comment(f"C{flag+i+3}", comment)
                else:
                    worksheet.write_comment(f"C{flag+i+2+idx}", comment)
        chart.set_title(
            {
                "name": f"={tbname}!$A{idx*1+flag+2}",
                "num_font": {"name": "Arial", "size": 16, "italic": True},
            }
        )
        chart.set_style(10)
        chart.set_size({"width": 480, "height": 360})
        worksheet.insert_chart(
            f"E{idx+1+flag}", chart, {"x_scale": 1.0, "y_scale": 1.0}
        )
        flag = flag + len(item)
    worksheet.autofit()
