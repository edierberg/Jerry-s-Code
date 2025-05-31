'''
Evan's workspace.

May 20: Shooting Mechanism (upon pressing key, bow releases arrow at constant velocity at wheel)

May 23: Incorporate with rest of project

May 26: Lives or chances (game can restart and show previous high scores) - - incorporated

May 29: Modulate speed of wheel spinning - - incorporated
    -increase/decrease speed of nob
    - ties in with the difficulty settings) 

    -> Also consider obstacles for shooters (birds, clouds, etc...)

June 2: Final done, with as many nice to haves as possible incorporated

Shooting Mechanism 
    bow
        stationary at bottom of screen
            - create pygame art for this
            -position it
    arrow
        arrowhead placed at tip of bow
            - create pygame art for arrow
            - position it
        upon click/press key, one arrow fires at wheel w constant v
            - velocity vector
        as soon as arrow hits wheel, next arrow loaded in same spot
        stop kinematics for arrow once hits the wheel
        stick the arrow to the wheel by reorienting it in polar coordinates/rotation around a fixed center
'''
import pygame, sys
pygame.init()

width, height = 600, 700
screen = pygame.display.set_mode((width, height))
clock  = pygame.time.Clock()

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
bow_pos = (width//2, height - 80)
bow_img = pygame.transform.rotate(bow_img, 270)

while True:
    dt = clock.tick(60) / 1000  # seconds/frame

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            # Shoot from bow position
            arrows.append(Arrow(*bow_pos))

    for a in arrows:
        a.update(dt)

    screen.fill((30,30,40))
    screen.blit(bow_img, bow_img.get_rect(center=bow_pos))

    for a in arrows:
        a.draw(screen)

    pygame.display.flip()
