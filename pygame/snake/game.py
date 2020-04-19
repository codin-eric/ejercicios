import pygame
import numpy as np
from assets.basics import Snake, Food
from assets.constants import (
    GAME_DELTA_TIME,
    SCREEN_RESOLUTION,
    FPS,
    WHITE,
    BLACK,
    LIGHT_BLUE,
    LIGHT_BLACK,
    COOL_RED,
    DERECHA,
    IZQUIERDA,
    ARRIBA,
    ABAJO,
)


def end_game():
    pygame.quit()
    quit()


# Init
pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
clock = pygame.time.Clock()  # Syncing the FPS
vibo = Snake(120, 120)
la_comi = Food()

# Game loop
while True:
    clock.tick(FPS)
    screen.fill(LIGHT_BLACK)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end_game()

            if event.key == pygame.K_DOWN:
                vibo.set_dir(ABAJO)
            if event.key == pygame.K_UP:
                vibo.set_dir(ARRIBA)
            if event.key == pygame.K_LEFT:
                vibo.set_dir(IZQUIERDA)
            if event.key == pygame.K_RIGHT:
                vibo.set_dir(DERECHA)

    # Colission
    vibo.colission(la_comi)
    # Movement
    vibo.move()

    # Draw
    vibo.draw(screen)
    la_comi.draw(screen)
    pygame.display.update()
