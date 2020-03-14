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


test()
