#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <syslog.h>
#include <signal.h>

int daemonize()
{
    pid_t pid;
    // fork off the parent process
    pid = fork();
    if (pid < 0) {
        exit(EXIT_FAILURE);
    }
    if (pid > 0) {
        exit(EXIT_SUCCESS);
    }

    // create new session
    if (setsid() < 0) {
        exit(EXIT_FAILURE);
    }

    pid = fork();
    if (pid < 0) {
        exit(EXIT_FAILURE);
    }
    if (pid > 0) {
        exit(EXIT_SUCCESS);
    }

    if (chdir("/") < 0) {
        exit(EXIT_FAILURE);
    }

    umask(0);

    for (int x=sysconf(_SC_OPEN_MAX); x>=0; x--) {
        close(x);
    }

    open("/dev/null", O_RDWR);
    dup(0);
    dup(0);

    openlog("daemonized_process", LOG_PID, LOG_DAEMON);
    syslog(LOG_NOTICE, "daemon started.");
    closelog();
}

int main()
{
    daemonize();

    while (1) {
        sleep(30);
    }

    return EXIT_SUCCESS;
}
