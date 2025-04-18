#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 12345
#define BUFFER_SIZE 1024

void send_message(int sockfd, const char *message)
{
    int message_len = strlen(message);
    send(sockfd, &message_len, sizeof(int), 0); // 发送消息长度前缀
    send(sockfd, message, message_len, 0);      // 发送消息内容
}

int main()
{
    int sockfd;
    struct sockaddr_in server_addr;

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1)
    {
        perror("Socket creation error");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1)
    {
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }

    // 发生消息
    send_message(sockfd, "Hello,");
    send_message(sockfd, "world!");
    send_message(sockfd, "xxxxxxxxxxxxxxx test ^_^ xxxxxxxxxxxxxxxxxxx");
    close(sockfd);

    return 0;
}