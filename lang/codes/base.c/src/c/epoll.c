#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/epoll.h>

// 最大客户端连接数
#define MAX_EVENTS 3
#define MAX_CLIENTS 3

int main() {
    int server_socket, client_socket[MAX_CLIENTS], max_clients = 0;
    struct sockaddr_in server_addr, client_addr;
    struct epoll_event ev, events[MAX_EVENTS];
    int epoll_fd, nfds, i;
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

    epoll_fd = epoll_create1(0);
    if (epoll_fd == -1) {
        perror("Epoll creation failed");
        exit(EXIT_FAILURE);
    }

    ev.events = EPOLLIN;
    ev.data.fd = server_socket;
    if (epoll_ctl(epoll_fd, EPOLL_CTL_ADD, server_socket, &ev) == -1) {
        perror("Epoll control failed");
        exit(EXIT_FAILURE);
    }

    while (1) {
        nfds = epoll_wait(epoll_fd, events, MAX_EVENTS, -1);
        if (nfds == -1) {
            perror("Epoll wait failed");
            exit(EXIT_FAILURE);
        }

        for (i = 0; i < nfds; i++) {
            if (events[i].data.fd == server_socket) {
                int new_socket;
                int addrlen = sizeof(client_addr);
                if ((new_socket = accept(server_socket, (struct sockaddr *)&client_addr, (socklen_t *)&addrlen)) < 0) {
                    perror("Accept error");
                    exit(EXIT_FAILURE);
                }

                printf("New connection from %s:%d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

                ev.events = EPOLLIN;
                ev.data.fd = new_socket;
                if (epoll_ctl(epoll_fd, EPOLL_CTL_ADD, new_socket, &ev) == -1) {
                    perror("Epoll control failed");
                    exit(EXIT_FAILURE);
                }
            } else {
                int sd = events[i].data.fd;
                if (read(sd, buffer, 1024) == 0) {
                    printf("Connection closed\n");
                    close(sd);
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
