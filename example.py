#A simple program that flash's an LED on and OFF.
#Connect pin 5 to a 330 ohm resistor , an LED and then a ground pin.

#Connect the pi to the arduino by connecting:
#pin 3 to an SDA pin (A4)
#pin 5 to an SDL pin (A5)
#pin 6 to a ground pin

from robot import *
import time

def main():
	setPinMode(5,OUTPUT)
	
	while True:
		setPin(5,HIGH)
		time.sleep(0.5)
		setPin(5,LOW)
		time.sleep(0.5)	
	
main()