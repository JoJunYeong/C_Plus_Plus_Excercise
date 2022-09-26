// 다른사람이 만들어 놓은 것 쓰기 (라이브러리 사용)

#include <stdio.h>
#include <string.h>

int main(){
    char str1[20] = {"hi"};
    char str2[20] = {"hello every1"};

    strcpy(str1, str2);

    printf("str1 : %s \n", str1);

    return 0;
}

