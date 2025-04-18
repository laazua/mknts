// select.c
// poll.c
// epoll.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    char message[1024] = {0};

    // 创建 TCP 套接字
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("Socket creation error");
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(8888);

    // 将 IPv4 地址从文本转换为二进制形式
    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        perror("Invalid address/ Address not supported");
        return -1;
    }

    // 连接到服务器
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("Connection failed");
        return -1;
    }

    while (1) {
        printf("Enter message: ");
        fgets(message, 1024, stdin);

        // 发送消息给服务器
        send(sock, message, strlen(message), 0);

        // 从服务器接收响应
        memset(message, 0, sizeof(message));
        recv(sock, message, 1024, 0);
        printf("Server response: %s\n", message);
    }

    close(sock);
    return 0;
}
