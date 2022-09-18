// 포인터의 형을 결정짓는 두가지 요소

#include <stdio.h>

int main(){
    int arr[2][3] = {{1,2,3},{4,5,6}};
    int arrr[3][4] = {{1,2,3,4},{2,2,2,2},{2,2,2,2}};
    int **parr;

    int *par=arr[0];
    int *par2=arrr[0];
    // parr = arr;

    printf("arr[1][1] : %d \n", arr[1][1]);
    // printf("parr[1][1] : %d \n", parr[1][1]);
    printf("sizeof(par) = %d\n\n", sizeof(par));
    printf("sizeof(par2) = %d\n\n", sizeof(par2));

    return 0;
}
