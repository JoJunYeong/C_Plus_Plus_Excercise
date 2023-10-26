#include "course4_4_problem2.hpp"

B::B(int c)
:   a(c)
{}

B::B(const B& b)
: a(b.a)
{}

A B::get_A(){
    A temp(a);
    return temp;
}
