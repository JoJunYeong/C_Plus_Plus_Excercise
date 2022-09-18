// 두 변수의 값을 교환하는 함수

#include <stdio.h>

int swap(int *a, int *b); // 함수의 원형
// 함수의 원형을 파일의 맨 위에 선언하여 컴파일단계에서 문제가 생기면 어디에서 어떤 오류가 났는지 알려줄 수 있도록 한다.

int main(){
    int i, j ;

    i=3;
    j=5;

    printf("SWAP이전 : i = %d , j = %d \n",i,j);

    swap(&i,&j);    // 참조값을 인자로 보낸다.

    printf("SWAP이후 : i = %d , j = %d \n",i,j);


    return 0;
}



int swap(int *a, int *b){   // int형을 가리키는 포인터 변수를 인자로 갖고있다.
    int tmp = *a;
    *a=*b;  // 주소를 교환한게 아니라 변수의 값을 교환해 준게 된다.
    *b=tmp;
    printf("%d %p\n\n", *a,a);  // *a가 내용이고, a가 주소이다.

    return 0;
}

