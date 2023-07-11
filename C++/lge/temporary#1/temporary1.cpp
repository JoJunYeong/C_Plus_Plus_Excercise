#include <iostream>

class Point{
    int x,y;
public:
    Point(int x, int y) : x(x), y(y) { std::cout << "Point(int, int)" << std::endl; }
    ~Point()    { std::cout << "~Point()" << std::endl; }
};

int main() {

    Point pt(1,2);  // 객체에 이름이 있다 (네임드 오브젝트) : 자신을 선언한 블록의 끝에서 파괴
    Point (1,2);  // 객체에 이름이 없다 (언네임드 오브젝트) : 자신을 선언한 문장의 끝에서 파괴 (임시객체 - temporary)

    std::cout << "------------" << std::endl;

    return 0;
}