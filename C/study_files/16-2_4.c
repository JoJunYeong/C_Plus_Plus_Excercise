// 구조체의 대입

#include <stdio.h>

char copy_str(char *dest, char *src);

struct test{
    /* data */
    int i;
    char c;
    char str[20];
};

int main() {
    struct test a,b;

    b.i = 3;
    copy_str(b.str,"Hello World!");

    a=b;

    printf("a.str : %s \n", a.str);
    printf("a.i : %d \n",a.i);

    
    return 0;
}

char copy_str(char *dest, char *src) {
    while(*src){
        *dest = *src;
        src++;
        dest++;
    }

    *dest = '\0';

    return 1;
}

