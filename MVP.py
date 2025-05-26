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

    Wheel(Radius_Wheel, width, height, screen)

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
