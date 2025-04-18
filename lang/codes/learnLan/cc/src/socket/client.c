// 
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
    int fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);

    if(0>fd)
    {
        perror("create error!");
        exit(EXIT_FAILURE);
    }

    int ret;
    struct sockaddr_in stSockAddr;
    memset(&stSockAddr, 0, sizeof(struct sockaddr_in));
    stSockAddr.sin_family = AF_INET;
    stSockAddr.sin_port = 2021;
    ret = inet_pton(AF_INET, "0.0.0.0", &stSockAddr.sin_addr);
    if(0>ret)
    {
        perror("#aaaaaaaaaaaaaaa#");
        close(fd);
        exit(EXIT_FAILURE);
    }
    if(0==ret)
    {
        perror("#bbbbbbbbbbbbbbb#");
        close(fd);
        exit(EXIT_FAILURE);
    }

    if(0>connect(fd, (const struct sockaddr *)&stSockAddr, sizeof(struct sockaddr_in)))
    {
        perror("connect error!");
        close(fd);
        exit(EXIT_FAILURE);
    }

    shutdown(fd, SHUT_RDWR);
    close(fd);
    return 0;
}