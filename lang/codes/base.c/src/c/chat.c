#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <pthread.h>

#define PORT 8888
#define MAX_CLIENTS 30
#define BUFFER_SIZE 1024

int client_sockets[MAX_CLIENTS] = {0}; // 声明客户端套接字数组

// 结构体用于传递参数给线程
typedef struct {
    int socket;
    struct sockaddr_in addr;
} client_data;

// 处理客户端的函数
void *handle_client(void *arg) {
    client_data *client = (client_data *)arg;
    char buffer[BUFFER_SIZE];
    int bytes_received;

    while (1) {
        bytes_received = recv(client->socket, buffer, BUFFER_SIZE, 0);
        if (bytes_received <= 0) {
            printf("Client %s:%d disconnected\n", inet_ntoa(client->addr.sin_addr), ntohs(client->addr.sin_port));
            close(client->socket);
            pthread_exit(NULL);
        }

        buffer[bytes_received] = '\0';
        printf("Received message from %s:%d: %s\n", inet_ntoa(client->addr.sin_addr), ntohs(client->addr.sin_port), buffer);

        // 广播消息给所有客户端
        for (int i = 0; i < MAX_CLIENTS; ++i) {
            if (client_sockets[i] != 0 && client_sockets[i] != client->socket) {
                send(client_sockets[i], buffer, strlen(buffer), 0);
            }
        }
    }
}

int main() {
    int server_socket, client_count = 0;
    struct sockaddr_in server_addr, client_addr;
    pthread_t client_threads[MAX_CLIENTS];
    char buffer[BUFFER_SIZE];

    // 创建服务器套接字
    if ((server_socket = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
        perror("Error creating server socket");
        exit(EXIT_FAILURE);
    }

    // 设置服务器地址结构
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    // 将套接字绑定到地址和端口
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    // 监听传入的连接
    if (listen(server_socket, MAX_CLIENTS) == -1) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }

    printf("Server listening on port %d\n", PORT);

    // 接受连接并创建线程处理每个客户端
    while (1) {
        socklen_t client_addr_size = sizeof(client_addr);
        int client_socket;

        // 接受新连接
        if ((client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &client_addr_size)) == -1) {
            perror("Accept failed");
            continue;
        }

        printf("New connection from %s:%d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

        // 添加新客户端到客户端数组
        for (int i = 0; i < MAX_CLIENTS; ++i) {
            if (client_sockets[i] == 0) {
                client_sockets[i] = client_socket;
                client_count++;
                break;
            }
        }

        // 创建新线程处理客户端
        client_data *data = (client_data *)malloc(sizeof(client_data));
        data->socket = client_socket;
        data->addr = client_addr;
        pthread_create(&client_threads[client_count - 1], NULL, handle_client, (void *)data);
    }

    // 关闭服务器套接字
    close(server_socket);

    return 0;
}


// client: nc 127.0.0.1 8888
