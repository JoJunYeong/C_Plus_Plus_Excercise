// 포인터의 포인터 (어려운 단원)

#include <stdio.h>

int main() {
    int a;
    int *pa;
    int **ppa;

    pa = &a;    // 포인터 pa는 a의 주소를 넣는다.
    ppa = &pa;  // 이중 포인터 ppa에 포인터 pa의 주소값을 넣는다.

    a = 3;

    printf("a : %d // *pa : %d // **ppa : %d \n", a, *pa, **ppa);  // 3,3,3
    printf("&a : %p // pa : %p // *ppa : %p \n", &a, pa, *ppa); // a의 주소 ,a의 주소, a의 주소
    printf("&pa : %p // ppa : %p \n", &pa, ppa);    // pa의 주소 , pa의 주소
    //  **ppa => *(*ppa) => *(pa) => *pa => &a
    
    return 0;
}




