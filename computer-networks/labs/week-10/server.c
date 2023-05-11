#include <arpa/inet.h>
#include <netinet/in.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 8080
#define BUFFER_SIZE 1024

void *sendMessage(void *vargp);

int main() {

  int server_fd, client_fd, addr_len;
  struct sockaddr_in server_addr, client_addr;
  char recv_buffer[BUFFER_SIZE];

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

  pthread_t send_thread;
  pthread_create(&send_thread, NULL, &sendMessage, (void *)&client_fd);

  // Receive a message from the client
  while (1) {
    /*************************************************************************/
    /*       Read new content from client file descriptor into a buffer      */
    /*************************************************************************/
    read(client_fd, recv_buffer, BUFFER_SIZE);
    printf("Client: %s", recv_buffer);
    memset(recv_buffer, 0, BUFFER_SIZE);
  }

  close(client_fd);
  close(server_fd);
  return 0;
}

void *sendMessage(void *server_fd_ptr) {
  int server_fd = *((int *)server_fd_ptr);
  char send_buffer[BUFFER_SIZE];

  while (1) {
    /*************************************************************************/
    /*           Get message from standard input and send to server          */
    /*************************************************************************/
    /* printf("Server: "); */

    // Send a message to the server
    fgets(send_buffer, BUFFER_SIZE, stdin);
    /* printf("Sending %s.\n", send_buffer); */
    int res = send(server_fd, send_buffer, strlen(send_buffer), 0);

    if (res == -1) {
      perror("send");
      exit(EXIT_FAILURE);
    }

    memset(send_buffer, 0, BUFFER_SIZE);
  }
}
