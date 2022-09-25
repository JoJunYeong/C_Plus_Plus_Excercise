// 제일 어려운 단원

#include <stdio.h>

int main(){

    int arr[3]= {1,2,3};
    int *parr;

    parr = arr; // sizeof 나 & 연산자가 없으므로 배열 arr의 가장 앞자리 주소가 parr로 전달된다.
    // parr = &arr[0] 과 동일한 기능을 한다.

    printf("arr[1] : %d \n", arr[1]);   // arr[1]은 *(arr+1) 로 변환된다.
    printf("parr[1] : %d \n", parr[1]); // parr[1]은 *(parr+1) 로 변환된다.
    

    return 0;
}




