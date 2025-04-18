#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <pthread.h>

#define PORT 8080
#define BUFFER_SIZE 1024

typedef struct {
    int client_socket;
    pthread_mutex_t *lock;
    pthread_cond_t *cond;
    char buffer[BUFFER_SIZE];
    int is_message_ready;
} ClientData;

void *handle_client(void *arg) {
    ClientData *data = (ClientData *)arg;
    char *response = "Hello from server!";
    int n;

    // 读取客户端发送的数据
    pthread_mutex_lock(data->lock);
    while (!data->is_message_ready) {
        pthread_cond_wait(data->cond, data->lock);
    }
    n = recv(data->client_socket, data->buffer, BUFFER_SIZE, 0);
    data->is_message_ready = 0;
    pthread_mutex_unlock(data->lock);

    if (n > 0) {
        // 处理接收到的消息
        printf("Received message from client: %s\n", data->buffer);

        // 处理完毕后向客户端发送响应消息
        send(data->client_socket, response, strlen(response), 0);
        printf("Response sent to the client\n");
    } else if (n == 0) {
        // 客户端关闭了连接
        printf("Client disconnected\n");
    } else {
        // 接收错误
        perror("recv failed");
    }

    close(data->client_socket);
    pthread_cond_signal(data->cond);
    pthread_exit(NULL);
}

int main() {
    int server_fd, *new_sock;
    struct sockaddr_in address;
    int addrlen = sizeof(address);
    pthread_t tid;
    pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
    pthread_cond_t cond = PTHREAD_COND_INITIALIZER;
    int is_message_ready = 0;
    char buffer[BUFFER_SIZE] = {0};

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

    while (1) {
        int *new_sock = malloc(sizeof(int));

        // 接受客户端连接并创建新线程处理请求
        if ((*new_sock = accept(server_fd, (struct sockaddr *)&address, (socklen_t *)&addrlen)) < 0) {
            perror("accept failed");
            exit(EXIT_FAILURE);
        }

        ClientData *data = malloc(sizeof(ClientData));
        data->client_socket = *new_sock;
        data->lock = &lock;
        data->cond = &cond;
        data->is_message_ready = is_message_ready;
        memcpy(data->buffer, buffer, BUFFER_SIZE);

        pthread_mutex_lock(&lock);
        pthread_cond_signal(&cond);

        if (pthread_create(&tid, NULL, handle_client, (void *)data) < 0) {
            perror("pthread_create failed");
            exit(EXIT_FAILURE);
        }

        pthread_mutex_unlock(&lock);
    }

    close(server_fd);

    return 0;
}