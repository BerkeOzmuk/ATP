#ifndef _DHT11_CPP_
#define _DHT11_CPP_

#include <iostream>

extern "C" {
    float fahrenheitToCelsius(float fahrenheit){
        return (fahrenheit - 32.0f) * (5.0f/9.0f);
    };

    float readTemperature(){
        float temperatureFahrenheit =  60.8f + static_cast <float> (std::rand()) / static_cast <float> (RAND_MAX/17.0f); //16C t/m 25 
        return fahrenheitToCelsius(temperatureFahrenheit);
    };
  
    void updateTemperature(float & temperature){
        temperature += 0.1;
    };
}

#endif
