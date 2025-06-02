import sys
import pygame
import pygame.locals
import math
import random
import time
import os

pygame.font.init()


class PinNeedle:
    def __init__(self) -> None:
        self.fps = 60
        self.fps_clock = pygame.time.Clock()
        self.width, self.height = 800, 1000
        self.offset = 300
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.radius = 120
        self.BOW_POS = (400, 800)
        self.anglerate = 0.05
        self.clock = pygame.time.Clock()

    def draw_wheel(self):
        pygame.draw.circle(
            self.screen,
            "#650f0e",
            (self.width / 2, self.height / 2 - self.offset),
            self.radius,
            0,
        )
        pygame.display.flip()

    def make_bow_surface(self):
        surf = pygame.Surface((60, 120), pygame.SRCALPHA)
        pygame.draw.arc(
            surf, (139, 69, 19), (10, 10, 40, 100), 3.14 / 2, 3 * 3.14 / 2, 6
        )  # bow
        pygame.draw.line(surf, (255, 255, 255), (30, 10), (30, 110), 2)  # string
        pygame.draw.rect(surf, (240, 240, 240), (4, 0, 2, 40))  # shaft
        pygame.draw.polygon(surf, (180, 0, 0), [(2, 0), (8, 0), (5, -10)])  # tip
        return surf

    def run_game(self):
        bow_img = self.make_bow_surface()

        arrows = []
        bow_img = pygame.transform.rotate(bow_img, 270)

        self.draw_wheel()
        self.screen.blit(bow_img, bow_img.get_rect(center=self.BOW_POS))

        score = 0
        game_over = False
        speed_multiplier = 1

        current_level = 0
        level = ["Easy", "Medium", "Hard"]

        highscore = 0

        while True:
            dt = self.clock.tick(60) / 1000

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    # Shoot from bow position
                    arrows.append(Arrow(*self.BOW_POS))
                if e.type == pygame.KEYDOWN and game_over:
                    game_over = False
                    score = 0
                    arrows = []
                    speed_multiplier = 1
                    dt = self.clock.tick(60) / 1000
                    current_level = 0
                if e.type == pygame.KEYDOWN:
                    self.anglerate += 0.02
                    speed_multiplier *= 2
                    current_level += 1
                    if self.anglerate > 0.1:
                        self.anglerate = 0.05
                        speed_multiplier = 1
                        current_level = 0

            if game_over == False:
                for a in arrows:
                    a.update(
                        speed_multiplier * dt,
                        self.height,
                        self.width,
                        self.offset,
                        self.radius,
                        self.anglerate,
                    )

                self.screen.fill((30, 30, 40))
                self.draw_wheel()
                self.screen.blit(bow_img, bow_img.get_rect(center=self.BOW_POS))

                count = 0

                for a in arrows:
                    a.draw(self.screen)
                    if (
                        a.y <= (self.height / 2 - self.offset + self.radius)
                        and a.y >= (self.height / 2 - self.offset + self.radius) - 0.08
                    ):
                        count += 1
                    if (
                        a.y >= (self.height / 2 - self.offset + self.radius)
                        and a.y
                        <= (self.height / 2 - self.offset + self.radius)
                        + 0.000000000000001
                    ):
                        score += 1

                if count > 1:
                    score -= 1
                    game_over = True
                    if score > highscore:
                        highscore = score

            else:
                font = pygame.font.Font(None, 80)
                score_surf1 = font.render("GAME OVER", True, (255, 255, 255))
                score_surf2 = font.render(
                    "Press a button to Restart", True, (255, 255, 255)
                )
                self.screen.blit(score_surf1, (50, 400))
                self.screen.blit(score_surf2, (50, 500))
            font = pygame.font.Font(None, 18)
            score_surf3 = font.render(
                "Press a Key to Change Difficulty (Three Levels)", True, (255, 255, 255)
            )
            self.screen.blit(score_surf3, (20, 800))
            score_surf4 = font.render(
                f"Difficulty Level:  {level[current_level]}", True, (255, 255, 255)
            )
            self.screen.blit(score_surf4, (20, 780))
            font = pygame.font.Font(None, 42)
            score_surf = font.render(str(score), True, (255, 255, 255))
            self.screen.blit(score_surf, (self.width - 40, 30))
            score_surf5 = font.render(
                f"High Score:  {highscore}", True, (255, 255, 255)
            )
            self.screen.blit(score_surf5, (20, 30))
            pygame.display.flip()


width, height = 800, 1000
screen = pygame.display.set_mode((width, height))
original_image = pygame.image.load("circle.png").convert_alpha()
center_x, center_y = 400, 250
speed_x, speed_y = 0, 0
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

move_direction = 0
move_speed = 3
last_move_change = time.time()
next_change_interval = random.uniform(5, 10)

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

    if current_time - last_move_change > next_change_interval:
        move_direction = random.choice([-1, 0, 1])
        next_change_interval = random.uniform(5, 10)
        move_speed = random.uniform(0.2, 2)
        last_move_change = current_time

    center_y += move_direction * move_speed

    if center_x < 0:
        center_x = 0
    elif center_x > width:
        center_x = width
    if center_y < 0:
        center_y = 0
    elif center_y > 500:
        center_y = 500

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


class Arrow:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.arrow_length = 55
        self.x2, self.y2 = x, y + self.arrow_length
        self.speed = -600
        self.angle = -math.pi / 2

    def update(self, dt, height, width, offset, radius, anglerate):
        bottom = height / 2 - offset + radius
        center_x = width / 2
        center_y = height / 2 - offset
        if self.y > bottom:
            self.y += self.speed * dt
            self.y2 += self.speed * dt
        else:
            self.x = center_x - radius * math.cos(self.angle)
            self.y = center_y - radius * math.sin(self.angle)
            self.x2 = center_x - (self.arrow_length + radius) * math.cos(self.angle)
            self.y2 = center_y - (self.arrow_length + radius) * math.sin(self.angle)
            self.angle += anglerate

    def draw(self, surf):

        pygame.draw.line(surf, "#efeef1", (self.x, self.y), (self.x2, self.y2), width=5)


if __name__ == "__main__":
    Game = PinNeedle()
    Game.run_game()
