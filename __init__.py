import smbus
import time

HIGH = 1
LOW = 0
INPUT = 1
OUTPUT = 2

bus = smbus.SMBus(1)
address = 0x04

#power is HIGH or LOW
def setPin(pin, power):
    if power == HIGH:
        bus.write(address, "h" + str(pin))
    else:
        bus.write(address, "l" + str(pin))

def setPinMode(pin, mode):
    if power == INPUT:
        bus.write(address, "i" + str(pin))
    else:
        bus.write(address, "o" + str(pin))


