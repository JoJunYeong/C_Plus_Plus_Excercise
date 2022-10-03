/*  memmove 함수   */

#include <stdio.h>
#include <string.h>

int main(){
    char str[50] = "I love Chewing C hahaha";

    printf("%s \n",str);
    printf("memmove 이후\n");
    memmove(str + 23, str + 17, 6); // str+17 부터 6개를 str+23에 붙여넣기
    printf("%s\n\n", str);



    return 0;
}








