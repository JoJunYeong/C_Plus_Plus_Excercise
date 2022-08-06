#include "course4_3(2).hpp"



Photon_Cannon::Photon_Cannon(int x, int y){

    std::cout << "생성자 호출 !" << std::endl;
    mHp = 100;
    mShield = 100;
    mCoordX = x;
    mCoordY = y;
    mDamage = 20;

}


Photon_Cannon::Photon_Cannon(const Photon_Cannon& pc){

    std::cout << "복사 생성자 호출 !" << std::endl;
    mHp = pc.mHp;
    mShield = pc.mShield;
    mCoordX = pc.mCoordX;
    mCoordY = pc.mCoordY;
    mDamage = pc.mDamage; 

}


Photon_Cannon::~Photon_Cannon(){
    
}

void Photon_Cannon::ShowStatus(){

    std::cout << "Photon Cannon " << std::endl;
    std::cout << "Location : ( " << mCoordX << " , " << mCoordY << " ) " << std::endl;
    std::cout << "HP : " << mHp << std::endl;

}




