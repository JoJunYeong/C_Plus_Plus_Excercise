

/*  매크로 함수  */

#include <stdio.h>

#define square(x) x *x  // 매크로 함수 (square(x)를 x*x로 치환하겠다.)
// 정의방법
// #define 함수이름(인자) 치환할것
/*
매크로와 함수는 큰 차이가 있는데, 바로 전처리기에 의해 언제 결과가 나오느냐 이다.
매크로는 #define이기 때문에 컴파일러가 컴파일 할 때, 정의에 맞게 결과가 바뀌지만, 
함수는 라인바이 라인으로 타고 흘러내려갈 때 결과값이 나오게 된다.
*/

#define PrintVariableName(var) printf(#var "\n");
// 인자에 #을 붙이면 문자열로 만들어준다.
// c언어에서 동일한 문자열은 하나로 만들어버리기 때문에 합쳐진다.

#define AddName(x,y) x##y
// ##은 입력한 것을 하나로 합쳐주는 역할을 한다.

int main(int argc, char **argv){
    printf("square(3) : %d \n", square(3));
    // 컴파일 하면 printf("square(3) : %d \n", 3*3); 으로 바뀐다.

    PrintVariableName(a);
    int AddName(b,d);   // 컴파일을 하면 int bd; 라는 것으로 치환된다.

    return 0;
}





