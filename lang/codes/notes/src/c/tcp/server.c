#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 12345
#define BUFFER_SIZE 1024

void receive_message(int sockfd)
{
    int message_len;
    char buffer[BUFFER_SIZE];

    recv(sockfd, &message_len, sizeof(int), 0); // 接收消息长度前缀
    recv(sockfd, buffer, message_len, 0);       // 接收消息内容

    buffer[message_len] = '\0';
    printf("Received message: %s\n", buffer);
}

int main()
{
    int sockfd, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1)
    {
        perror("Socket creation error");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1)
    {
        perror("Binding error");
        exit(EXIT_FAILURE);
    }

    if (listen(sockfd, 5) == -1)
    {
        perror("Listening error");
        exit(EXIT_FAILURE);
    }

    client_socket = accept(sockfd, (struct sockaddr *)&client_addr, &client_len);
    if (client_socket == -1)
    {
        perror("Accepting error");
        exit(EXIT_FAILURE);
    }

    // 接收消息
    receive_message(client_socket);
    receive_message(client_socket);
    receive_message(client_socket);

    close(client_socket);
    close(sockfd);

    return 0;
}