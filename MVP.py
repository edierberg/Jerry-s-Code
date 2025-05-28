import sys
import pygame
import pygame.locals
import math
import random

Width_Arrow_Head = 10
Speed_Wheel = 20 
Radius_Wheel = 150

def Wheel(radius, width, height, screen):
    #pygame.draw.circle(screen, "#ff0000", (width/2, height/2 - 300), radius, 0)
    pygame.display.flip()
    return 

def Wheel_Spin(screen):
    #Wheel spin 
    return

def Detection(Width_Arrows):
    # check position of arrowead 
    return

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    width, height = 1000, 1000
    screen = pygame.display.set_mode((width, height))
    center = (450, 450)
    radius = 150
    x, y, z, a, b, c = 0,0,255,255,0,255
    center_color = (a, b, c) 
    edge_color = (x, y, z)

    Wheel(Radius_Wheel, width, height, screen)

    for y in range(center[1] - radius, center[1] + radius):
        for x in range(center[0] - radius, center[0] + radius):
            dx = x - center[0]
            dy = y - center[1]
            distance = math.sqrt(dx**2 + dy**2)
            if distance <= radius:
                t = distance / radius
                color = tuple(int(center_color[i] + (edge_color[i] - center_color[i]) * t) for i in range(3))
                screen.set_at((x, y), color)

    pygame.display.flip()

    while True:
        screen.fill("#000000")
        #Spin()
        #Detection()
        fps_clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
