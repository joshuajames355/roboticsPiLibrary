# Overview

This is a library for a raspberry pi and that simplifies the proccess of
sending serial commands over i2c to interface with https://github.com/laserbeam897/roboticsArduinoClient.
It currently can set the power and mode of digital pins , send the power of all pins 
(0/1 for digital pins , 0-255 for analog pins) , and set the power/direction for the motor shield.

# API

* getAnaloguePower(pin) , returns 0-255
* getDigitalPower(pin) , returns 0 or 1
* setPin(pin, power) , where power is either HIGH or LOW (constants declared in the library)
* setPinMode(pin, mode) , where mode is either INPUT or OUTPUT (constants declared in the library). This must be run before digital read or write.
* setMotorPower(channel, power), where channel is either CHANNELA or CHANNELB (constants declared in the library). Power must be -255-255 , with 
negative numbers indicating running in reverse.

# Communicaton protocol Details

## Command formats:
*[] indicates a variable. 
* i [pinNumber] //setmode of a digital pin to input
* o [pinNumber] //setmode of a digital pin to output
* h [pinNumber] //set a digit pin to high
* l [pinNumber] //set a digit pin to low
* a [power] //sets the power of the motor on channel A
* b [power] //sets the power of the motor on channel B
	
## Requesting pin power 
	
When sending a request, the command bit represents the pin number 
, where analog pins aremapped as 100 + the pin number.

# Connecting to the arduino.

## Connect the pi to the arduino by connecting:
* pin 3 on the raspberry pi to an SDA pin (A4) on the arduino
* pin 5 on the raspberry pi to an SDL pin (A5) on the arduino
* pin 6 on the raspberry pi to a ground pin on the arduino

## The pins on the raspberry pi are numbered as follows:

![Raspberry PI pin diagram](https://user-images.githubusercontent.com/5314742/31580000-4c86b236-b13b-11e7-96f4-07cf46751c7b.png)