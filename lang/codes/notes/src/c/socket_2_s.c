#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 8080
#define BUFFER_SIZE 1024

void handle_client(int client_socket) {
    char buffer[BUFFER_SIZE] = {0};
    char *response = "Hello from server!";
    int n;

    while ((n = recv(client_socket, buffer, BUFFER_SIZE, 0)) > 0) {
        // 处理接收到的消息
        printf("Received message from client: %s\n", buffer);

        // 处理完毕后向客户端发送响应消息
        send(client_socket, response, strlen(response), 0);

        // 清空缓冲区
        memset(buffer, 0, sizeof(buffer));
    }

    if (n == 0) {
        // 客户端关闭了连接
        printf("Client disconnected\n");
    } else {
        // 接收错误
        perror("recv failed");
    }

    close(client_socket);
}

int main() {
    int server_fd, client_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);

    // 创建套接字
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);

    // 绑定套接字到指定的IP地址和端口
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    // 监听套接字
    if (listen(server_fd, 3) < 0) {
        perror("listen failed");
        exit(EXIT_FAILURE);
    }

    printf("Server listening on port %d\n", PORT);

    while(1) {
        // 接受客户端连接并处理请求
        if ((client_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0) {
            perror("accept failed");
            exit(EXIT_FAILURE);
        }
        
        // 在新的线程中处理客户端请求
        // 在实际应用中可以考虑使用线程池或者异步处理方式
        handle_client(client_socket);
    }

    close(server_fd);

    return 0;
}