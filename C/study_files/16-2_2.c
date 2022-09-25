// 구조체 포인터에서 헷갈리는 부분


#include <stdio.h>

struct test{
    /* data */
    int c;
    int *pointer;
};

int main() {
    struct test t;
    struct test *ptr = &t;
    int i = 0;

    // t의 멤버 pointer가 i를 가리키게 한다.
    t.pointer = &i;

    // t의 멤버 pointer가 가리키는 변수의 값을 3으로 만든다.
    *t.pointer = 3; //  *(t.pointer) 와 같다
    printf("i : %d \n",i);

    /*

    연산자 -> 가 * 보다 우선순위가 높으므로 먼저 해석하게 된다.
    즉,
    (pt가 가리키는 구조체 변수의 pointer 멤버) 가 가리키는 변수의 값을 4로 바꾼다.
    라는 뜻이다.

    */

   *ptr->pointer = 4; //  *(ptr->pointer) 와 같다.
   printf("i : %d \n", i);

    return 0;
}
