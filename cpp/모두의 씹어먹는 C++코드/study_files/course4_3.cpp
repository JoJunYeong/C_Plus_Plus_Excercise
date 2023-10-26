#include "course4_3.hpp"

Marine::Marine(){
    mHp = 50;
    mCoordX = mCoordY = 0;
    mDamage = 5;
    mIsDead = false;
    mName = NULL;
}

Marine::Marine(int x, int y, const char* name) {

    mName = new char[strlen(name)+1];
    strcpy(mName,name);

    mCoordX = x;
    mCoordY = y;
    mHp = 50;
    mDamage = 5;
    mIsDead = false;
}

Marine::~Marine(){
    std::cout << mName << "의 소멸자 호출!" << std::endl;
    if(mName != NULL)
        delete[] mName;
}


int Marine::Attack() { return mDamage; }

void Marine::BeAttacked(int damage_earn) {
    mHp -= damage_earn;
    if(mHp <= 0)
        mIsDead = true;
}

void Marine::ShowStatus(){
    std::cout << " *** Marine : " << mName <<" *** " << std::endl;
    std::cout << " Location : ( " << mCoordX << " , " << mCoordY << " ) " << std::endl;
    std::cout << " HP : " << mHp << std::endl;
}




