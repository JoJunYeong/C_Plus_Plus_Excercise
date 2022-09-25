// 배열 이름의 주소값?

/*

배열 이름에 sizeof 연산자와 주소값 연산자를 사용할 때 빼고는 
전부다 포인터로 암묵적 변환이 이루어진다고 하였습니다. 
그렇다면 주소값 연산자를 사용하면 어떻게 되길래 그러는 것일까요? 한 번 코드로 살펴봅시다.
*/

#include <stdio.h>

int main(){
    int arr[3] = {1,2,3};
    int (*parr)[3] = &arr;

    printf("arr[1]: %d \n", arr[1]);
    printf("parr[1] : %d \n", (*parr)[1]);

    return 0;
}
