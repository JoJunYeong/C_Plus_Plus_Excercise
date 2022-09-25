// 구조체 포인터 연습

#include <stdio.h>

int add_one(int *a);

struct test{
    /* data */
    int c;
};

int main(){
    struct test t;
    struct test *ptr = &t;

    // pt가 가리키는 구조체 변수의 c멤버의 값을 0으로 한다.
    ptr->c = 0 ;

    // add_one 함수의 인자에 t 구조체 변수의 멤버 c 주소값을 전달하고 있다.
    add_one(&t.c);
    printf("t.c : %d \n", t.c);


    // add_one 함수의 인자에 ptr이 가리키는 구조체 변수의 멤버 c의 주소값을 전달하고 있다.
    add_one(&ptr->c);
    printf("t.c : %d \n", t.c);

    return 0;
}

int add_one(int *a){

    (*a)++;

    return 0;
}

