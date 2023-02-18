__global__ void mykernal(void) {
  // Kernal parameters can be passed in placed of void
  // global function indicates runs on the device and is called frmo host code.
}


int main(void) {
  /*
   * nvcc command separates source code into host and device components.
   * mykernal() is processed by NVIDIA compiler
   * main() is processed by the standard host compiler
   *
   */

  mykernal<<<1, 1>>>();
  printf("Hello World!\n");
  return 0;
}
