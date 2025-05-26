import turtle
import sys
import tkinter as tk
import pygame
import pygame.locals
import math

'''
minimum viable project:
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
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Needle Shooting Game")

center = (450, 450)
radius = 150
center_color = (255, 0, 255) 
edge_color = (0, 0, 255)      

# Game loop.
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

# Event loop to keep the window open
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
    