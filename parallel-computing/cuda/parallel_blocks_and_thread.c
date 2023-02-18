__global__ void add(int *a, int *b, int *c) {
/*
* Pass pointers into parameters
*/
int index = threadIdx.x + blockIdx.x * blockDim.x;
if (index < n) {
  // Avoid accessing beyond end of arrays.
  c[index] = a[index] + b[index];
}
}

#define N (2048 * 2048)
#define THREADS_PER_BLOCK 512
int main(void) {
  int *a, *b, *c;
  int *d_a, *d_b, *d_c;

  int size = N * sizeof(int);

  // Allocate space for device copies of a, b, c.
  cudaMalloc((void **)&d_a, size);
  cudaMalloc((void **)&d_b, size);
  cudaMalloc((void **)&d_c, size);

  // Alloc space for host copies  of a, b, c and setup input values
  a = (int *)malloc(size);
  random_ints(a, N);
  b = (int *)malloc(size);
  random_ints(b, N);
  c = (int *)malloc(size);

  // Copy inputs to device
  cudaMemcpy(d_a, a, size, cudaMemcpyHostToDevice);
  cudaMemcpy(d_b, b, size, cudaMemcpyHostToDevice);

  // Launch add on device with N threads
  add << N / THREADS_PER_BLOCK, THREADS_PER_BLOCK >> (d_a, d_b, d_c);

  // TODO update the kernel launch
  // What does this mean?
  // add <<<(N + M - 1) / M, M>>>(d_a, d_b, d_c, M);

  // Copy result back to host
  cudaMemcpy(c, d_c, size, cudaMemcpyDeviceToHost);

  // Clean up
  free(a);
  free(b);
  free(c);

  cudaFree(d_a);
  cudaFree(d_b);
  cudaFree(d_c);

  return 0;
}
