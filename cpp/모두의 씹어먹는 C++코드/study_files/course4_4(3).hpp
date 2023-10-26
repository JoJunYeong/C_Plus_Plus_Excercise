#include <iostream>

class Marine {
    static int mTotalMarineNum;
    const static int i = 0;

    int mHp;    // 마린 체력
    int mCoordX, mCoordY;   // 마린 위치
    bool mIsDead;

    const int mDefaultDamage;

    public:
        Marine();   // 기본 생성자
        Marine(int x, int y);   // x, y 좌표에 마린 생성
        Marine(int x, int y, int dafaultDamage);   // x, y 좌표에 마린 생성

        int Attack() const;   // 데미지를 리턴한다. (const를 붙임으로서 변수의 값을 바꾸지 않고 읽기만 한다는 것을 선언.)
        Marine& BeAttacked(int damageEarn); // 입는 데미지
        void Move(int x, int y);    // 새로운 위치

        void ShowStatus();  // 상태를 보여준다.
        static void ShowTotalMarine();
        ~Marine();

};


class A{

    int x;

    public:
        A(int c);
        
        int& access_x();
        int get_x();
        void show_x();


};


