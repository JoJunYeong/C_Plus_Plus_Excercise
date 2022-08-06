#include "course4_3(2).hpp"


int main(){

    Photon_Cannon pc1(3,3);
    Photon_Cannon pc2(pc1);
    Photon_Cannon pc3 = pc2;

    pc1.ShowStatus();
    pc2.ShowStatus();

    return 0;
}

