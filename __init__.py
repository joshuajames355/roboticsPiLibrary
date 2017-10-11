import smbus

#Constants
HIGH = 0
LOW = 1
INPUT = 2
OUTPUT = 3
CHANNELA = 4
CHANNELB = 5


bus = smbus.SMBus(1)
address = 0x04

#power is HIGH or LOW
def setPinPower(pin, power):
    if power == HIGH:
        bus.write(address, "h" + str(pin))
    elif power == LOW:
        bus.write(address, "l" + str(pin))

#mode is INPUT or OUTPUT
def setPinMode(pin, mode):
    if mode == INPUT:
        bus.write(address, "i" + str(pin))
    elif mode == OUTPUT:
        bus.write(address, "o" + str(pin))

#channel is CHANNELA or CHANNELB
def setMotorPower(channel, power):
    if channel == CHANNELA:
        bus.write(address, "a" + str(power))
    elif channel == CHANNELB:
        bus.write(address, "b" + str(power))
