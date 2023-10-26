#include "course4_4(2).hpp"

void create_marine();

int main(){

    Marine marine1(2,3,5);
    Marine::ShowTotalMarine();

    Marine marine2(3,5,10);
    Marine::ShowTotalMarine();

    create_marine();

    std::cout << std::endl << " 마린 1이 마린 2를 공격! " << std::endl;
    marine2.BeAttack(marine1.Attack());

    marine1.ShowStatus();
    marine2.ShowStatus();


}


void create_marine(){
    Marine marine3(10,10,4);
    Marine::ShowTotalMarine();
}