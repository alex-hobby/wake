from flask import Flask
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# Modify this if you have a different sized character LCD
lcd_columns = 16
lcd_rows = 2

# compatible with all versions of RPI as of Jan. 2019
# v1 - v3B+
lcd_rs = digitalio.DigitalInOut(board.D22)
lcd_en = digitalio.DigitalInOut(board.D17)
lcd_d4 = digitalio.DigitalInOut(board.D25)
lcd_d5 = digitalio.DigitalInOut(board.D24)
lcd_d6 = digitalio.DigitalInOut(board.D23)
lcd_d7 = digitalio.DigitalInOut(board.D18)


# Initialise the lcd class
lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                      lcd_d7, lcd_columns, lcd_rows)
app = Flask(__name__)

PIN = 12

GPIO.setup(PIN, GPIO.OUT)
pwm = GPIO.PWM(PIN, 440)


@app.route('/sleeping/<int:asleep>')
def asleep_check(asleep):
    if asleep:
        lcd.clear()
        lcd.message = "You need rest!\nPull over now"
        pwm.start(50)
    else:
        pwm.stop()
    return str(asleep)


if __name__ == '__main__':
    lcd.message = "Keep on driving"
    app.run(host='10.136.7.139', debug=False)
