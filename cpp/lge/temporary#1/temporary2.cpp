#include <iostream>

class Point{
public:
    int x,y;
    Point(int x, int y) : x(x), y(y) { }

    void set(int a, int b) { x = a; y = b; }
};

int main(){
    Point pt(1,2);  // pt라는 이름의 Point 객체를 만든다.

    pt.x = 10;  // pt의 x를 10으로 바꿔준다.(OK)
    Point(1,2).x = 10;  // Point(1,2) 라는 임시객체를 만들고(이 객체의 수명은 ;까지), 이 임시객체의 x에다가 10을 넣겠다. (ERROR)
    // 왜 error가 나는가? - temporary는 등호의 왼쪽에 올 수 없다. = temporary는 rvalue 이다.
    Point(1,2).set(10,20);  // OK

    Point* p1 = &pt;    // OK
    Point* p2 = &Point(1,2);   // ERROR
     // 임시객체의 주소를 담아서 p2에다가 넣겠다는 의미. 근데 이렇게 되면, 임시객체가 사라지는 경우, 주소가 가리키는 곳이 없는 이상한 현상이 일어난다.

    Point& r1 = pt; // OK 이름있는 객체들은 참조를 가리키는게 가능하다.
    Point& r2 = Point(1,2); // ERROR 임시객체를 참조로 가리킬 수 없다.
    
    // 하지만 C++에서는 이것을 해결하기 위해 조금 어려운 개념을 도입했는데, 
    const Point& r3 = Point(1,2);   // const(상수참조)때문이다. const는 임시객체의 값을 저장한 변수를 참조할 수 있게 해준다. 

}