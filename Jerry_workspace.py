import turtle
import sys
import tkinter as tk
import pygame
import pygame.locals
import math
import random
import time

"""minimum viable project:
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
"""

pygame.init()
fps = 240
fpsClock = pygame.time.Clock()
width, height = 900, 900
picture = "circle.png"
screen = pygame.display.set_mode((width, height))
original_image = pygame.image.load(picture).convert_alpha()
center_x, center_y = 450, 450
speed_x, speed_y= 0, 0
angle = 0
clock = pygame.time.Clock()
last_change = pygame.time.get_ticks()
pygame.display.set_caption("Needle Shooting Game")
background_color = (0, 0, 0)

current_speed = 0.3
target_speed = 1.0
last_speed_change = time.time()
transition_start_speed = 1.0
in_transition = False

# 上下运动控制变量
center_x, center_y = 450, 450
move_direction = 0  # 0表示不移动，1表示向上，-1表示向下
move_speed = 3  # 移动速度
last_move_change = time.time()
next_change_interval = random.uniform(5, 10)  # 首次变化间隔

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
            current_speed = (
                transition_start_speed
                + (target_speed - transition_start_speed) * transition_progress
            )
    ###
    # 随机上下运动控制
    if current_time - last_move_change > next_change_interval:
        move_direction = random.choice([-1, 0, 1])  # 随机选择方向
        next_change_interval = random.uniform(5, 10)  # 设置下次变化间隔
        move_speed = random.uniform(1, 3)  # 设置下次变化间隔
        last_move_change = current_time

    # 更新Y轴位置
    center_y += move_direction * move_speed

    # 限制图片不超出屏幕边界
    if center_x < 0:
        center_x = 0
    elif center_x > width:
        center_x = width
    if center_y < 0:
        center_y = 0
    #elif center_y > height - original_image.get_height():
    #    center_y = height - original_image.get_height()
    elif center_y > height:
        center_y = height

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angle += current_speed
    center_y += speed_y
    rect = original_image.get_rect(center=(center_x, center_y))
    angle %= 360
    rotated_image = pygame.transform.rotate(original_image, -angle)
    rotated_rect = rotated_image.get_rect(center=rect.center)

    screen.fill(background_color)
    screen.blit(rotated_image, rotated_rect.topleft)
    pygame.display.flip()

pygame.quit()
sys.exit()
