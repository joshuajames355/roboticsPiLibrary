import smbus

HIGH = 0
LOW = 1
INPUT = 2
OUTPUT = 3
CHANNELA = 4
CHANNELB = 5

bus = smbus.SMBus(1)
address = 0x40

def getAnaloguePower(pin):
	return bus.read_byte_data(address,pin + 100)
	
def getDigitalPower(pin):
	return bus.read_byte_data(address,pin)	

#power is HIGH or LOW
def setPin(pin, power):
    if power == HIGH:
        writeString("h", str(pin))
    else:
        writeString("l", str(pin))

#mode is INPUT or OUTPUT
def setPinMode(pin, mode):
    if mode == INPUT:
        writeString("i", str(pin))
    else:
        writeString("o", str(pin))

#channel is CHANNELA or CHANNELB
def setMotorPower(channel, power):
    if channel == CHANNELA:
        writeString("a", str(power))
    else:
        writeString("b", str(power))

def encodeStringAsByteArray(string):
    array = []
    for each in string:
        array.append(ord(each))
    return array


def writeString(command,data):
    bus.write_i2c_block_data(address,ord(command),encodeStringAsByteArray(data))


