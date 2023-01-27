/*
 * This example code is from  
 * https://www.programiz.com/c-programming/c-pointers-arrays 
 * */
#include <stdio.h>
int main() {
   int x[10];
   int i;
   for(i = 0; i < 4; ++i) {
      printf("&x[%d] = %p\n", i, &x[i]);
   }
   printf("Address of array x: %p", x);

   return 0;
}
