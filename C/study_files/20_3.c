/*  2차원 배열의 동적 할당  */

/*
2차원 배열을 동적으로 할당하는 방법으로 크게 두 가지 방법을 생각할 수 있습니다.

1. 포인터 배열을 사용해서 2 차원 배열 처럼 동작하는 배열을 만드는 방법
2. 실제로 2 차원 배열 크기의 메모리를 할당한 뒤 2 차원 배열 포인터로 참조하는 방법

로 꼽을 수 있습니다. 먼저 포인터 배열을 사용하는 방법 부터 살펴봅시다.
*/


#include <stdio.h>
#include <stdlib.h>

int main(int argc , char **argv){
    int i;
    int x,y;
    int **arr;  // 우리는 arr[x][y]를 만들 것이다.

    printf("arr[x][y]를 만들 것이다.\n");
    scanf("%d %d", &x, &y);

    arr = (int **)malloc(sizeof(int *)*x);
    // int * 형의 원소를 x 개 가지는 1차원 배열 생성

    for (i = 0 ; i < x ; i++){
        arr[i] = (int *)malloc(sizeof(int) * y);
        // int 형의 원소를 y개 가지는 i번쨰 자리의 배열 생성
    }

    printf("생성완료! \n");

    for(i =0 ; i < x ; i++ ){
        free(arr[i]);
    }
    free(arr);


    return 0;
}








