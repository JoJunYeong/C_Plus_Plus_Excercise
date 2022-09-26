// #define 이란?

/* #define */
#include <stdio.h>

#define VAR 10  // #(전처리기) 들은 문장의 끝에 ;(세미콜론)을 붙이지 않는다!

int main(){
    char arr[VAR] = {"hi"};
    printf("%s \n ",arr);

    return 0;
}


