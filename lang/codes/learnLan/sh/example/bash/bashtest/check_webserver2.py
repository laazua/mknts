#!/usr/bin/python
#coding:utf-8
#基于httplib库的web服务检测
import httplib,sys
from optparse import OptionParser


def check_webserver(address, port, resource):
	#Create connection
	if not resource.startswith('/'):
		resource = '/' + resource

	try:
		conn = httplib.HTTPConnection(address, port)
		print "HTTP connection created successfully"
		#make request
		req = conn.request('GET', resource)
		print 'request for %s successful' % resource
		#get response
		rep = conn.getresponse()
		print "响应状态: %s" % rep.status
	except sock.error, e:
		print "HTTP connection failed: %s" % e
	finally:
		conn.close()
		print 'HTTP connection clised successfully'

	if rep.status in [200, 301]:
		return True
	else:
		return False


def main():
    parser = OptionParser()
    parser.add_option("-a", "--address", dest="address", default="localhost", help="ADDRESS for webserver", metavar="DDRESS")
    parser.add_option("-p", "--port", dest="port", type="int", default=80, help="PORT for webserver", metavar="PORT")
    parser.add_option("-r", "--resource", dest="resource", default="index.html", help="RESOURCE to check", metavar="RESOURCE")

    options, args = parser.parse_args()
    print "options: %s, args: %s" % (options, args)
    check = check_webserver(options.address, options.port, options.resource)
    print "check_webserver returned %s" % check
    sys.exit(not check)


if __name__ == '__main__':
	main()
