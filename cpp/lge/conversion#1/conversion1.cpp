#include <iostream>

class Int32{
    int value;
public:
    Int32() : value(0) { }
    Int32(int n) : value(n) { }

    operator int() const{ return value; }
};

int main(){
    int pn;
    Int32 un;
    const Int32 un2;
    // 만약에 아래와 같이 쓰게 된다면,
    pn = un;
    // un 과 pn의 형식이 다르기 때문에 컴파일러는 un에 대해서 un.operator int() 가 존재하는지 알아보게 된다.
    // 그래서 Int32 안에 operator int() 만들어서 넣어주었다.

    // 이번엔 반대를 넣어보자
    un = pn;
    // pn.operator Int32() 는 만들 수 없다.
    // 이런경우 복사생성자를 사용하면 된다.
    // 1. un.operator=(pn)
    // 2. Int32(pn)



}


