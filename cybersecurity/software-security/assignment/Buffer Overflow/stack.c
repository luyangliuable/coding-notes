/* stack.c */

/* This program has a buffer overflow vulnerability. */
/* Our task is to exploit this vulnerability */
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int bof(char *str,int studentId)
{
    int bufferSize;
    bufferSize = 12 + studentId%32;
    
    char buffer[bufferSize];

    /* The following statement has a buffer overflow problem */ 
    strcpy(buffer, str);

    return 1;
}

int main(int argc, char **argv)
{
    char str[517];
    FILE *badfile;

    int studentId = ; // please input your studentId
    badfile = fopen("badfile", "r");
    fread(str, sizeof(char), 517, badfile);
    bof(str,studentId);

    printf("Returned Properly\n");
    return 1;
}
