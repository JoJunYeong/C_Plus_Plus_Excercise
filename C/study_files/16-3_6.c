// 열거형

#include <stdio.h>

enum {RED, BLUE, WHITE, BLACK};
enum {A = 3, B, C, D};  // 열거형의 수를 0부터 시작하고 싶지 않다면 이와같은 방법으로 처음 수를 지정해 주면 된다.

int main() {
    int palette = RED;
    switch(palette){
        case RED :
            printf("palette : RED \n");
            break;
        case BLUE :
            printf("palette : BLUE \n");
            break;
        case WHITE :
            printf("palette : WHITE \n");
            break;
        case BLACK :
            printf("palette : BLACK \n");
            break;
    }
    printf("C = %d\n",C);

    return 0;
}