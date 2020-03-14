from Servo import Servo
import inputs


aileron_left = 11
aileron_right = 12
elevator = 15
rudder = 16
chan_list = [aileron_left, aileron_right, elevator, rudder]

Servo.initialize(chan_list)
aileron_left = Servo(chan_list[0], "Left Aileron")
aileron_right = Servo(chan_list[1], "Right Aileron")
elevator = Servo(chan_list[2], "Elevator")
rudder = Servo(chan_list[3], "Yaw")


def test():
    aileron_left.test(chan_list[0])
    aileron_right.test(chan_list[1])
    elevator.test(chan_list[2])
    rudder.test(chan_list[3])
    Servo.cleanup()                       # temporary for testing
    print("clean up")


def gamepad():
    while 1:  # Initial Device Connection Check
        try:
            event = inputs.get_gamepad()
        except(inputs.UnpluggedError):
            print("Warning: No device is found")
            print("wainting Device Connection...")
        else:
            break
    print("Loop exited")


test()
gamepad()
