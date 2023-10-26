#include <iostream>

class Int32{
    int value;
public:
    Int32(int n) : value(n) {}

    Int32 (const Int32&) = delete;  // delete를 사용함으로서 복사생성자를 삭제해본다.
    Int32& operator=(const Int32&) = delete;    // delete를 사용함으로서 디폴트 연산자 operator= 를삭제한다는 의미가 된다.
};

int main(){
    Int32 n1(3);
    Int32 n2 = 3;
    Int32 n3{3};
    Int32 n4 = {3};

    n1 = 3;

}