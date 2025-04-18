# -*- coding: utf-8 -*-
"""
监控主机cpu,磁盘,负载,内存,网络,业务进程
"""
import os
import time
import json
import psutil
import requests
import schedule
from gmcom.config import gmdcon
from gmcom.log import gmdlog
from threading import Timer

host_state = {}

class GmMon:
    def __init__(self):
        self.current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    
    def mon_cpu(self):
        for index, percent in enumerate(psutil.cpu_percent(interval=1, percpu=True)):
            host_state['cpu'] = percent
            if percent > gmdcon.cpu_val:
                cpu_msg = f"cpu num: {index} percent: {percent}"
                gmdlog.writelog(cpu_msg)
                argument = {'msgtype': 'text', 'text': { 'content': self.current_time + ' [SYF] ' + cpu_msg}}
                self.send_msg(argument)

    def mon_disk(self):
        disk_percent = psutil.disk_usage('/data').percent
        disk_msg = f"disk percent: {disk_percent}"
        host_state['disk'] = disk_percent
        gmdlog.writelog(disk_msg)
        if disk_percent > gmdcon.disk_val:
            argument = {'msgtype': 'text', 'text': { 'content': self.current_time + ' [SYF] ' + disk_msg}}
            self.send_msg(argument)

    def mon_mem(self):
        mem_percent = psutil.virtual_memory().percent
        mem_msg = f"mem percent: {mem_percent}"
        host_state['mem'] = mem_percent
        gmdlog.writelog(mem_msg)
        if mem_percent > gmdcon.mem_val:
            argument = {'msgtype': 'text', 'text': { 'content': self.current_time + ' [SYF] ' + mem_msg}}
            self.send_msg(argument)

    def mon_load(self):
        load_percent = psutil.getloadavg()[2]
        host_state['load'] = load_percent
        load_msg = f"load 15: {load_percent}"
        gmdlog.writelog(load_msg)
        if load_percent > gmdcon.load_val:
            argument = {'msgtype': 'text', 'text': { 'content': self.current_time + ' [SYF] ' + load_msg}}
            self.send_msg(argument)

    def mon_net(self):
        pass

    def mon_process(self):
        # 匹配主机上的活跃进程目录
        all_pids = psutil.pids()
        # 匹配主机上的进程目录
        p_dirs = []
        for item in os.listdir(gmdcon.game_dir):
            if item.startswith(gmdcon.game_alias):
                p_dirs.append(gmdcon.game_dir + item)
        # 判断进号文件内容是否为空[为空表示正常关闭]
        gmdlog.writelog("process monitor!!!")
        host_state['num'] = len(p_dirs)
        for pd in p_dirs:
            if os.path.exists(pd + '/tmp/gameserv.pid') and os.path.getsize(pd + '/tmp/gameserv.pid'):
                fd = open(pd + '/tmp/gameserv.pid')
                pid = int(fd.read().strip())
                fd.close()
                if pid not in all_pids:
                    gmdlog.writelog(pd + "异常关闭")
                    argument = {"msgtype": "text", "text": { "content": self.current_time + " [SYF] " + pd + "异常关闭"}, "at": { "isAtAll": True }}
                    self.send_msg(argument)
    
    def mon_conn(self):
        num = 1
        for con in  psutil.net_connections(kind='tcp4'):
            if con.status == 'ESTABLISHED':
               num = num + 1
        host_state['conn'] = num 

    def host_state(self, data):
        self.mon_cpu()
        self.mon_disk()
        self.mon_load()
        self.mon_mem()
        self.mon_process()
        self.mon_conn()
        return host_state

    def run(self):
         tasks = [self.mon_cpu, self.mon_disk, self.mon_load, self.mon_mem, self.mon_process]
         for task in tasks:
             schedule.every(60).seconds.do(task)
         while True:
             schedule.run_pending()
             time.sleep(20)

    def send_msg(self,message):
        
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        try:
            req = requests.post(gmdcon.web_hook, data=json.dumps(message), headers=headers)
            gmdlog.writelog(f"发送到钉钉接口的返回结果: {req.text}")
        except requests.exceptions.HTTPError as e:
            gmdlog.writelog(f"发送消息失败: {e.response.reason}")
        except requests.exceptions.ConnectionError:
            gmdlog.writelog("HTTP Connection failed")

gmdmon = GmMon()
__all__ = [ gmdmon ]