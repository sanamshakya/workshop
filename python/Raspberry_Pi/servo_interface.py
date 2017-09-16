## This code is meant to test micro servo interfaced on Raspberry Pi

## Connect Pan Servo to S1 pin and Tilt servo to S2 pin
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
servo1 = 23     # pin 16 - S1 pin
servo2 = 24     # pin 18 - S2 pin

GPIO.setup(servo1,GPIO.OUT)
GPIO.setup(servo2,GPIO.OUT)

p = GPIO.PWM(servo1,50)    # Generating Software PWM of 50 HZ for S1 pin 
p1 = GPIO.PWM(servo2,50)	# Generating Software PWM of 50 HZ for S2 pin

p.start(7.5)
p1.start(7.5)
time.sleep(1)
try:
	while(1):
		p.ChangeDutyCycle(7.5)			#90 degeree
		time.sleep(1)
                p1.ChangeDutyCycle(7.5) #90 degeree
                time.sleep(1)
		p.ChangeDutyCycle(2.5)			#0 degree
		time.sleep(1)
                p1.ChangeDutyCycle(2.5) #0 degeree
                time.sleep(1)
		p.ChangeDutyCycle(12.5)			#180 degree
		time.sleep(1)
                p1.ChangeDutyCycle(12.5)#180 degeree
                time.sleep(1)
except KeyboardInterrupt:
	p.stop()
	p1.stop()
	GPIO.cleanup()

