import RPi.GPIO as gpio
import time


class Servo:
    def __init__(servo, pin, name):
        servo.pwm = gpio.PWM(pin, 50)
        servo.name = name

    def test(servo, pin):
        servo.pwm.start(7)
        print("Pin ", servo.name, " Neutral")
        time.sleep(0.5)
        servo.pwm.ChangeDutyCycle(2.7)
        print("Left ", servo.name, " Down")
        time.sleep(1.5)
        servo.pwm.ChangeDutyCycle(11.3)
        print("Left ", servo.name, " Up")
        time.sleep(1.5)
        servo.pwm.ChangeDutyCycle(7)
        print("Left ", servo.name, " Neutral")
        time.sleep(2)

    @staticmethod
    def cleanup():
        gpio.cleanup()

    @staticmethod
    def initialize(chan_list):
        gpio.cleanup
        gpio.setmode(gpio.BOARD)
        gpio.setup(chan_list, gpio.OUT)
