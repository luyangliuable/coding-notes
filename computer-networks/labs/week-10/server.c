#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 8080
#define BUFFER_SIZE 1024


int main() {

  int server_fd, client_fd, addr_len;
  struct sockaddr_in server_addr, client_addr;
  char buffer[BUFFER_SIZE];

  /***************************************************************************/
  /*                               Start socket                              */
  /***************************************************************************/
  server_fd = socket(AF_INET, SOCK_STREAM, 0);

  if (server_fd == -1) {
    perror("socket");
    exit(EXIT_FAILURE);
  }

  server_addr.sin_family = AF_INET;
  server_addr.sin_addr.s_addr = INADDR_ANY;
  server_addr.sin_port = htons(PORT);


  if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) ==
      -1) {
    perror("bind");
    exit(EXIT_FAILURE);
  }
  if (listen(server_fd, 1) == -1) {
    perror("listen");
    exit(EXIT_FAILURE);
  }

  addr_len = sizeof(client_addr);

  /***************************************************************************/
  /*                      Create client file descriptor                      */
  /***************************************************************************/
  client_fd = accept(server_fd, (struct sockaddr *)&client_addr,
                     (socklen_t *)&addr_len);

  if (client_fd == -1) {
    perror("accept");
    exit(EXIT_FAILURE);
  }


  // Receive a message from the client
  while (1) {

    /*************************************************************************/
    /*       Read new content from client file descriptor into a buffer      */
    /*************************************************************************/
    memset(buffer, 0, BUFFER_SIZE);
    read(client_fd, buffer, BUFFER_SIZE);

    printf("Client: %s", buffer);

    /*************************************************************************/
    /*           Get message from standard input and send to client          */
    /*************************************************************************/
    // Send a message to the client
    printf("Server: ");
    fgets(buffer, BUFFER_SIZE, stdin);
    send(client_fd, buffer, strlen(buffer), 0);
  }

  close(client_fd);
  close(server_fd);
  return 0;
}
