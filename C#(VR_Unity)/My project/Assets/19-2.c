
/* void형 변수 */

#include <stdio.h>

int read_char(void *p, int byte);

int main(){
    //void a; // 이거는 안되지만
    void *aa; // 이거는 된다.
    /*
    앞의 void a; 의 경우 a의 값의 크기를 정할 수 없기 때문에 메모리상에 a를 위해 
    얼마나 많은 공간을 설정 해 놓아야 하는지 모르지만, 
    void *a 의 경우 '포인터' 이기 때문에 메모리상에 8바이트만큼을 지정하게 된다.
    (64bit 운영체제에서는 포인터의 크기는 8바이트이다.)
    그렇다면 void *a 포인터는 void형의 변수의 메모리 주소를 가지게 될까?
    물론, 논리를 따지고 보면 맞지만 void형 변수라는 것은 존재할 수 없기 때문에 
    void형 포인터의 존재가 쓸모없어 보일 수 있지만, 사실 void는 타입이 없기 때문에, 
    거꾸로 생각해보면 어떠한 형태의 포인터 값이라도 담을 수 있는 마법의 도구가 되어버린다.

    예를들어 
    void *a;
    double b;
    a = &b;

    이런 느낌으로 갈 수도 있다.
    근데 여기에서 한가지 문제점이 생기는데, 그럼 불러다가 쓸 때는 어떻게 하는가?
    라는 문제점이 생긴다. int*는 4byte를 읽어들여야 하고, double*는 8byte를 읽어야 하는데,
    이놈은 뭐란말인가?
    printf("%lf",*a); 
    이렇게 써 버리면 안된다. 
    왜냐하면 *a 는 void 형이기 때문에 어떤 형으로 불러와야 될지를 모르는거다.
    즉, 진짜 주솟값만 담는 변수가 되어버린거다.
    그럼 어떻게 하면 쓸 수 있을까?
    바로 "강제 형변환"을 이용하면 쓸 수 있다.
    printf("%lf",*(double *)a);

    이렇게 사용한다면, 잘 담겨서 나오게 된다.
    
    */
    double b = 3;
    aa = &b;
    printf("%lf\n",*(double *)aa);
    //a=3;


    int arr[1] = {0x12345678};

    printf("%x\n", arr[0]);
    read_char(arr,4);
    
    return 0;
}


int read_char(void *p, int byte){

    do{
        printf("%x\n",*(char *)p);
        byte--;

        p=(char *)p + 1;
    }while( p && byte);

    return 0;

}

