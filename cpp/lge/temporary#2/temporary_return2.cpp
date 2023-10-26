#include <iostream>

class Counter{
    int count{0};
public:
    // Counter increment(){    // ERROR (값 리턴)
    Counter& increment(){   // OK (참조리턴)
        ++count;
        return *this;
    }
    int get() const { return count; }
};


int main(){
    Counter c;
    c.increment().increment().increment();
    std::cout << c.get << std::endl;
}


