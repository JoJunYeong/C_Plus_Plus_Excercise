#include <string.h>
#include <iostream>

class Photon_Cannon{
    int mHp, mShield;
    int mCoordX, mCoordY;
    int mDamage;
    char* mName;

    public :
        Photon_Cannon(int x, int y);
        Photon_Cannon(int x, int y, char *name);
        Photon_Cannon(const Photon_Cannon& pc);
        ~Photon_Cannon();

        void ShowStatus();

};