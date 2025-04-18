#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <pthread.h>

#define BUF_SIZE 1024
#define TRUE 1
#define FALSE 0

void *handle_client(void *arg);
void error_handling(char *message);

struct ThreadArgs {
    int clnt_sock;
    char *dest_ip;
    int dest_port;
};

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Usage: %s <port> <dest_ip> <dest_port>\n", argv[0]);
        exit(1);
    }

    int serv_sock;
    struct sockaddr_in serv_addr;

    serv_sock = socket(PF_INET, SOCK_STREAM, 0);
    if (serv_sock == -1)
        error_handling("socket() error");

    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = htonl(INADDR_ANY);
    serv_addr.sin_port = htons(atoi(argv[1]));

    if (bind(serv_sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) == -1)
        error_handling("bind() error");

    if (listen(serv_sock, 5) == -1)
        error_handling("listen() error");

    while (TRUE) {
        struct sockaddr_in clnt_addr;
        socklen_t clnt_addr_size = sizeof(clnt_addr);
        int clnt_sock = accept(serv_sock, (struct sockaddr *)&clnt_addr, &clnt_addr_size);
        if (clnt_sock == -1)
            error_handling("accept() error");

        struct ThreadArgs *thread_args = malloc(sizeof(struct ThreadArgs));
        thread_args->clnt_sock = clnt_sock;
        thread_args->dest_ip = argv[2];
        thread_args->dest_port = atoi(argv[3]);

        pthread_t tid;
        pthread_create(&tid, NULL, handle_client, (void *)thread_args);
        pthread_detach(tid);
    }

    close(serv_sock);
    return 0;
}

void *handle_client(void *arg) {
    struct ThreadArgs *thread_args = (struct ThreadArgs *)arg;
    int clnt_sock = thread_args->clnt_sock;
    char *dest_ip = thread_args->dest_ip;
    int dest_port = thread_args->dest_port;
    free(arg);

    char message[BUF_SIZE];
    int str_len;

    // 连接到目标服务器
    int dest_sock = socket(PF_INET, SOCK_STREAM, 0);
    if (dest_sock == -1)
        error_handling("socket() error");

    struct sockaddr_in dest_addr;
    memset(&dest_addr, 0, sizeof(dest_addr));
    dest_addr.sin_family = AF_INET;
    dest_addr.sin_addr.s_addr = inet_addr(dest_ip);
    dest_addr.sin_port = htons(dest_port);

    if (connect(dest_sock, (struct sockaddr *)&dest_addr, sizeof(dest_addr)) == -1)
        error_handling("connect() error");

    while ((str_len = recv(clnt_sock, message, BUF_SIZE, 0)) > 0) {
        printf("Received from client: %s\n", message);

        // 将数据转发到目标服务器
        int sent_len = 0;
        while (sent_len < str_len) {
            int ret = send(dest_sock, message + sent_len, str_len - sent_len, 0);
            if (ret == -1)
                error_handling("send() error");
            sent_len += ret;
        }

        // 从目标服务器接收响应并转发给客户端
        int recv_len = 0;
        while ((recv_len = recv(dest_sock, message, BUF_SIZE, 0)) > 0) {
            sent_len = 0;
            while (sent_len < recv_len) {
                int ret = send(clnt_sock, message + sent_len, recv_len - sent_len, 0);
                if (ret == -1)
                    error_handling("send() error");
                sent_len += ret;
            }
        }
    }

    close(dest_sock);
    close(clnt_sock);
    return NULL;
}

void error_handling(char *message) {
    fputs(message, stderr);
    fputc('\n', stderr);
    exit(1);
}

