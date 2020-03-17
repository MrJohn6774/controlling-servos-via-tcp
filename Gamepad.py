import pygame
import time
import logging
from collections import deque


logging.basicConfig(level=logging.INFO)
pygame.init()
pygame.joystick.init()


class Gamepad:
    AILERON = 0
    ELEVATOR = 1
    YAW = 3
    AXES = deque(["Aileron", "Elevator", "Yaw"])
    #        RX       LY     LX
    m1 = [AILERON, ELEVATOR, YAW]  # mode 1
    m3 = [YAW, ELEVATOR, AILERON]  # mode 3
    m2 = [AILERON, 4, YAW]         # mode 2

    @staticmethod
    def quit():
        pygame.quit()

    @staticmethod
    def log(debug):
        logging.basicConfig(level=debug)

    def __init__(self, id=0, mode=m3):
        self.conn()
        self.js = pygame.joystick.Joystick(id)
        self.js.init()
        Gamepad.AXES.deque.extendleft(Gamepad.mode)
        logging.info("Device Connected. Id = %s" % id)

    def conn(self):
        while pygame.joystick.get_count() == 0:
            logging.info("Waiting Device Connection")
            pygame.joystick.quit()
            time.sleep(0.2)
            pygame.joystick.init()
            time.sleep(1.8)

    def getPos(self, x):
        pygame.event.pump()
        logging.debug(f"Gamepad {Gamepad.AXES[x+3]} Channel: {Gamepad.AXES[x]}")
        logging.debug(f"Gamepad {Gamepad.AXES[x+3]} Value: {self.js.get_axis(Gamepad.AXES[x])}")
        if self.js.get_axis(Gamepad.AXES[x]) < -0.06 or self.js.get_axis(Gamepad.AXES[x]) > 0.06:
            return self.js.get_axis(Gamepad.AXES[x])
        else:
            return 0
