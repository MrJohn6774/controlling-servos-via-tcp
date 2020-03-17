import pygame
import time
import logging
from collections import deque


pygame.init()
pygame.joystick.init()


class Gamepad:
    AILERON = 0
    ELEVATOR = 1
    YAW = 3
    #        RX       LY     LX
    m1 = [AILERON, ELEVATOR, YAW]  # mode 1
    m3 = [YAW, ELEVATOR, AILERON]  # mode 3
    m2 = [AILERON, 4, YAW]         # mode 2

    @staticmethod
    def quit():
        pygame.quit()

    @staticmethod
    def log(debug=logging.INFO):
        logging.basicConfig(level=debug)

    def __init__(self, mode, id=0):
        self.axes = deque(["Aileron", "Elevator", "Yaw"])
        self.conn()
        self.js = pygame.joystick.Joystick(id)
        self.js.init()
        self.axes.extendleft(mode)
        logging.debug(self.axes)
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
        logging.debug(f"Gamepad {self.axes[x+3]} Channel: {self.axes[x]}")
        logging.debug(f"Gamepad {self.axes[x+3]} Value: {self.js.get_axis(self.axes[x])}")
        if self.js.get_axis(self.axes[x]) < -0.06 or self.js.get_axis(self.axes[x]) > 0.06:
            return self.js.get_axis(self.axes[x])
        else:
            return 0
