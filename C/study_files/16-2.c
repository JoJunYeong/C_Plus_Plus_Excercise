// 구조체 포인터
// 구조체를 인자로 받기
// 구조체의 대입

#include <stdio.h>

struct test{
    /* data */
    int c;
};

int main(){
    struct test t;
    struct test *ptr = &t;

    // pt 가 가리키는 구조체 변수의 c 멤버의 값을 0으로 한다.
    (*ptr).c = 0;
    printf("t.c : %d \n", t.c);

    // pt가 가리키는 구조체 변수의 c 멤버의 값을 1으로 한다.
    // -> 연산자의 의미는 "pt가 가리키는 구조체 변수의 멤버"를 의미한다.
    ptr->c = 1;
    printf("t.c : %d \n",t.c);

    return 0;
}






