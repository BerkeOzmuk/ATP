#ifndef SERVO_CPP
#define SERVO_CPP

#include <iostream>

bool isWindowOpen = false;
extern "C" {   
    void openWindow(){
        std::cout << "Raam wordt geopend!" << '\n';
        isWindowOpen = true;
    };

    void closeWindow(){
        std::cout << "Raam wordt gesloten!" << '\n';
        isWindowOpen = false;
    };

    bool getWindowStatus(){
        return isWindowOpen;
    }
}

#endif