import pygame
import sys
from time import sleep
import time

pygame.init()
pygame.joystick.init()


# Waiting gamepad connection
while pygame.joystick.get_count() == 0:
    s = int(time.time())
    print("Status: Waiting Device Connection")
    pygame.joystick.quit()
    sleep(0.2)
    pygame.joystick.init()
    sleep(1.8)

# how many joysticks connected to computer?
joystick_count = pygame.joystick.get_count()
print("There is ", str(joystick_count), " joystick/s")

# initialise joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

axes = joystick.get_numaxes()
buttons = joystick.get_numbuttons()
hats = joystick.get_numhats()

print("There is ", str(axes), " axes")
print("There is ", str(buttons), " button/s")
print("There is ", str(hats), " hat/s")


def getAxis(number):
    # when nothing is moved on an axis, the VALUE IS NOT EXACTLY ZERO
    # so this is used not "if joystick value not zero"
    if number == 2 or number == 5:
        if joystick.get_axis(number) > -1:
            print("Axis value is", joystick.get_axis(number))
            print("Axis ID is", number)
    elif joystick.get_axis(number) < -0.06 or joystick.get_axis(number) > 0.06:
        print("Axis value is", joystick.get_axis(number))
        print("Axis ID is", number)


def getButton(number):
    # returns 1 or 0 - pressed or not
    if joystick.get_button(number):
        # just prints id of button
        print("Button ID is ", number)


def getHat(number):
    if joystick.get_hat(number) != (0, 0):
        # returns tuple with values either 1, 0 or -1
        print("Hat value is ", joystick.get_hat(number)[0], joystick.get_hat(number)[1])
        print("Hat ID is", number)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if buttons != 0:
                    for i in range(buttons):
                        getButton(i)
            if event.type == pygame.JOYAXISMOTION:
                if axes != 0:
                    for i in range(axes):
                        getAxis(i)
            if event.type == pygame.JOYHATMOTION:
                if hats != 0:
                    for i in range(hats):
                        getHat(i)
        sleep(0.1)


try:
    main()
except(KeyboardInterrupt):
    pygame.quit()
    sys.exit()
    print("Stopped")
