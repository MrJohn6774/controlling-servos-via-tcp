# import inputs
import time
import timeout_decorator
from Servo import Servo


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

@timeout_decorator.timeout(5)
def gamepad():
    while 1:  # Initial Device Connection Check
        print("Debug: Prepare to import inputs")
        import inputs
        print("Debug: Inputs imported")
        try:
            event = inputs.get_gamepad()
        except(inputs.UnpluggedError):
            print("Warning: No device is found")
            print("Status: Waiting Device Connection...")
            del inputs
            time.sleep(3)
        except(IOError):
            print("Warning: Device connection lost")
            print("Status: Waiting Device Connection...")
            del inputs
            time.sleep(3)
        else:
            break
    print("Status: Device connected")
    Servo.cleanup()
    return True


while 1:
    try:
        gamepad()
    except(timeout_decorator.TimeoutError):
        print("Warning: No data is received")
        print("Check device is turned on and connected")
        continue
    else:
        break
