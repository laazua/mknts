// c TCP socket server 
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


int main(void)
{
    // socket句柄
    int fd;
    int rfd;
    char buffer[1024] = {0};
    
    fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if(fd<0)
    {
        perror("create socket fd error!\n");
        exit(EXIT_FAILURE); 
    }

    // ipv4 AF_INET sockets
    struct sockaddr_in stSockAddr;
    memset(&stSockAddr, 0, sizeof(struct sockaddr_in));

    stSockAddr.sin_family = AF_INET;
    stSockAddr.sin_port = htons(2021);
    stSockAddr.sin_addr.s_addr = INADDR_ANY;

    if(0>bind(fd, (const struct sockaddr *)&stSockAddr, sizeof(struct sockaddr_in)))
    {
        perror("bin error");
        close(fd);
        exit(EXIT_FAILURE);
    }
    if(0>listen(fd, 5))
    {
        perror("listen error!");
        exit(EXIT_FAILURE);
    }
    while(1)
    {
        int cfd = accept(fd, NULL, NULL);
        if(0>fd)
        {
            perror("accept error!");
            close(fd);
            exit(EXIT_FAILURE);
        }

        shutdown(fd, SHUT_RDWR);
        close(cfd);
    }

    close(fd);
    return 0;
}