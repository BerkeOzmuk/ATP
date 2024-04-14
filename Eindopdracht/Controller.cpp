#ifndef _CONTROLLER_CPP_
#define _CONTROLLER_CPP_

#include "DHT11.cpp"
#include "SCD4x.cpp"
#include "Ventilatorkachel.cpp"
#include "Servo.cpp"

extern "C"{
    float setKachel(float temperature){
        if(getKachelStatus()){
            if(temperature > 19.9f){
                turnOffKachel();
                return temperature;
            }
            updateTemperature(temperature);
        }
        else{
            if(temperature <= 19.5f){
                turnOnKachel();
            }
        }
        return temperature;
    };

    int setServo(int CO2){
        if(getWindowStatus()){
            if(CO2 <= 600){
                closeWindow();
                return CO2;
            }
            updateCO2(CO2);
        }
        else{
            if(CO2 >= 800){
                openWindow();
            }
        }
        return CO2;
    };
}
#endif