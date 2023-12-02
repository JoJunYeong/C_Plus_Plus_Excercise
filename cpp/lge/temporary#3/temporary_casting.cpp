// temporary와 casting
#include <iostream>

struct Base
{
    int value = 10;

    Base() = default;

    Base(const Base& b) : value(b.value)
    {
        std::cout << "Base copy" << std::endl;
    }
};

struct Derived : public Base
{
    int value = 20;
};

int main(){

    Derived d;
    std::cout << d.value << std::endl;
    std::cout << static_cast<Base&>(d).value << std::endl;
}


