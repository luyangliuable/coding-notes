#include <arpa/inet.h>
#include <netinet/in.h>
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define SERVER_IP "127.0.0.1"
#define PORT 8080
#define BUFFER_SIZE 1024

void *sendMessage(void *vargp);

typedef struct {
  int socket_fd;
} thread_arg;

int main() {
  int client_fd;
  struct sockaddr_in server_addr;
  char send_buffer[BUFFER_SIZE];
  char recv_buffer[BUFFER_SIZE];
  client_fd = socket(AF_INET, SOCK_STREAM, 0);

  if (client_fd == -1) {
    perror("socket");
    exit(EXIT_FAILURE);
  }

  server_addr.sin_family = AF_INET;
  server_addr.sin_addr.s_addr = inet_addr(SERVER_IP);
  server_addr.sin_port = htons(PORT);

  if (connect(client_fd, (struct sockaddr *)&server_addr,
              sizeof(server_addr)) == -1) {
    perror("connect");
    exit(EXIT_FAILURE);
  }

  pthread_t send_thread;
  pthread_create(&send_thread, NULL, &sendMessage, (void *)&client_fd);

  while (1) {
    read(client_fd, recv_buffer, BUFFER_SIZE);
    fflush(STDIN_FILENO);
    memset(recv_buffer, 0, BUFFER_SIZE);
    printf("Client: %s", recv_buffer);
  }

  close(client_fd);
  return 0;
}

void *sendMessage(void *client_fd_ptr) {
  int client_fd = *((int *)client_fd_ptr);
  char send_buffer[BUFFER_SIZE];

  while (1) {
    printf("Client: ");

    fgets(send_buffer, BUFFER_SIZE, stdin);
    printf("Sending %s.\n", send_buffer);
    int res = send(client_fd, send_buffer, strlen(send_buffer), 0);
    fflush(STDIN_FILENO);

    if (res == -1) {
      perror("send");
      exit(EXIT_FAILURE);
    }

    memset(send_buffer, 0, BUFFER_SIZE);
  }
}
