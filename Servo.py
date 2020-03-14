import RPi.GPIO as gpio
import time


class Servo:
    def __init__(servo, servopin):
        servo.pwm = gpio.PWM(servopin, 50)

    def test(self, servopin):
        pwm = gpio.PWM(servopin, 50)
        pwm.start(7)
        print("Pin ", servopin, " Neutral")
        time.sleep(0.5)
        pwm.ChangeDutyCycle(2.7)
        print("Left ", servopin, " Down")
        time.sleep(1.5)
        pwm.ChangeDutyCycle(11.3)
        print("Left ", servopin, " Up")
        time.sleep(1.5)
        pwm.ChangeDutyCycle(7)
        print("Left ", servopin, " Neutral")
        time.sleep(2)
        gpio.cleanup()
        print("cleanup")
