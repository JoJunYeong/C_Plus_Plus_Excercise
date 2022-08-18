#include "course4_4(3).hpp"

int Marine::mTotalMarineNum = 0;

void Marine::ShowTotalMarine(){
    std::cout << "전체 마린 수 : " << mTotalMarineNum << std::endl;
}

Marine::Marine()
:   mHp(50),
mCoordX(0),
mCoordY(0),
mDefaultDamage(5),
mIsDead(false){
    mTotalMarineNum++;
}

Marine::Marine(int x, int y)
:   mCoordX(x),
mCoordY(y),
mHp(50),
mDefaultDamage(5),
mIsDead(false){
    mTotalMarineNum++;
}

Marine::Marine(int x, int y, int defaultDamage)
:   mCoordX(x),
mCoordY(y),
mHp(50),
mDefaultDamage(defaultDamage),
mIsDead(false){
    mTotalMarineNum++;
}

int Marine::Attack() const{
    return mDefaultDamage;
} 

Marine& Marine::BeAttacked(int damageEarn){
    mHp -= damageEarn;
    if(mHp <= 0)
        mIsDead = true;

    return *this;
}

void Marine::Move(int x, int y){
    mCoordX = x;
    mCoordY = y;
}

void Marine::ShowStatus(){
    std::cout << " *** Marine *** " << std::endl;
    std::cout << " Location : ( " << mCoordX << " , " << mCoordY << " ) " << std::endl;
    std::cout << " HP : " << mHp << std::endl;
    std::cout << " 현재 총 마린 수 : " << mTotalMarineNum << std::endl;
}

Marine::~Marine(){
    mTotalMarineNum--;
}




A::A(int c)
:x(c)
{

}

int& A::access_x(){
    return x;
}

int A::get_x(){
    return x;
}

void A::show_x(){
    std::cout << x << std::endl;
}

