/*

순수 가상함수와 추상함수

*/

#include <iostream>

class Animal{   // speak 같은 가상함수를 하나라도 갖고 있는 클래스를 "추상 클래스"라고 한다.
    public:
        Animal() {}
        virtual ~Animal() {}
        virtual void speak() = 0;   // 이 함수는 무엇일까? 바로 "무엇을 하는지 정의되어 있지 않은 함수"이다.
                                    // 즉, 반드시 오버라이딩 되어야 하는 함수라는 의미이다.
                                    // 이런함수를 "가상함수" 라고 부른다.
};

class Dog : public Animal {
    public:
        Dog() : Animal() {}
        void speak() override { std::cout << "왈왈" << std::endl; }
};

class Cat : public Animal {
    public:
        Cat() : Animal() {}
        void speak() override { std::cout << "야옹야옹" << std::endl; }
};

int main(){
    Animal* dog = new Dog();
    Animal* cat = new Cat();

    dog->speak();
    cat->speak();
}