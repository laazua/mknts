# -*- conding:utf-8 -*-

"""
create daemon process
"""

import time
import os, sys
import atexit, signal


def do_work():
    time.sleep(3600)
          

def create_daemon(pidfile, *, stdin="/dev/null", stdout="/dev/null", stderr="/dev/null"):
    
    if os.path.exists(pidfile):
        raise RuntimeError("Already running")

    # first fork(detaches from parent)
    try:
        if os.fork() > 0:
            raise SystemExit(0)    # Parent exit
    except OSError as e:
        raise RuntimeError("fork #1 failed.")

    os.chdir('/')
    os.umask(0)
    os.setsid()

    # second fork (relinquish session leadership)
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError("fork #2 failed.")

    # flush I/O buffers
    sys.stdout.flush()
    sys.stderr.flush()

    # replace file descriptors for stdin, stdout, stderr
    with open(stdin, 'rb', 0) as fd:
        os.dup2(fd.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', 0) as fd:
        os.dup2(fd.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', 0) as fd:
        os.dup2(fd.fileno(), sys.stderr.fileno()) 

    # write the pid file
    with open(pidfile, 'w') as fd:
        print(os.getpid(), file=fd)

    # arrange to have the pid file removed on exit/signal
    atexit.register(lambda: os.remove(pidfile))

    #signal handler for termination (required)
    def sigterm_handler(signo, frame):
        raise SystemExit(1)

    signal.signal(signal.SIGTERM, sigterm_handler)
    
    # do some work
    do_work()


def start(pidfile):
    try:
        create_daemon(pidfile, stdout="/tmp/daemon.log", stderr="/tmp/daemon.log")
    except RuntimeError as e:
        print(e, file=sys.stderr)
        raise SystemExit(1)


def stop(pidfile):
    if os.path.exists(pidfile):
        with open(pidfile) as fd:
            os.kill(int(fd.read()), signal.SIGTERM)
    else:
        print("Not running", file=sys.stderr)
        raise SystemExit(1)


def main():
    PIDFILE = "/tmp/daemon.pid"

    if len(sys.argv) != 3:
        print("Usage: python3 {} -s [start|stop]".format(sys.argv[0]), file=sys.stderr)
        raise SystemExit(1)
    elif sys.argv[2] == "start":
        start(PIDFILE)
    elif sys.argv[2] == "stop":
        stop(PIDFILE)
    else:
        print("Unknow command {!r}".format(sys.argv[2]), file=sys.stderr)


if __name__ == "__main__":
    main()
