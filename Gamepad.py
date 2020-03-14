import pygame
import time
import sys
import timeout_decorator
""" def timeout(seconds=None,
                use_signals=True,
                timeout_exception=TimeoutError,
                exception_message=None)
"""

pygame.joystick.init()


class Gamepad:

    @staticmethod
    def quit():
       pygame.quit()
       sys.exit()

    def __init__ (self, id=0):
        self.conn()
        self.joystick = pygame.joystick.Joystick(id)
        self.joystick.init()
        print("Debug: Device Connected. Id =", id)

    def conn(self):
        while pygame.joystick.get_count() == 0:
            s = int(time.time())
            print("Status: Waiting Device Connection")
            pygame.joystick.quit()
            time.sleep(0.2)
            pygame.joystick.init()
            time.sleep(1.8)
