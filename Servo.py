import RPi.GPIO as gpio
import time


class Servo:
    def __init__(servo, pin, name):
        servo.pwm = gpio.PWM(pin, 50)
        servo.pin = pin
        servo.name = name

    def test(servo):
        servo.pwm.start(7)
        print(servo.name, " Neutral")
        time.sleep(0.3)
        servo.pwm.ChangeDutyCycle(2.7)
        print(servo.name, " Down")
        time.sleep(0.5)
        servo.pwm.ChangeDutyCycle(11.3)
        print(servo.name, " Up")
        time.sleep(0.8)
        servo.pwm.ChangeDutyCycle(7)
        print(servo.name, " Neutral")
        time.sleep(0.5)

    @staticmethod
    def cleanup():
        gpio.cleanup()

    @staticmethod
    def initialize(chan_list):
        gpio.cleanup
        gpio.setmode(gpio.BOARD)
        gpio.setup(chan_list, gpio.OUT)
