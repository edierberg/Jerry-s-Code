import sys
import pygame
import pygame.locals
import math
import random

Width_Arrow_Head = 10
Speed_Wheel = 20 
Radius_Wheel = 150
clock  = pygame.time.Clock()

#todo: finish integration, organize, and make rotate

#Wheel
def Wheel(radius, width, height, screen):
    #pygame.draw.circle(screen, "#ff0000", (width/2, height/2 - 300), radius, 0)
    pygame.display.flip()
    return 

#shooter
def make_arrow_surface():
    surf = pygame.Surface((10, 40), pygame.SRCALPHA)
    pygame.draw.rect(surf, (240, 240, 240), (4, 0, 2, 40))        # shaft
    pygame.draw.polygon(surf, (180, 0, 0), [(2, 0), (8, 0), (5, -10)])  # tip
    return surf

def make_bow_surface():
    surf = pygame.Surface((60, 120), pygame.SRCALPHA)
    pygame.draw.arc(surf, (139,69,19), (10, 10, 40, 100), 3.14/2, 3*3.14/2, 6)  # bow
    pygame.draw.line(surf, (255,255,255), (30, 10), (30, 110), 2)               # string
    pygame.draw.rect(surf, (240, 240, 240), (4, 0, 2, 40))        # shaft
    pygame.draw.polygon(surf, (180, 0, 0), [(2, 0), (8, 0), (5, -10)])  # tip

    return surf

def Detection(Width_Arrows):
    # check position of arrowead 
    return

def main():
    fps = 60
    fps_clock = pygame.time.Clock()
    width, height = 1000, 1000
    screen = pygame.display.set_mode((width, height))
    center = (width - 500, 200)
    radius = 150
    x, y, z, a, b, c = 0,0,255,255,0,255
    center_color = (a, b, c) 
    edge_color = (x, y, z)
    screen.fill("#000000")
    
    arrow_img = make_arrow_surface()
    bow_img = make_bow_surface()

    class Arrow:
        def __init__(self, x, y):
            self.x, self.y = x, y
            self.speed = -600

        def update(self, dt):
            self.y += self.speed * dt

        def draw(self, surf):
            surf.blit(arrow_img, arrow_img.get_rect(center=(self.x, self.y)))

    arrows = []
    BOW_POS = (500, 500)
    bow_img = pygame.transform.rotate(bow_img, 270)

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

    while True:
        #Spin()
        #Detection()
        fps_clock.tick(fps)
        dt = clock.tick(60) / 1000  # seconds/frame

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                # Shoot from bow position
                arrows.append(Arrow(*BOW_POS))

        for a in arrows:
            a.update(dt)

        screen.blit(bow_img, bow_img.get_rect(center=BOW_POS))

        for a in arrows:
            a.draw(screen)
        
        pygame.display.flip()
        
if __name__ == "__main__":
    main()
