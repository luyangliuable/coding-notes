#include<stdio.h>
// this function will affect the values
void swap_by_pointer(int *pa, int *pb) 
{ 
    int temp = *pa; 
    *pa = *pb; 
    *pb = temp; 
} 
// this function will not affect the values
void swap_by_value(int a, int b) 
{ 
    int temp = a; 
    a = b; 
    b = temp; 
}
// main function to drive the program
int main(){

    int a = 1;  // define two variables
    int b = 2;
    // output inital values  
    printf("Initial values:\n");
    printf("a = %d, b = %d\n", a, b);
    
    // output values after calling by values
    printf("Call by values:\n");
    swap_by_value(a, b);
    printf("a = %d, b = %d\n", a, b);

    // output values after calling by pointers
    printf("Call by pointers:\n");
    swap_by_pointer(&a, &b);
    printf("a = %d, b = %d\n", a, b);
}
