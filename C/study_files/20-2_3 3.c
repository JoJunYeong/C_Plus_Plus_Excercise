/*  메모리 관련 함수  */

/*  memcpy 함수  */

#include <stdio.h>
#include <string.h>

int main(){
    char str[50] = "I love chewing C hahaha";
    char str2[50];
    char str3[50];

    // memcpy(destination, start, length);
    // memcpy 함수는 메모리의 특정한 부분으로부터 얼마 까지의 부분을 다른 메모리 영역으로 복사해주는 함수이다.
    // 문자열 복사를 전문적으로 하는 함수는 strcpy이지만, memcpy 함수를 사용하는 것도 나쁘지는 않다.

    memcpy(str2,str,strlen(str) + 1);   // str로부터 strlen(str) + 1 만큼의 문자를 str2로 복사해라
    memcpy(str3,"hello",6);     // "hello" 문자열의 메모리 정보를 str3로 복사해라 길이는 6이다. (맨 마지막의 null문자 포함)

    printf("%s \n",str);    
    printf("%s \n",str2);
    printf("%s \n",str3);


    return 0;
}





