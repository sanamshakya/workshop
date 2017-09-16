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
		print "ON"
		print "Press ctrl+c to stop"
		GPIO.output(LED_PIN_1, True)
		GPIO.output(LED_PIN_2, False)
		GPIO.output(LED_PIN_3, False)
		time.sleep(4)
		print "ON"
		print "Press ctrl+c to stop"
		GPIO.output(LED_PIN_2, True)
		GPIO.output(LED_PIN_1, False)
		GPIO.output(LED_PIN_3, False)
		time.sleep(4)
		print "ON"
		print "Press ctrl+c to stop"
		GPIO.output(LED_PIN_3, True)
		GPIO.output(LED_PIN_2, False)
		GPIO.output(LED_PIN_1, False)
		time.sleep(4)
		print "All off"
		print "Press ctrl+c to stop"
		GPIO.output(LED_PIN_1, False)
		GPIO.output(LED_PIN_2, False)
		GPIO.output(LED_PIN_3, False)
		time.sleep(2)

except KeyboardInterrupt:
	print "Keyboard Interrupt - Turning off LEDs"
	GPIO.output(LED_PIN_1, False)
	GPIO.output(LED_PIN_2, False)
	GPIO.output(LED_PIN_3, False)
	GPIO.cleanup()
