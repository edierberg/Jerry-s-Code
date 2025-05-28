import turtle
import sys
import tkinter as tk
import pygame
import pygame.locals
import math
import random
import time

'''minimum viable project:
Spinning Wheel (wheel spinning around fixed point) 

Nice to have:
Graphics Jerry/Evan/Dash
a. Cool images for wheel and shooting mechanism
Background Jerry
a. Visual enhancement
More complicated mechanism Jerry
a. Pull back e\ects
b. More detailed graphics
Lives or chances Jerry/Evan/Dash
a. Can restart and shows high scores
'''

pygame.init()
fps = 240
fpsClock = pygame.time.Clock()
width, height = 900, 900 
picture = "circle.png"
screen = pygame.display.set_mode((width, height))
original_image = pygame.image.load(picture).convert_alpha()
rect = original_image.get_rect(center=(450, 450))
angle = 0
clock = pygame.time.Clock()
last_change = pygame.time.get_ticks()
pygame.display.set_caption("Needle Shooting Game")
background_color=(0,0,0)
speed = 0.3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    current_time = pygame.time.get_ticks()
    if current_time - last_change >= 3000:
        speed = random.uniform(-0.8, 0.8)
        last_update = current_time

    angle += speed
    angle %= 360
    rotated_image = pygame.transform.rotate(original_image, -angle) 
    rotated_rect = rotated_image.get_rect(center=rect.center)

    screen.fill(background_color)
    screen.blit(rotated_image, rotated_rect.topleft)
    pygame.display.flip()

pygame.quit()
sys.exit()