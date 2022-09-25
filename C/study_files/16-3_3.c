/*

구조체 변수를 정의하는 색다른 방법.
예제를 이렇게 길게 만든 이유는 소스를 읽으면서 구조체와 조금 더 친해지기 바래서
입니다. 소스를 찬찬히 분석해보세요 ^^

*/

#include <stdio.h>

struct obj {
    char name[20];
    int x,y;
}Ball = {"abc",10,2};   // 구조체 초기화 방법

char copy_str(char *dest, char *src);
int Print_Obj_Status(struct obj OBJ);



int main(){
    Ball.x = 3;
    Ball.y = 4;
    copy_str(Ball.name, "RED BALL");

    Print_Obj_Status(Ball);

    return 0;
}

int Print_Obj_Status(struct obj OBJ){
    printf("Location of %s \n", OBJ.name);
    printf("( %d , %d ) \n", OBJ.x, OBJ.y);

    return 0;
}

char copy_str(char *dest, char *src) {

    while(*src){
        *dest = *src;
        src++;
        dest++;
    }

    *dest = '\0';

    return 1;
}




