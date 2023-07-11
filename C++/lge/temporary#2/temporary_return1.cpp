#include <iostream>

class Point{
    int x,y;

    Point(int x, int y) : x(x), y(y) { std::cout << "Point(int,int)" << std::endl; }
    ~Point()    { std::cout << "~Point()" << std::endl; }
};

// --------------------------------------------

void f1(Point p1) {}
void f2(Point& p2) {}

Point pt(1,2);

Point f3(){ // return by value
    return pt;
}

Point& f4(){ // return by reference
    return pt;
}


int main(){
    f3().x = 10;    // ERROR
    f4().x = 10;    // OK pt.x = 10

    // Point pt(1,2);
    // f1(pt);
    // f2(pt);

}