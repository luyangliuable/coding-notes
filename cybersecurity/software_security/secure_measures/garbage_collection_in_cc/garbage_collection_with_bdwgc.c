/*
    File: example.c
    Description: A simple example of using the Boehm-Demers-Weiser Garbage Collector (BDWGC) in C. Make sure that you are linking the BDWGC library with your program during compilation.You can do this by adding the - lgc flag to your gcc command line.For example : gcc - o example example.c - lgc

   Author: Luyang Liu
   Date: 01-22-2022
*/


#include <gc.h>
#include <stdio.h>

    int
    main() {
  // Allocate memory using the BDWGC
  int *myInt = (int *)GC_MALLOC(sizeof(int));
  *myInt = 5;

  // Use the memory
  printf("Value: %d\n", *myInt);

  // The GC will automatically free the memory when it is no longer needed
  return 0;
}
