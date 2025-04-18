#coding:utf-8
import os, time

def write(applogs):
    if not os.path.exists("/root/monitor/logs/"):
        os.mkdir("/roo/monitor/logs/")
    
    current_time = time.strftime("%Y%m%d")
    logs = "[" + time.strftime("%Y-%m-%d-%H-%M-%S") +  "]: " + applogs + "\n"
    with open("/root/monitor/logs/"+current_time+".txt", 'w') as fd:
        fd.write(logs)