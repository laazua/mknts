#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 12345 /* Port to listen on */
#define BACKLOG 10 /* Number of connections allowed in the queue */

int main(void) 
{
    int sockfd, newfd; /* Listen on sockfd, new connection on newfd */
    struct sockaddr_in server_addr, client_addr;
    socklen_t sin_size;
    char buffer[256];
    int n;

    /* Create a TCP socket */
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("ERROR opening socket");
        exit(1);
    }

    /* Bind the socket to a local address */
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;
    memset(server_addr.sin_zero, '\0', sizeof(server_addr.sin_zero));
    if (bind(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("ERROR on binding");
        exit(1);
    }

    /* Listen for incoming connections */
    if (listen(sockfd, BACKLOG) < 0) {
        perror("ERROR on listen");
        exit(1);
    }

    /* Accept incoming connections */
    sin_size = sizeof(client_addr);
    newfd = accept(sockfd, (struct sockaddr *)&client_addr, &sin_size);
    if (newfd < 0) {
        perror("ERROR on accept");
        exit(1);
    }

    /* Read data from the client */
    n = recv(newfd, buffer, sizeof(buffer), 0);
    if (n < 0) {
        perror("ERROR reading from socket");
        exit(1);
    }
    printf("Received %d bytes: %s\n", n, buffer);

    /* Send data to the client */
    n = send(newfd, "Hello, world!", 14, 0);
    if (n < 0) {
        perror("ERROR writing to socket");
        exit(1);
    }

    /* Close the sockets */
    close(newfd);
    close(sockfd);

    return 0;
}
