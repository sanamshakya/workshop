import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servo1 = 23         # pin 16
servo2 = 24         # pin 18

GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)

p = GPIO.PWM(servo1,50)
p1 = GPIO.PWM(servo2,50)

p.start(7.5)
p1.start(7.5)
time.sleep(1)
try:
	while(1):
		p.ChangeDutyCycle(7.5)		#90 degeree
		time.sleep(1)
                p1.ChangeDutyCycle(7.5)
                time.sleep(1)
		p.ChangeDutyCycle(2.5)		#0 degree
		time.sleep(1)
                p1.ChangeDutyCycle(2.5)
                time.sleep(1)
		p.ChangeDutyCycle(12.5)		#180 degree
		time.sleep(1)
                p1.ChangeDutyCycle(12.5)
                time.sleep(1)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()

