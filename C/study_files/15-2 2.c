// 이상한 scanf
#include <stdio.h>

int main() {

    int num;
    char c;
    
    printf("숫자를 입력하세요 : ");
    scanf("%d", &num);

    fflush(stdin);  // fflush는 MS계열의 컴파일러로만 해야된다 gcc에서는 정상적으로 안될확률이 크다.

    printf("문자를 입력하세요 : ");
    scanf("%c", &c);
    printf("%c 출력",c);

    return 0;
}






