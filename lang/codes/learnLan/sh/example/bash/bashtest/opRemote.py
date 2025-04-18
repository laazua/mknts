#!/usr/bin/python
#_*_ coding: utf-8 _*_
# Author: Sseve
"""
Welcome to use opRemote.py V1.0 copyright by Sseve.
When you want to use this script. First,you must config sshd 
without passwd to login between master host and server host. 
Then you can use this script.
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import argparse
import paramiko

#Global variable
USER = 'bobo'
PASSWD = '123456'
PORT = '22'

class Sshremotehost(object):
    def __init__(self, host, user, passwd, cmd, port):
	self.host = host
	self.user = user
	self.passwd = passwd
	self.cmd = cmd
 	self.port = port

    def do_cmd(self):
	try:
            client = paramiko.SSHClient()
	    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	    client.connect(hostname=self.host, username=self.user, password=self.passwd, port=self.port, timeout=10)
	except:
            print "\033[1;31m[-]\033[0m Create ssh connection of %s faild!!" % self.host
	
        print "\033[1;32m[+]\033[0m Login %s execute command --> %s" % (self.host, self.cmd)
        cmd = self.cmd
	stdin, stdout, stderr = client.exec_command(cmd)
	res = stdout.read().decode('utf-8')
   	print res

	client.close()

    def do_put(self):
        try:
	    transport = paramiko.Transport((self.host, self.port))
	    transport.connect(username=self.user, password=self.passwd)
	except:
	    print "\033[1;31m[-]\033[0m Create channel of %s faild!!" % self.host

        try:
     	    putf = paramiko.SFTPClient.from_transport(transport)
        except:
            print "\033[1;31m[-]\033[0m Create SFTPClient object %s faild!" % self.host

        lfile = self.cmd[0]
        rfile = self.cmd[1]

        print "\033[1;32m[+]\033[0m Upload file: %s -->> %s path: %s" % (lfile, self.host, rfile)
        try:
	    putf.put(lfile, rfile) 
        except:
	    print "\033[1;31m[-]\033[0m Upload file from %s failed!" % self.host

	putf.close()
	transport.close()	

    def do_get(self):
	try:
	    transport = paramiko.Transport(self.host, self.port)
	    transport.connect(username=self.user, password=self.passwd)
	except:
	    print "\033[1;31m[-]\033[0m Create channel of %s failed!" % self.host

	try:
	    getf = paramiko.SFTPClient.from_transport(transport)
	except:
	    print "\033[1;31m[-]\033[0m Create SFTPClient object of %s failed!" % self.host
           
  	lfile = self.cmd[1]
        rfile = self.cmd[0]
        
	try:
 	    print "\033[1;32m[+]\033[0m Get file: %s from %s path: %s" % (rfile, self.host, lfile)
	    getf.get(rfile, lfile)
	except:
	    print "\033[1;32m[-]\033[0m Download file from %s failed" % self.host
        
	getf.close()
        transport.close()


def print_help():
    print """
    Version: python 2.7
    Message: this py script used to operate remote host like this:
    Usage:
	python opRemote.py -c ["df -h"|"pwd;echo 'echo 123' > b.sh; sudo cp b.sh /root"]   -- execute command on remote host
	python opRemote.py -l '/ltest/test.txt' -r '/rtest/test.txt'  -- upload file to remote host
	python opRemote.py -l '/ltest/test.txt' -r '/rtest/test.txt' -i 127.0.0.1  --download file from remote host
    """
    sys.exit()
    

def argv_parameter():
    parser = argparse.ArgumentParser(description="run: python opRemote.py to learn more. And first config ssh without passwd between hosts. Then you can use this script.")
    parser.add_argument("-c", "--command", help="the command you want to run.")
    parser.add_argument("-l", "--localfile", help="the file you want to upload to remote host which on localhost.")
    parser.add_argument("-r", "--remotefile", help="the file you wan to save the localfilefile on remotehost. ")
    parser.add_argument("-i", "--ip", help="the host you want to get file from")
    args = parser.parse_args()
   
    return args

def main():
    user = USER
    passwd = PASSWD
    port = PORT
    #iplist = ['192.168.5.130', '127.0.0.1']
    iplist = []
    try:
        fo = open('ip.txt', 'r') 
        for line in fo.readlines():
            iplist.append(line.strip('\n'))
    except:
	print "Can not open ip.txt, please touch it and write ip in which you want to option."  
	sys.exit()  
    fo.close()
    
    argv = argv_parameter()
    argslist = []

    if argv.command == None and argv.ip == None and argv.localfile != None and argv.remotefile != None:
        argslist.append(argv.localfile)
        argslist.append(argv.remotefile)
        for i in iplist:
    	    p = Sshremotehost(i, user, passwd, argslist, int(port))
    	    p.do_put()
    elif argv.command != None and argv.ip == None and argv.localfile == None and argv.remotefile == None:
        command = argv.command
    	for i in iplist:
    	    p = Sshremotehost(i, user, passwd, command, int(port))
    	    p.do_cmd()
    elif argv.command == None and argv.ip != None and argv.localfile != None and argv.remotefile != None:
        argslist.append(argv.remotefile)
        argslist.append(argv.localfile)
	p = Sshremotehost(argv.ip, user, passwd, argslist, int(port))
        p.do_get()
    elif argv.command == None and argv.ip == None and argv.remotefile == None and argv.localfile == None:
	print_help()


if __name__ == '__main__':
    main()
