#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 8888
#define BUF_SIZE 1024

int main() 
{
    int sockfd, newsockfd, clilen;
    char buffer[BUF_SIZE];
    struct sockaddr_in serv_addr, cli_addr;
    int n;

    // 创建套接字
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("Error opening socket");
        exit(1);
    }

    // 设置服务器地址结构
    memset((char *) &serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(PORT);

    // 绑定套接字
    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) {
        perror("Error on binding");
        exit(1);
    }

    // 监听连接
    listen(sockfd, 5);
    clilen = sizeof(cli_addr);

    // 接受连接
    newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
    if (newsockfd < 0) {
        perror("Error on accept");
        exit(1);
    }

    // 读取客户端消息并回显
    while (1) {
        memset(buffer, 0, BUF_SIZE);
        n = read(newsockfd, buffer, BUF_SIZE);
        if (n < 0) {
            perror("Error reading from socket");
            exit(1);
        }
        printf("Client: %s\n", buffer);

        n = write(newsockfd, buffer, strlen(buffer));
        if (n < 0) {
            perror("Error writing to socket");
            exit(1);
        }
    }

    close(newsockfd);
    close(sockfd);

    return 0;
}

// nc localhost 8888
