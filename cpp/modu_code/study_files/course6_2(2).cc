#include <iostream>

class Base{
    std::string s;

    public:
        Base() :  s("Base") { std::cout << "Base Class" << std::endl; }

        virtual void what() { std::cout << "what() of Base class" << std::endl; }

};

class Derived : public Base{

    std::string s;

    public:
        Derived() : Base(), s("Derived") {}

        void what() override {std::cout << "what() of Derived Class" << std::endl; }
};

int main(){

    Base p;
    Derived c;

    Base* p_c = &c;
    Base* p_p = &p;

    std::cout << " == real object is Base == " << std::endl;
    p_p->what();

    std::cout << " == real object is Derived == " << std::endl;
    p_c->what();

    return 0;

}





