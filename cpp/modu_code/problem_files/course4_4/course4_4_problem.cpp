#include "course4_4_problem.hpp"

A::A(int c)
: x(c)
{}

A::A(const A& a){
    x = a.x;
    std::cout << "복사생성" << std::endl;
}




