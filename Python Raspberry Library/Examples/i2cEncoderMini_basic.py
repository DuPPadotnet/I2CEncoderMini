import smbus2
from gpiozero import Button
from time import sleep
import i2cEncoderMiniLib


def EncoderChange():
    print('Changed: %d' % (encoder.readCounter32()))

def EncoderPush():
    print('Encoder Pushed!')

def EncoderRelease():
    print('Encoder Released!')

def EncoderDoublePush():
    print('Encoder Double Push!')

def EncoderLongPush():
    print('Encoder Long Push!')

def EncoderMax():
    print('Encoder max!')

def EncoderMin():
    print('Encoder min!')

def Encoder_INT():
    encoder.updateStatus()


bus = smbus2.SMBus(1)
INT_pin = 4
interrupt = Button(INT_pin, pull_up=True)

encoder = i2cEncoderMiniLib.i2cEncoderMiniLib(bus, 0x20) #Encoder address 0x20

encconfig = ( i2cEncoderMiniLib.WRAP_ENABLE |
              i2cEncoderMiniLib.DIRE_RIGHT |
              i2cEncoderMiniLib.IPUP_ENABLE |
              i2cEncoderMiniLib.RMOD_X1 )
encoder.begin(encconfig)

encoder.writeCounter(0)
encoder.writeMax(35)
encoder.writeMin(-20)
encoder.writeStep(1)
encoder.writeDoublePushPeriod(50)

encoder.onChange = EncoderChange
encoder.onButtonPush = EncoderPush
encoder.onButtonRelease = EncoderRelease
encoder.onButtonDoublePush = EncoderDoublePush
encoder.onButtonLongPush = EncoderLongPush
encoder.onMax = EncoderMax
encoder.onMin = EncoderMin

encoder.autoconfigInterrupt()
print('Board ID code: 0x%X' % (encoder.readIDCode()))
print('Board Version: 0x%X' % (encoder.readVersion()))

interrupt.when_pressed = Encoder_INT   


while True:
    sleep(0.01)
