

/*  memcmp 함수  */


#include <stdio.h>
#include <string.h>

int main(){
    int arr[10] = {1,2,3,4,5};
    int arr2[10] = {1,2,3,4,5};

    if(memcmp(arr,arr2,sizeof(int)*5) == 0)
        printf("arr과 arr2는 일치! \n");
    else
        printf("arr과 arr2는 일치 안함! \n");

    return 0;
}


