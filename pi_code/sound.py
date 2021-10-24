import RPi.GPIO as GPIO
import time

PIN = 32


GPIO.setmode(GPIO.BOARD)

GPIO.setup(PIN, GPIO.OUT)

pwm = GPIO.PWM(PIN, 440)
pwm.start(50)
time.sleep(1)
pwm.stop()

pwm = GPIO.PWM(PIN, 261)
pwm.start(50)
time.sleep(1)
pwm.stop()
