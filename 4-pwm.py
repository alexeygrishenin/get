import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)

p = GPIO.PWM(22,1000)
p.start(0)
try:
    while(1):
        a = int(input("Введите коэффициент"))
        p.start(a)
        input("press return to stop")
        p.stop()
finally:
    GPIO.cleanup()