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
center_x =450
center_y = 450
angle = 0
clock = pygame.time.Clock()
last_change = pygame.time.get_ticks()
pygame.display.set_caption("Needle Shooting Game")
background_color=(0,0,0)

current_speed = 0.3
target_speed = 1.0
last_speed_change =time.time()
transition_start_speed = 1.0
in_transition = False
sb=0

last_y_change =time.time()
in_transform = False

running = True
while running:
    current_time = time.time()
    
    if current_time - last_speed_change > 10 and not in_transition:
        target_speed = random.uniform(-1.0, 1.0)
        transition_start_speed = current_speed
        transition_start_time = current_time
        in_transition = True
        last_speed_change = current_time
    
    if in_transition:
        transition_progress = (current_time - transition_start_time) / 2.0
        if transition_progress >= 1.0:
            current_speed = target_speed
            in_transition = False
        else:
            current_speed = transition_start_speed + (target_speed - transition_start_speed) * transition_progress

    if current_time - last_y_change > 30 and not in_transform:
        in_transform = True
        last_y_change = current_time
        transform_start_time =current_time

    if in_transform:
        transform_progress = (current_time - transform_start_time)
        if transform_progress <= 2:
            sb = -0.2
        elif 2<transform_progress <= 6:
            sb = 0.2
        elif 6<transform_progress <= 8:
            sb = -0.2
        else:
            sb =0
            in_transform = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angle += current_speed
    center_y += sb
    rect = original_image.get_rect(center=(center_x, center_y))
    angle %= 360
    rotated_image = pygame.transform.rotate(original_image, -angle) 
    rotated_rect = rotated_image.get_rect(center=rect.center)

    screen.fill(background_color)
    screen.blit(rotated_image, rotated_rect.topleft)
    pygame.display.flip()

pygame.quit()
sys.exit()