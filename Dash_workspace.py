'''
    mimimum Value Project: A detection system for arrows on wheel
    detects if new arrow shot into empty spot
    Class - arrow
    1. arrow moves towards the wheel
    2. arrow hits the wheel
    3. check if overlap
    width of arrow head = 10
    speed of wheel
'''

import sys

import pygame
import pygame.locals

Width_Arrow_Head = 10
Speed_Wheel = 20 
Radius_Wheel = 200

def Wheel(radius, width, height, screen):
    pygame.draw.circle(screen, "#ff0000", (width/2, height/2 - radius), radius, 0)
    pygame.display.flip()
    return 

def Spin(Speed):
    return

def detection(Width_Arrows):
    return

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    width, height = 1000, 1000
    screen = pygame.display.set_mode((width, height))

    Wheel(Radius_Wheel, width, height, screen)

    while True:
        screen.fill("#000000")
        fps_clock.tick(fps)


if __name__ == "__main__":
    main()
