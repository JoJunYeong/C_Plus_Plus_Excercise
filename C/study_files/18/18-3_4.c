

/* #ifdef */

#include <stdio.h>

#define A

int main(){
    #ifdef A
        printf("AAAA\n");
    #endif

    #ifdef B
        printf("BBBB\n");
    #endif

    #ifdef A
        printf("aaaa\n");
    #else
        printf("elseelseelse\n");
    #endif

    return 0;
}



