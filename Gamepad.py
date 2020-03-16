import pygame
import time


pygame.init()
pygame.joystick.init()


class Gamepad:
    AILERON = 0
    ELEVATOR = 1
    YAW = 3
    AXES = [AILERON, ELEVATOR, YAW, "Aileron", "Elevator", "Yaw"]

    @staticmethod
    def quit():
        pygame.quit()

    def __init__(self, id=0):
        self.conn()
        self.js = pygame.joystick.Joystick(id)
        self.js.init()
        print("Debug: Device Connected. Id =", id)

    def conn(self):
        while pygame.joystick.get_count() == 0:
            print("Status: Waiting Device Connection")
            pygame.joystick.quit()
            time.sleep(0.2)
            pygame.joystick.init()
            time.sleep(1.8)

    def getPos(self, x):
        pygame.event.pump()
        print("DEBUG: Gamepad", Gamepad.AXES[x+3], "Channel:", Gamepad.AXES[x])
        print("DEBUG:", Gamepad.AXES[x+3], "input value:", self.js.get_axis(Gamepad.AXES[x]))
        if self.js.get_axis(Gamepad.AXES[x]) < -0.06 or self.js.get_axis(Gamepad.AXES[x]) > 0.06:
            return self.js.get_axis(Gamepad.AXES[x])
        else:
            return 0
