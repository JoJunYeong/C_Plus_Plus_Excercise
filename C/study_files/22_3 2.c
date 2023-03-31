/*  여러가지 typedef 예제들  */

#include <stdio.h>

int add(int a, int b) {return a+b;}

typedef int CAL_TYPE;
typedef int (*Padd)(int, int);  // (int,int) 를 인자로 받는 포인터를 Padd단어 하나로 지정하겠다.
typedef int Arrays[10]; // 원소가 10개인 배열을 선언해라 를 Arrays 단어 하나로 치환

int main(){
    CAL_TYPE a = 10;
    Arrays arr = {1,2,3,4,5,6,7,8,9,0};
    Padd ptr = add;

    printf("a : %d \n",a);
    printf("arr[3] : %d \n", arr[3]);
    printf("add(3,5) : %d \n", ptr(3,5));

    return 0;
}






