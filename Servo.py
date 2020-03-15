import RPi.GPIO as gpio
import time


class Servo:
    def __init__(servo, pin, name):
        servo.pwm = gpio.PWM(pin, 50)
        servo.pin = pin
        servo.name = name
        servo.pwm.start(7)

    def test(servo):
        servo.pwm.ChangeDutyCycle(7)
        print("Debug:", servo.name, "Position: Neutral")
        time.sleep(0.3)
        servo.pwm.ChangeDutyCycle(2.7)
        print("Debug:", servo.name, "Position: Down")
        time.sleep(0.5)
        servo.pwm.ChangeDutyCycle(11.3)
        print("Debug:", servo.name, "Position: Up")
        time.sleep(0.8)
        servo.pwm.ChangeDutyCycle(7)
        print("Debug:", servo.name, "Position: Neutral")
        time.sleep(0.5)

    def move(servo, gp_pos):
        x = gp_pos
        dc = 7
        if x < -0.06:
            dc = 4.3/0.94*(x+1)+2.7
        elif x > 0.06:
            dc = 4.3/0.94*(x-0.06)+7
        servo.pwm.ChangeDutyCycle(dc)

    @staticmethod
    def cleanup():
        gpio.cleanup()

    @staticmethod
    def initialize(chan_list):
        gpio.cleanup
        gpio.setmode(gpio.BOARD)
        gpio.setup(chan_list, gpio.OUT)
