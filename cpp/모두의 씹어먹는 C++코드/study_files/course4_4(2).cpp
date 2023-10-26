#include "course4_4(2).hpp"

int Marine::mTotalMarineNum = 0;

Marine::Marine():
mHp(50),
mCoordX(0),
mCoordY(0),
mDefaultDamage(5),
mIsDead(false){
    UpTotalMarineNum();
}

Marine::Marine(int x, int y):
mHp(50),
mCoordX(x),
mCoordY(y),
mDefaultDamage(5),
mIsDead(false){
    UpTotalMarineNum();
}

Marine::Marine(int x, int y, int defaultDamage):
mHp(50),
mCoordX(x),
mCoordY(y),
mDefaultDamage(defaultDamage),
mIsDead(false){
    UpTotalMarineNum();
}

Marine::~Marine(){
    DownTotalMarineNum();
}

void Marine::Move(int x, int y){
    mCoordX = x;
    mCoordY = y;
}

int Marine::Attack(){
    return mDefaultDamage;
}

void Marine::BeAttack(int damageEarn){
    mHp -= damageEarn;
    if (mHp <= 0) mIsDead = true;
}

void Marine::ShowStatus(){
    std::cout << " *** Marine *** " << std::endl;
    std::cout << " Location : ( " << mCoordX << " , " << mCoordY << " ) " << std::endl;
    std::cout << " HP : " << mHp << std::endl;
    std::cout << " 현재 총 마린 수 : " << ReturnTotalMarineNum() << std::endl;
}

void Marine::UpTotalMarineNum(){
    mTotalMarineNum++;
}

void Marine::DownTotalMarineNum(){
    mTotalMarineNum--;
}

int Marine::ReturnTotalMarineNum(){
    return mTotalMarineNum;
}

void Marine::ShowTotalMarine() {
    std::cout << "전체 마린 수 : " << mTotalMarineNum << std::endl;
}


