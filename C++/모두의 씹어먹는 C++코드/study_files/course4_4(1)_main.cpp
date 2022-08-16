#include "course4_4(1).hpp"



int main(){

    Marine marine1(2,3);
    Marine marine2(3,5);

    marine1.ShowStatus();
    marine2.ShowStatus();

    std::cout << std::endl << "마린 1이 마린 2를 공격! " << std::endl;
    marine2.BeAttacked(marine1.Attack());

    marine1.ShowStatus();
    marine2.ShowStatus();


    return 0;
}