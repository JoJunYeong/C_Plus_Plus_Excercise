
/* 메인 함수의 인자 */

// #include <stdio.h>

// int main(int argc, char **argv){
//     printf("받은 인자의 개수 : %d \n",argc);
//     printf("이 프로그램의 경로 : %s \n", argv[0]);


//     return 0;
// }

/* 인자를 가지는 메인 함수 */

#include <stdio.h>

int main(int argc, char **argv) {
    int i;
    printf("받은 인자의 개수 : %d \n", argc);

    for( i= 0; i < argc ; i++){
        printf("이 프로그램이 받은 인자 : %s \n", argv[i]);
    }


    return 0;
}




