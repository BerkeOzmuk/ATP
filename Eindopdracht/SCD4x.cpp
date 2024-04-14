#ifndef _SCD4x_CPP
#define _SCD4x_CPP_

#include <iostream>

extern "C" {   
    int readCO2(){
        int CO2ppm =  400 + static_cast <float> (std::rand()) / static_cast <float> (RAND_MAX/600);//400pmm t/m 1000ppm
        return CO2ppm;
    };
    
    void updateCO2(int & CO2){
        CO2 -= 50;
    };
}

#endif