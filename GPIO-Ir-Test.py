import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)
from time import sleep
GPIO.setup(24, GPIO.OUT)

try:
	while True:
		if GPIO.input(25)==1:
			print("Wait, I see something")
		else:
			print("Go.. ")
		sleep(0.1)
finally:
	GPIO.cleanup()
