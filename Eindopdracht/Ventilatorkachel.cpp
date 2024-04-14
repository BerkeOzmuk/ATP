#ifndef _VENTILATORKACHEL_CPP_
#define _VENTILATORKACHEL_CPP_

#include <iostream>

bool isKachelOn = false;

extern "C" {   
    void turnOnKachel(){
        std::cout << "kachel aan" << '\n';
        isKachelOn = true;
    };

    void turnOffKachel(){
        std::cout << "kachel uit" << '\n';
        isKachelOn = false; //Ahmet Serdar Canakje bracht mij op dit geweldige idee!
    };

    bool getKachelStatus(){
        return isKachelOn;
    };
}

#endif