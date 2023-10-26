#include <iostream>
#include <string.h>

class Marine{
    int mHp;    // 마린 체력
    int mCoordX, mCoordY;   // 마린 위치
    int mDamage;    // 공격력
    bool mIsDead;   // 
    char* mName; // 마린 이름

    public:
        Marine();       // 기본 생성자.
        Marine(int x, int y, const char* name);   // x, y 좌표에 마린 생성
        ~Marine();

        int Attack();   // 데미지를 리턴한다.
        void BeAttacked(int damage_earn);  // 입는 데미지
        void Move(int x, int y);    // 새로운 위치

        void ShowStatus();
};
