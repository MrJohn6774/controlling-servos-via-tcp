import pygame
import time
import sys
import timeout_decorator
""" def timeout(seconds=None,
                use_signals=True,
                timeout_exception=TimeoutError,
                exception_message=None)
"""


pygame.init()
pygame.joystick.init()


class Gamepad:
    AILERON = 0
    ELEVATOR = 1
    YAW = 3

    @staticmethod
    def quit():
        pygame.quit()
        sys.exit()

    def __init__(self, id=0):
        self.conn()
        self.joystick = pygame.joystick.Joystick(id)
        self.joystick.init()
        print("Debug: Device Connected. Id =", id)

    def conn(self):
        while pygame.joystick.get_count() == 0:
            print("Status: Waiting Device Connection")
            pygame.joystick.quit()
            time.sleep(0.2)
            pygame.joystick.init()
            time.sleep(1.8)

    def getAileron(self):
        if self.joystick.get_axis(Gamepad.AILERON) < -0.06 or self.joystick.get_axis(Gamepad.AILERON) > 0.06:
            return self.joystick.get_axis(Gamepad.AILERON)
