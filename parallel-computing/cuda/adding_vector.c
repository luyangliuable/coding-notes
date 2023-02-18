__global__ void add(int *a, int *b, int *c) {
  /*
   * Pass pointers into parameters
   */
  *c = *a + *b;
}

int main(void) {
  int a, b, c;
  int *d_a, *d_b, *d_c;
  int size = sizeof(int);

  // Allocate space for device copies of a, b and c.
  cudaMalloc((void **)&d_a, size);
  cudaMalloc((void **)&d_b, size);
  cudaMalloc((void **)&d_c, size);

  // Copying the inputs to the device (GPU)
  cudaMemcpy(d_a, &a, size, cudaMemcpyHostToDevice);
  cudaMemcpy(d_b, &b, size, cudaMemcpyHostToDevice);
  cudaMemcpy(d_c, &b, size, cudaMemcpyHostToDevice);

  // Launch add() kernal on GPU. Execute N times in parallel
  int N = 3
  add << 1, 1 >> (d_a, d_b, d_c);

  // Copy result back to the host
  cudaError err = cudaMemcpy(&c, d_c, size, cudaMemcpyDeviceToHost);

  // Error handling
  if (err != cudaSuccess) {
    printf("CUDA error copying to Host: %s\n", cudaGetErrorString(err));
  }

  printf("result is %d.\n", c);

  // Clean up
  cudaFree(d_a);
  cudaFree(d_b);
  cudaFree(d_c);

  return 0;
}
