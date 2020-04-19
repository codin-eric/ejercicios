import numpy as np
import pygame
from random import randint
from assets.constants import (
    SCREEN_RESOLUTION,
    WHITE,
    COOL_RED,
    COMPLEMENTARY_RED,
    DERECHA,
    IZQUIERDA,
    ARRIBA,
    ABAJO,
)


class Food:
    def __init__(self):
        self.size = 40
        self.color = COOL_RED
        self.set_pos()

    def set_pos(self):
        x = randint(1, int(SCREEN_RESOLUTION[0]-self.size)/self.size)
        y = randint(1, int(SCREEN_RESOLUTION[1]-self.size)/self.size)

        self.pos = np.array([x, y]) * self.size

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.pos, int(self.size/2), 0)


class Snake:
    def __init__(self, x, y):
        self.pos = np.array([x, y])
        self.size = 40
        self.color = WHITE
        self.dir = np.array(DERECHA)
        self.body = None

    def set_dir(self, new_dir):
        if not np.array_equal(np.array(new_dir), -self.dir):
            self.dir = np.array(new_dir)

    def move(self):
        if self.body:
            self.body.move(self.pos)
        self.pos = self.pos + self.dir * self.size

    def add_body(self):
        if self.body:
            self.body.add_body()
        else:
            self.body = SnakeBody(self.color, self.size)

    def colission(self, other):
        if np.array_equal(self.pos, other.pos):
            self.add_body()
            other.set_pos()

    def draw(self, screen):
        if self.body:
            self.body.draw(screen)
        pygame.draw.circle(screen, self.color, self.pos, int(self.size/2), 0)


class SnakeBody:
    def __init__(self, color, size):
        self.size = size
        self.color = color
        self.next = None

    def move(self, new_pos):
        if self.next:
            self.next.move(self.pos)
        self.pos = new_pos

    def add_body(self):
        if self.next:
            self.next.add_body()
        else:
            self.next = SnakeBody(self.color, self.size)

    def draw(self, screen):
        if self.next:
            self.next.draw(screen)
        pygame.draw.circle(screen, self.color, self.pos, int(self.size/2), 0)
