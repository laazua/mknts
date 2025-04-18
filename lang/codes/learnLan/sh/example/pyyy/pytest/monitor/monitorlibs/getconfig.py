#coding:utf-8
import configparser, traceback, writelog
from configparser import ConfigParser

def getkey(section, field):
    config = ConfigParser.ConfigParser()
    try:
        config.read("/root/monitor/config/config.txt")
        value = config.get(section, field)
    except:
        errorlog = traceback.format_exc()
        writelog.write(errorlog)