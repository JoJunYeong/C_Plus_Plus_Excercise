// void형의 함수, void형의 포인터에 대한 이해
// main함수의 인자에 대한 이해 (argc, argv)
// 포인터 배열
// 총 3가지 카테고리에 대해 배워보도록 하겠다.

/* return 값이 없는 함수 */

#include <stdio.h>

void add_one(int *p){
    (*p)++;
}

int main(){
    int a = 1;
    printf("Before : %d \n",a);
    add_one(&a);
    printf("After : %d \n",a);

    return 0;
}