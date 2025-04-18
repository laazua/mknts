# -*- coding: utf-8 -*-
#!/usr/bin/python3.6
import sys
import json
import getopt
import base64
import urllib.error
import urllib.parse as parse
import urllib.request as requests

# 此脚本用于操作jenkins的api接口,用于控制同一时间段，只允许有一个流水线实例运行


# Jenkins API Token
api_token = '11989fb125a0640799409326072ce1e7fa'


def help_message():
    print(f"Usage: python3.6 {sys.argv[0]} -h for help")
    print("    -h|--help      帮助信息")
    print("    -u|--url       jenkins接口地址")
    print("    -n|--username  jenkins登录用户名")
    print("    -j|--jobname   jenkins中需要被终止的job名")


def api_auth(url, auth, data=None):
    """
    接口认证
    url: api接口地址, 字符串类型
    auth: 认证信息, 元组类型
    """
    request = requests.Request(url, data)
    base64_auth = base64.b64encode(f"{auth[0]}:{auth[1]}".encode("ascii")).decode("ascii")
    request.add_header(f"Authorization", f"Basic {base64_auth}")
    request.add_header("Content-Type", "application/json")
    
    return request


def get_api_data(request):
    """
    获取接口数据
    url: api接口地址, 字符串类型
    """
    response = requests.urlopen(request)
    data = json.load(response)
    
    return data


if __name__ == "__main__":
    # 获取命令行参数
    api_url, user_name, job_name, status_code = None, None, None, None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:n:j:", ["help", "url=", "username=", "jobname="])
    except getopt.GetoptError as _:
        help_message()
        sys.exit(1)
    for key, value in opts:
        if key in ("-j", "--jobname"):
            job_name = value
        elif key in ("-u", "--url"):
            api_url = value
        elif key in ("-n", "--username"):
            user_name = value
        else:
            help_message()
            sys.exit(2)

    if not api_url or not user_name or not job_name:
        sys.exit(2)
    auth = (user_name, api_token)
    # 获取构建的任务信息
    jobs_url = f"{api_url}/api/json?tree=jobs[name,builds[number]]"
    request = api_auth(jobs_url, auth)
    data = get_api_data(request)
    # 遍历jobs进行任务停止
    for job in data["jobs"]:
        if job["name"] != job_name:
            continue
        if not job["builds"]:
            continue
        job["builds"].sort(key=lambda build: build["number"], reverse=True)
        for build in job["builds"][1:]:
            stop_url = f"{api_url}/job/{job['name']}/{build['number']}/stop"
            params = {"tree": "jobs[name,color,url,buildable,lastBuild[timestamp],queueItem[why]]"}
            encode_data = parse.urlencode(params).encode("utf-8")
            request = api_auth(stop_url, auth, encode_data)
            try:
                with requests.urlopen(request) as response:
                    status_code = response.getcode()
                    body = response.read().decode('utf-8')
                    sys.exit(0)
            except urllib.error.HTTPError as error:
                    status_code = error.code
                    print(f'HTTP Error: {status_code}')
                    body = error.read().decode('utf-8')
                    sys.exit(3)
