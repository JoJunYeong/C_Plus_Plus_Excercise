#include <iostream>

class Marine {
    int mHp;    // 마린체력
    int mCoordX, mCoordY;   // 마린위치
    bool mIsDead;   // 마린 생사여부

    const int mDefaultDamage;   // 기본 공격력

    public:
        Marine();   //  기본생성자
        Marine(int x, int y);   // x,y 좌표에 마린생성
        Marine(int x, int y, int defaultDamege);

        int Attack();   // 데미지를 리턴해주는 함수
        void BeAttacked(int damageEarn);    // 입는 데미지
        void Move(int x, int y);    // 새로운 위치

        void ShowStatus();  // 상태를 보여준다.

};



