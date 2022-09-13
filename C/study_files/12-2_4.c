// 배열이름의 비밀

#include <stdio.h>

int main(){
    int arr[3] = {1,2,3};
    printf("\n%d \n",arr);
    printf("arr 의 정체 : %p \n",arr);
    printf("arr[0]의 주소값 : %p \n", &arr[0]);

    return 0;
}

