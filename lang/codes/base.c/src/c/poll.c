#include <stdio.h>
#include <errno.h>
#include <poll.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

// 最大客户端连接数
#define MAX_CLIENTS 3

int main() {
    int server_socket, client_socket[MAX_CLIENTS], max_clients = 0;
    struct sockaddr_in server_addr, client_addr;
    struct pollfd fds[MAX_CLIENTS + 1]; // +1 for server socket
    int i, activity;
    char buffer[1024] = {0};

    // 创建 TCP 套接字并监听端口
    if ((server_socket = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(8888);

    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        exit(EXIT_FAILURE);
    }

    if (listen(server_socket, 5) < 0) {
        perror("Listen failed");
        exit(EXIT_FAILURE);
    }

    memset(client_socket, 0, sizeof(client_socket));

    fds[0].fd = server_socket;
    fds[0].events = POLLIN;

    for (i = 1; i <= MAX_CLIENTS; i++) {
        fds[i].fd = -1;
    }

    while (1) {
        activity = poll(fds, max_clients + 1, -1);

        if ((activity < 0) && (errno != EINTR)) {
            perror("Poll error");
        }

        if (fds[0].revents & POLLIN) {
            int new_socket;
            int addrlen = sizeof(client_addr);
            if ((new_socket = accept(server_socket, (struct sockaddr *)&client_addr, (socklen_t *)&addrlen)) < 0) {
                perror("Accept error");
                exit(EXIT_FAILURE);
            }

            printf("New connection from %s:%d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

            for (i = 1; i <= MAX_CLIENTS; i++) {
                if (fds[i].fd == -1) {
                    fds[i].fd = new_socket;
                    fds[i].events = POLLIN;
                    break;
                }
            }
            if (i == MAX_CLIENTS + 1) {
                printf("Too many clients\n");
            }
            max_clients++;
        }

        for (i = 1; i <= max_clients; i++) {
            if (fds[i].revents & POLLIN) {
                int sd = fds[i].fd;
                if (read(sd, buffer, 1024) == 0) {
                    printf("Connection closed\n");
                    close(sd);
                    fds[i].fd = -1;
                } else {
                    printf("Received: %s\n", buffer);
                    send(sd, buffer, strlen(buffer), 0);
                    memset(buffer, 0, sizeof(buffer));
                }
            }
        }
    }

    return 0;
}
