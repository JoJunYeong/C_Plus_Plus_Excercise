#include "course4_4(3).hpp"

int main(){

    Marine marine1(2,3,5);
    marine1.ShowStatus();

    Marine marine2(3,5,10);
    marine2.ShowStatus();

    std::cout << std::endl << "마린 1이 마린 2를 두번 공격!" << std::endl;
    marine2.BeAttacked(marine1.Attack()).BeAttacked(marine1.Attack());

    marine1.ShowStatus();
    marine2.ShowStatus();


///.. 아래는 예제코드를 그대로 가져옴

    A a(5);
    a.show_x();

    int& c = a.access_x();
    c=4;
    a.show_x();

    int d = a.access_x();
    d=3;
    a.show_x();

    // 아래는 오류
    // int& e = a.get_x();
    // e= 2;
    // a.show_x();

    int f = a.get_x();
    f=1;
    a.show_x();

    return 0;
}


