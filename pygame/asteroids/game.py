import pygame
import numpy as np
from constants import (
    GAME_DELTA_TIME,
    SCREEN_RESOLUTION,
    FPS,
    WHITE,
    BLACK,
    LIGHT_BLUE,
    LIGHT_BLACK,
    COOL_RED,
)


def end_game():
    pygame.quit()
    quit()


class Nave:
    def __init__(self, x, y, color):
        self.pos = np.array([x, y])
        self.size = 20
        self.speed = np.array([0, 0])
        self.color = color

    def move(self, player_dir):
        abs_speed = np.sum(np.absolute(self.speed))

        # Aceleracion
        if abs_speed < 5:
            self.speed = self.speed + player_dir * 0.5

        # Movimiento
        self.pos = self.pos + self.speed

        # Limites de pantalla.
        # En X
        if self.pos[0] < self.size:
            self.pos[0] = self.size
            self.speed[0] = 0
        elif self.pos[0] > SCREEN_RESOLUTION[0] - self.size:
            self.pos[0] = SCREEN_RESOLUTION[0] - self.size
            self.speed[0] = 0

        if self.pos[1] < self.size:
            self.pos[1] = self.size
            self.speed[1] = 0
        elif self.pos[1] > SCREEN_RESOLUTION[1] - self.size:
            self.pos[1] = SCREEN_RESOLUTION[1] - self.size
            self.speed[1] = 0

        # Desaceleracion
        if abs_speed != 0:
            self.speed = self.speed - self.speed / 10
            if abs_speed < 0.4:
                self.speed = [0, 0]

    def collision(self, other):
        escalar_distance = np.sum(np.absolute(self.pos - other.pos))
        print(escalar_distance)
        if escalar_distance <= (self.size + other.size):
            self.color = LIGHT_BLUE
            other.color = LIGHT_BLUE

    def draw(self):
        pygame.draw.circle(screen, self.color, self.pos.astype(int), self.size, 0)


# Init
pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
clock = pygame.time.Clock()  ## Syncing the FPS
font_name = pygame.font.match_font("arial")
screen_running = True
player = Nave(100, 100, WHITE)
player.draw()
enemy = Nave(SCREEN_RESOLUTION[0] * 0.5, SCREEN_RESOLUTION[1] * 0.5, COOL_RED)
enemy.draw()

pygame.display.update()

# Game loop
while True:
    clock.tick(FPS)
    screen.fill(LIGHT_BLACK)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end_game()

    key = pygame.key.get_pressed()

    player_dir = np.array([0, 0])
    if key[pygame.K_DOWN]:
        player_dir = player_dir + np.array([0, 1])

    if key[pygame.K_UP]:
        player_dir = player_dir + np.array([0, -1])

    if key[pygame.K_RIGHT]:
        player_dir = player_dir + np.array([1, 0])

    if key[pygame.K_LEFT]:
        player_dir = player_dir + np.array([-1, 0])

    # Draw
    player.move(player_dir)

    # Collisions
    player.collision(enemy)

    player.draw()
    enemy.draw()
    pygame.display.update()
