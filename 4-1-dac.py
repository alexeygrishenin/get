import RPi.GPIO as GPIO

import time

def decimal2binary(value):
 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)

dac = [26,19,13,6,5,11,9,10]
GPIO.setup(dac,GPIO.OUT)
clean = [0,0,0,0,0,0,0,0]
try:
    while(1):
        a = input("Введите число от 0 до 255")
        if a == 'q':
            exit()
        if a >='a':
            print("Это строка")
            continue
        if float(a)%1 != 0:
            print("Число не целое")
            continue
        a = int(a)
        if a < 0:
            print("Число отрицательное.Введите положительное!")
            continue
        GPIO.output(dac,decimal2binary(a))
        x = 3.3*a/255 
        print("Предполагаемое напряжение ",x)
        print(decimal2binary(a))
finally:
    GPIO.output(dac,clean)
    GPIO.cleanup()