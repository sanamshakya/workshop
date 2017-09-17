import RPi.GPIO as GPIO
import time

LED_PIN_1 = 22
LED_PIN_2 = 17
LED_PIN_3 = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1,GPIO.OUT)
GPIO.setup(LED_PIN_2,GPIO.OUT)
GPIO.setup(LED_PIN_3,GPIO.OUT)

time.sleep(1)

try:
	while(1):
		print "RED ON"
		GPIO.output(LED_PIN_1, True)
		GPIO.output(LED_PIN_2, False)
		GPIO.output(LED_PIN_3, False)
		time.sleep(4)
		print "Blue ON"
		GPIO.output(LED_PIN_2, True)
		GPIO.output(LED_PIN_1, False)
		GPIO.output(LED_PIN_3, False)
		time.sleep(4)
		print "Green ON"
		GPIO.output(LED_PIN_3, True)
		GPIO.output(LED_PIN_2, False)
		GPIO.output(LED_PIN_1, False)
		time.sleep(4)
		print "All off"
		GPIO.output(LED_PIN_1, False)
		GPIO.output(LED_PIN_2, False)
		GPIO.output(LED_PIN_3, False)
		time.sleep(2)

except KeyboardInterrupt:
	print "Keyboard Interrupt"
	GPIO.output(LED_PIN_1, False)
	GPIO.output(LED_PIN_2, False)
	GPIO.output(LED_PIN_3, False)
	GPIO.cleanup()
#try:
#	while(1):
#		print "Turning On"
#		GPIO.output(LED_PIN_1,True)
#		time.sleep(2)
#		GPIO.output(LED_PIN_2,True)
#		time.sleep(2)
#		GPIO.output(LED_PIN_3,True)
#		time.sleep(2)
#		print "Turning Off"
#		GPIO.output(LED_PIN_1,False)
#		GPIO.output(LED_PIN_2,False)
#		GPIO.output(LED_PIN_3,False)
#		time.sleep(2)
#except KeyboardInterrupt:
#	print "Keyboard Interrupt Occurred"
#	print "Closing script"		
#	GPIO.cleanup()
