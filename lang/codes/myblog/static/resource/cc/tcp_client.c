#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>

int main(int argc, char *argv[]) {
    int sockfd, n;
    struct sockaddr_in server_addr;
    struct hostent *server;
    char buffer[256];

    /* Check for required arguments */
    if (argc < 3) {
        fprintf(stderr, "Usage: %s hostname port\n", argv[0]);
        exit(1);
    }

    /* Get the server's address */
    server = gethostbyname(argv[1]);
    if (server == NULL) {
        fprintf(stderr, "ERROR, no such host\n");
        exit(1);
    }

    /* Create a TCP socket */
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("ERROR opening socket");
        exit(1);
    }

    /* Connect to the server */
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(atoi(argv[2]));
    memcpy(&server_addr.sin_addr.s_addr, server->h_addr, server->h_length);
    memset(server_addr.sin_zero, '\0', sizeof(server_addr.sin_zero));
    if (connect(sockfd, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("ERROR connecting");
        exit(1);
    }

    /* Send data to the server */
    n = send(sockfd, "Hello, world!", 14, 0);
    if (n < 0) {
        perror("ERROR writing to socket");
        exit(1);
    }

    /* Read data from the server */
    n = recv(sockfd, buffer, sizeof(buffer), 0);
    if (n < 0) {
        perror("ERROR reading from socket");
        exit(1);
    }
    printf("Received %d bytes: %s\n", n, buffer);

    /* Close the socket */
    close(sockfd);

    return 0;
}
