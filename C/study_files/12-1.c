#include <stdio.h>

int main(){

    int *p;
    int a;

    p = &a;
    *p = 3;

    printf("a 의 값 : %d \n", a);
    printf("*p 의 값 : %d \n", *p);
    printf("dsadsada\n\n");


    return 0;
}