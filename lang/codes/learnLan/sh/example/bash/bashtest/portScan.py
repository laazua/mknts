#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import nmap


input_port = raw_input('please input port: ')
if not input_port:
    print 'Input error, example: 22,25'
    sys.exit(0)

try:
    fd = open('ip.txt')
except:
    print "打开ip文件失败"
    sys.exit()

ips = fd.read().strip('\n')

try:
    nmp = nmap.PortScanner()
except nmap.PortScannerError:
    print 'nmap not found', sys.exc_info()[0]
    sys.exit(0)
except:
    print "Unexpected error:", sys.exc_info()[0]
    sys.exit(0)

try:
    nmp.scan(hosts=ips, arguments=' -v -sS -p ' + input_port)
except Exception, e:
    print "scan error:", str(e)


for host in nmp.all_hosts():
    print "======================================"
    print 'Host : %s (%s)' % (host, nmp[host].hostname())
    print 'State : %s' % nmp[host].state()    #输出状态,如up、down
