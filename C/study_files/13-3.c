// 함수 (더블포인터 인자, 2차원 배열인자, 상수인자, 함수 포인터)
// 2차원 배열의 각 원소를 1씩 증가시키는 함수

#include <stdio.h>
// 열의 개수가 2개인 이차원 배열과, 총 행의 수를 인자로 받는다.

int addl_element(int(*arr)[2], int row);

int main(){
    int arr[3][2];
    int i,j;

    for(i=0; i<3 ; i++)
        for(j=0; j<2 ; j++)
            scanf("%d", &arr[i][j]);

    addl_element(arr,3);

    for (i = 0; i < 3; i++) {
        for (j = 0; j < 2; j++) {
            printf("arr[%d][%d] : %d \n", i, j, arr[i][j]);
        }
    }

    return 0;
}

int addl_element(int(*arr)[2], int row) {
    int i, j;

    for(i=0; i<row; i++)
        for(j=0; j<2; j++)
            arr[i][j]++;

    return 0;
}





