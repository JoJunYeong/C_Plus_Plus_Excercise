// 배열은 배열이고 포인터는 포인터이다.

#include <stdio.h>

int main(){
    int arr[6] = {1,2,3,4,5,6};
    int* parr = arr;

    printf("Sizeof(arr) : %d \n", sizeof(arr));
    printf("Sizeof(parr) : %d \n", sizeof(parr));   // 포인터의 크기는 64비트 컴퓨터 기준 8바이트이다.

    return 0;
}

/*
C 언어 상에서 배열의 이름이 sizeof 연산자나 주소값 연산자(&)와 사용되는 (&arr 또는 sizeof(arr)) 경우를 빼면, 
배열의 이름은 암묵적으로 첫 번째 원소를 가리키는 포인터로 타입 변환됩니다.
*/

