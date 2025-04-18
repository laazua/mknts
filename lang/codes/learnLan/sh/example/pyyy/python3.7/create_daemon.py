#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time

def create_daemon():
    try:
        if os.fork() > 0:
            os._exit(0)
    except OSError as e:
        print(e)
    os.chdir("/home/wnot")
    os.setsid()
    try:
        pid = os.fork()
        if pid > 0:
            with open("/home/wnot/test.pid", "w") as fd:
                fd.write(str(pid))
            os._exit(0)
    except OSError as error:
        print(error)
        os._exit(0)

if __name__ == '__main__':
    create_daemon()
    while True:
        time.sleep(10)
        os.system('echo aa >> teeet.txt')
