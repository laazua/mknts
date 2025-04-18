#/usr/bin/env python2
#coding:utf-8
import os, sys, getopt, signal, Queue, threading
from .monitorlibs import getconfig, disk, cpu

MONITTORJOBQ = Queue.Queue()
QMAX = 10


class MonitorThread(threading.Thread):
    def __init__(self, monitorinput):
        threading.Thread.__init__(self)
        self._monitorjobq = monitorinput

    def run(self):
        while True:
            if self._monitorjobq.qsize() > 0:
                try:
                    monitorjob = self._monitorjobq.get()
                    monitorjob.Run()
                except Queue.empty:
                    queue_size = 0
            else:
                break


def print_help():
    print "-h   print help message."
    print "-s   start|stop this process."
    os._exit(0)


def start_opt():
    if os.path.exists("/var/run/monitor.pid"):
        with open("/var/run/monitor.pid") as fd:
            pid = fd.read()
        if pid.strip() == "":
            create_daemon()
        else:
            print "进程未关闭."
    else:
        create_daemon()


def stop_opt():
    with open("/var/run/monitor.pid") as fd:
        pid = fd.read()
        os.kill(int(pid.strip()), signal.SIGKILL)
    with open("/var/run/monitor.pid", "w") as fd:
        fd.write("")
     

def create_daemon():
    try:
        if os.fork > 0:
            os._exit(0)
    except OSError as error:
        os._exit(1)

    os.chdir("/root/monitor")
    os.setsid()
    
    try:
        pid = os.fork()
        if pid > 0:
            with open("/var/run/monitor/monitor.pid", "w") as fd:
                fd.write(str(pid))
            os._exit(0)
    except OSError as error:
        os._exit(1)
    
    add_moniter_module()


def add_moniter_module():
    while_list = getconfig.getkey("global", "whilelist")
    if "disk" not in while_list:
        MONITTORJOBQ.put(disk)
    if "cpu" not in while_list:
        MONITTORJOBQ.put(cpu)
    #if ...

    for i in range(QMAX):
        MonitorThread(MONITTORJOBQ).start()

    
def main():
    opt, args = getopt.getopt(sys.argv[1:], "s:h")
    for op, value in opt:
        if op == '-h':
            print_help()
    
        elif op == '-s':
            if value == 'start':
                start_opt()
            elif value == 'stop':
                stop_opt()


if __name__ == '__main__':
    main()