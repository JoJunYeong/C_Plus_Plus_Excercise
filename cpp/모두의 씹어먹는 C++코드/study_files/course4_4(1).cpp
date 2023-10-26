#include "course4_4(1).hpp"


Marine::Marine():
mHp(50),
mCoordX(0),
mCoordY(0),
mDefaultDamage(5),
mIsDead(false){

}

Marine::Marine(int x, int y):
mCoordX(x),
mCoordY(y),
mHp(50),
mDefaultDamage(5),
mIsDead(false){

}

Marine::Marine(int x, int y, int defaultDamage):
mCoordX(x),
mCoordY(y),
mHp(50),
mDefaultDamage(defaultDamage),
mIsDead(false){

}



int Marine::Attack(){
    return mDefaultDamage;
}

void Marine::BeAttacked(int damageEarn){
    mHp -= damageEarn;
    if(mHp <= 0)
        mIsDead = true;
}

void Marine::Move(int x, int y){
    mCoordX = x;
    mCoordY = y;
}

void Marine::ShowStatus(){
    std::cout << " *** Marine *** " << std::endl;
    std::cout << " Location : ( " << mCoordX << " , " << mCoordY << " ) " << std::endl;
    std::cout << " HP : " << mHp << std::endl;

}

