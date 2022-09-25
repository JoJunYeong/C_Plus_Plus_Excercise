// 공용체 (Union)

// 공용체는 많이 사용하지는 않지만, 한번 보자면
// 구조체의 내부 멤버들은 메모리에 독립적으로 얹어져 있지만 
// 공용체는 내부 멤버들의 시작 주소가 모두 같다. 즉, 예로들면 두 변수가 차지하는 메모리 영역이 겹쳐지는 것이다.

// 공용체 예시
// #include <stdio.h>
// union A{
//     int i;
//     char j;
// };
// int main(){
//     union A a;
//     a.i = 0x12345678;
//     printf("\n%x\n",a.j);   // 리틀 앤디안에 대해 알려주기 위한 예제임 
//     // 빅 엔지안도 설명 했음.
//     return 0;
// }

#include <stdio.h>

int main()
{
    enum {CHAR_ = 1, INT_, FLOAT_};
    union data
    {
        char a;
        int x;
        float f;
    } myData = {'o'};   // union은 첫번째 멤버만 초기화 할 수 있다.

    int mode = CHAR_;

    myData.a = 'A';
    printf("Here is the Data:\n%c\n%i\n%.3f\n", myData.a, myData.x, myData.f );

    myData.x = 42;
    mode = INT_;
    printf("Here is the Data:\n%c\n%i\n%.3f\n", myData.a, myData.x, myData.f );

    myData.f = 101.357;
    mode = FLOAT_;
    printf("Here is the Data:\n%c\n%i\n%.3f\n", myData.a, myData.x, myData.f );

    if( mode == CHAR_ )
        printf("The char is being used\n");
    else if( mode == INT_ )
        printf("The int is being used\n");
    else if( mode == FLOAT_ )
        printf("The float is being used\n");

    return 0;
}


