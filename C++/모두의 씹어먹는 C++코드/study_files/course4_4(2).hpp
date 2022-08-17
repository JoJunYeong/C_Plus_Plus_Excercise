#include <iostream>

class Marine{
    static int mTotalMarineNum;
    const static int i = 0;

    int mHp;    // 마린 체력
    int mCoordX, mCoordY;   // 마린 위치
    bool mIsDead;   // 마린 생사

    const int mDefaultDamage;   // 기본 공격력

    public:
        Marine();   // 기본 생성자
        Marine(int x, int y);   // x, y 좌표에 마린 생성
        Marine(int x, int y, int defaultDamage);

        int Attack();   // 데미지를 리턴한다.
        void BeAttack(int damageEarn);  // 입는 데미지
        void Move(int x, int y);

        void ShowStatus(); // 상태를 보여준다.
        void UpTotalMarineNum();
        void DownTotalMarineNum();
        int ReturnTotalMarineNum();
        static void ShowTotalMarine();
        ~Marine();
    
};