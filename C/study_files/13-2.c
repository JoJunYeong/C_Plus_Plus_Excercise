// 함수(포인터로 받는 인자, 함수의 원형, 배열을 인자로 받기)

// 드디어 써먹는 포인터

#include <stdio.h>

int change_val(int *pi){
    printf("---- change_val 함수 안에서 ----\n");
    printf("pi의 값 : %p \n", pi);
    printf("pi가 가리키는 것의 값 : %d \n",*pi);

    *pi = 3;

    printf("---- change_val 함수 끝 ----\n");
    return 0;
}

int main(){
    int i = 0;

    printf("i변수의 주소값 : %p \n", &i);
    printf("호출 이전의 i 값 : %d \n", i);
    change_val(&i);
    printf("호출 이후 i의 값 : %d \n",i);

    return 0;
}





