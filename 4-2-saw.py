import RPi.GPIO as GPIO

import time

def dec2bin(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)

dac = [26,19,13,6,5,11,9,10]
GPIO.setup(dac,GPIO.OUT)
clean = [0,0,0,0,0,0,0,0]

try:
    period = 3
    time5 = period / 510
    while(1):
        i = 0
        while(i<255):
            GPIO.output(dac,dec2bin(i))
            i += 1
            time.sleep(time5)
        while(i>0):
            GPIO.output(dac,dec2bin(i))
            i -= 1
            time.sleep(time5)
finally:
    GPIO.output(dac,clean)
    GPIO.cleanup()
