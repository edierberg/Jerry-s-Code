import sys
import pygame
import pygame.locals
import math
import random

class PinNeedle:
    def __init__(self) -> None:
        self.fps = 60
        self.fps_clock = pygame.time.Clock()
        self.width, self.height = 800, 1000
        self.offset = 300
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.radius = 120
        self.BOW_POS = (400, 800)
        self.clock = pygame.time.Clock()

    def draw_wheel(self):
        pygame.draw.circle(self.screen, "#f30a0a", (self.width/2, self.height/2 - self.offset), self.radius, 0)
        pygame.display.flip()

    def make_bow_surface(self):
        surf = pygame.Surface((60, 120), pygame.SRCALPHA)
        pygame.draw.arc(surf, (139,69,19), (10, 10, 40, 100), 3.14/2, 3*3.14/2, 6)  # bow
        pygame.draw.line(surf, (255,255,255), (30, 10), (30, 110), 2)               # string
        pygame.draw.rect(surf, (240, 240, 240), (4, 0, 2, 40))        # shaft
        pygame.draw.polygon(surf, (180, 0, 0), [(2, 0), (8, 0), (5, -10)])  # tip
        return surf

    def detection(self, arrows):
        for index in range(len(arrows)-1): 
            print("list 1")
            if arrows[-1].arrowrect.colliderect(arrows[index].arrowrect) == True:
                print("list 2")
                return print("womp womp")
            else:
                print("lsit 3")
                return 

    def run_game(self):
        bow_img = self.make_bow_surface()

        arrows = []
        bow_img = pygame.transform.rotate(bow_img, 270)

        self.draw_wheel()
        self.screen.blit(bow_img, bow_img.get_rect(center=self.BOW_POS))

        while True:
            #Spin()
            #Detection()
            self.fps_clock.tick(self.fps)
            dt = self.clock.tick(60) / 1000  # seconds/frame

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    # Shoot from bow position
                    arrows.append(Arrow(*self.BOW_POS))

            for a in arrows:
                a.update(dt, self.height, self.width, self.offset, self.radius)
            if arrows:
                self.detection(arrows)
            self.screen.fill((30,30,40))
            self.draw_wheel()
            self.screen.blit(bow_img, bow_img.get_rect(center=self.BOW_POS))
            #pygame.time.wait(100)
            for a in arrows:
                a.draw(self.screen)
            
            pygame.display.flip()
        
class Arrow:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.speed = -600
        self.angle = -math.pi/2
        self.width = 10
        self.surf = pygame.Surface((self.width, 40), pygame.SRCALPHA)
        self.surf.fill((240, 240, 240))
        # pygame.draw.rect(self.surf, (240, 240, 240), (4, 0, 2, 40))        # shaft
        # pygame.draw.polygon(self.surf, (180, 0, 0), [(2, 0), (8, 0), (5, -10)])  # tip
        self.arrowrect = self.surf.get_rect(topleft=(self.x, self.y))
        #bself.arrowrect = pygame.Rect(self.x, self.y, 10, 40)
    
    def update(self, dt, height, width, offset, radius):
        bottom = height/2 - offset + radius
        center_x = width/2
        center_y = height/2 - offset
        if self.arrowrect.y > bottom:
            self.arrowrect.y += self.speed * dt
        else:
            self.arrowrect.x = center_x - radius*math.cos(self.angle) - self.width/2
            self.arrowrect.y = center_y - radius*math.sin(self.angle)
            self.angle += 0.1
            self.surf = pygame.transform.rotate(self.surf, self.angle)



    def draw(self, surf):
        #surf.blit(self.surf, self.surf.get_rect(center=(self.x, self.y)))
        pygame.draw.rect(surf, (240, 240, 240), self.arrowrect)

if __name__ == "__main__":
    Game = PinNeedle()
    Game.run_game()
