import os
import sys
import time
import atexit
from signal import SIGTERM


class Daemon:
    def __init__(
        self, 
        pidfile,
        stdin="/dev/null", 
        stdout="/dev/null", 
        stderr="/dev/null"
    ):
        self._stdin = stdin
        self._stdout = stdout
        self._stderr = stderr
        self._pidfile = pidfile

    def daemonize(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write(f"First Fork Error: {e.errno} ({e.strerror})\n")
            sys.exit(1)

        os.chdir("/")
        os.setsid()
        os.umask(0)
        
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write(f"Fork Second Error: {e.errno} ({e.strerror})") 
            sys.exit(1)
        
        sys.stdout.flush()
        sys.stdout.flush()
        with open(self._stdin, "r") as si:
            os.dup2(si.fileno(), sys.stdin.fileno())
        with open(self._stdout, "a+") as so:
            os.dup2(so.fileno(), sys.stdout.fileno())
        if self._stderr:
            try:
                with open(self._stderr, "a+", 0) as se:
                    os.dup2(se.fileno(), sys.stderr.fileno())
            except ValueError:
                with open(self._stderr, "a+", 1) as se:
                    os.dup2(se.fileno(), sys.stderr.fileno())
        else:
            se = so

        atexit.register(self._delpid)
        pid = str(os.getpid())
        with open(self._pidfile, "w+") as fd:
            fd.write(f"{pid}")
        
    def _delpid(self):
        os.remove(self._pidfile)

    def start(self):
        # 检测程序是否启动
        try:
            with open(self._pidfile, "r") as fd:
                pid = int(fd.read().strip())
        except IOError:
            pid = None

        if pid:
            message = f"Pidfile {self._pidfile} already exist, Daemon already running?\n"
            sys.stderr.write(message)
            sys.exit(1)
        self.daemonize()
        self.run()
    
    def stop(self):
        try:
            with open(self._pidfile, "r") as fd:
                pid = int(fd.read().strip())
        except IOError:
            pid = None
        if not pid:
            message = f"Pidfile {self._pidfile} do not exist, Daemon not running?\n"
            sys.stderr.write(message)
            return
        try:
            while True:
                os.kill(pid, SIGTERM)
                time.sleep(0.5)
        except OSError as e:
            if str(e).find("No such process") > 0:
                if os.path.exists(self._pidfile):
                    self._delpid()
                else:
                    print(str(e))
                    sys.exit(1)
    
    def restart(self):
        self.stop()
        self.start()
    
    def run(self):
        pass