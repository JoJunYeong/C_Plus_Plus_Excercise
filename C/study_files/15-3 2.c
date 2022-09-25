// 문자열 리터럴(literal) 에 대한 이해 
// 문자열 다루기 (복사, 합치기, 비교하기)

#include <stdio.h>

int main() {

    char str[] = "sentence";
    char *pstr = "sentence";

    printf("str : %s \n", str);
    printf("pstr : %s \n", pstr);
//    printf("%d, \n","sentence");

    char str2[] = "hello";
    char *pstr2 = "goodbye";

    str2[1] = 'a';
//    pstr2[1] = 'a';


    return 0;
}


