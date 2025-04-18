# -*- coding:utf-8 -*-
#!/usr/bin/python3.6
import sys
import getopt

def help_message():
    print(f"Usage: python3.6 {sys.argv[0]} -h for help")
    print("    -h|--help      帮助信息")
    print("    -u|--url       jenkins接口地址")
    print("    -n|--username  jenkins用户名")
    print("    -j|--jobname   jenkins中需要被终止的job名")


# 获取命令行参数
url, user_name, job_name = None, None, None
try:
    opts, _ = getopt.getopt(sys.argv[1:], "hu:n:j:", ["help", "url=", "username=", "jobname="])
except getopt.GetoptError as _:
    help_message()
    sys.exit(1)
for key, value in opts:
    if key in ("-j", "--jobname"):
        job_name = value
    elif key in ("-u", "--url"):
        url = value
    elif key in ("-n", "--username"):
        user_name = value
    else:
        help_message()
        sys.exit(2)
print(url, user_name, job_name)
