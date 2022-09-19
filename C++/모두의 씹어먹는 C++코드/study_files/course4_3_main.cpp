#include "course4_3.hpp"

int main() {
    
    Marine* marines[100];
    
    marines[0] = new Marine(2,3, "Marine2");
    marines[1] = new Marine(3,5, "Marine1");

    marines[0]->ShowStatus();
    marines[1]->ShowStatus();

    std::cout << std::endl << "마린 1이 마린 2를 공격! " << std::endl;
    marines[1]->BeAttacked(marines[0]->Attack());

    marines[0]->ShowStatus();
    marines[1]->ShowStatus();

    delete marines[0];
    delete marines[1];

    return 0;
}




