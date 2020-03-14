import inputs
import time
import timeout_decorator
""" def timeout(seconds=None,
                use_signals=True,
                timeout_exception=TimeoutError,
                exception_message=None)
"""
from importlib import reload
from Servo import Servo


aileron_left = 11
aileron_right = 12
elevator = 15
rudder = 16
chan_list = [aileron_left, aileron_right, elevator, rudder]
event = None

Servo.initialize(chan_list)
aileron_left = Servo(chan_list[0], "Left Aileron")
aileron_right = Servo(chan_list[1], "Right Aileron")
elevator = Servo(chan_list[2], "Elevator")
rudder = Servo(chan_list[3], "Yaw")


def test():
    aileron_left.test()
    aileron_right.test()
    elevator.test()
    rudder.test()
    Servo.cleanup()                       # temporary for testing
    print("clean up")


@timeout_decorator.timeout(5)
def gamepad_conn():                       # Initialize Device Connection
    print("Debug: Prepare to import inputs")
    import inputs
    print("Debug: Inputs imported")
    while 1:
        try:
            global event
            event = inputs.get_gamepad()
        except(inputs.UnpluggedError):
            print("Warning: No device is found")
            print("Status: Waiting Device Connection...")
            time.sleep(3)
            inputs = reload(inputs)
        except(IOError):
            print("Warning: Device connection lost")
            print("Status: Waiting Device Connection...")
            time.sleep(3)
            inputs = reload(inputs)
        else:
            break
    print("Status: Device connected")


test()


while 1:
    try:
        gamepad_conn()
    except(timeout_decorator.TimeoutError):
        print("Warning: No data is received")
        print("Check device is turned on and connected")
        time.sleep(2)
    else:
        break
