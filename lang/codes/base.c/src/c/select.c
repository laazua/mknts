#include <stdio.h>
#include <errno.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/select.h>

// 最大客户端连接数
#define MAX_CLIENTS 3

int main()
{
    int server_socket, client_socket[MAX_CLIENTS], max_clients = 10;
    struct sockaddr_in server_addr, client_addr;
    fd_set readfds;
    int max_sd, activity, sd, i;
    char buffer[1024] = {0};
    
    if ((server_socket=socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("init socket failure!");
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

    // 初始化客户端套接字列表
    for (i = 0; i < MAX_CLIENTS; i++) {
        client_socket[i] = 0;
    }

    while (1) {
        FD_ZERO(&readfds);
        FD_SET(server_socket, &readfds);
        max_sd = server_socket;

        for (i = 0; i < max_clients; i++) {
            sd = client_socket[i];
            if (sd > 0) {
                FD_SET(sd, &readfds);
            }
            if (sd > max_sd) {
                max_sd = sd;
            }
        }

        activity = select(max_sd + 1, &readfds, NULL, NULL, NULL);

        if ((activity < 0) && (errno != EINTR)) {
            perror("Select error");
        }
        
        if (FD_ISSET(server_socket, &readfds)) {
            int new_socket;
            int addrlen = sizeof(client_addr);
            if ((new_socket = accept(server_socket, (struct sockaddr *)&client_addr, (socklen_t *)&addrlen)) < 0) {
                perror("Accept error");
                exit(EXIT_FAILURE);
            }

            printf("New connection from %s:%d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

            for (i = 0; i < max_clients; i++) {
                if (client_socket[i] == 0) {
                    client_socket[i] = new_socket;
                    break;
                }
            }
            if (i == max_clients) {
                printf("Too many clients\n");
            }
            max_clients++;
        }

        for (i = 0; i < max_clients; i++) {
            sd = client_socket[i];
            if (FD_ISSET(sd, &readfds)) {
                if (read(sd, buffer, 1024) == 0) {
                    printf("Connection closed\n");
                    close(sd);
                    client_socket[i] = 0;
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
