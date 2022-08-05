#include "course4_3.hpp"

Marine::Marine(){
    mHp = 50;
    mCoordX = mCoordY = 0;
    mDamage = 5;
    mIsDead = false;
}

Marine::Marine(int x, int y) {
    mCoordX = x;
    mCoordY = y;
    mHp = 50;
    mDamage = 5;
    mIsDead = false;
}

int Marine::Attack() { return mDamage; }

void Marine::BeAttacked(int damage_earn) {
    mHp -= damage_earn;
    if(mHp <= 0)
        mIsDead = true;
}

void Marine::ShowStatus(){
    std::cout << " *** Marine *** " << std::endl;
    std::cout << " Location : ( " << mCoordX << " , " << mCoordY << " ) " << std::endl;
    std::cout << " HP : " << mHp << std::endl;
}




