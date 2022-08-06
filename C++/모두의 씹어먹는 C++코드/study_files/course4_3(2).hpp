#include <string.h>
#include <iostream>

class Photon_Cannon{
    int mHp, mShield;
    int mCoordX, mCoordY;
    int mDamage;

    public :
        Photon_Cannon(int x, int y);
        Photon_Cannon(const Photon_Cannon& pc);
        ~Photon_Cannon();

        void ShowStatus();

};