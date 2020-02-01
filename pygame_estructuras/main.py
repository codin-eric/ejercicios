"""
Grafiquemos cada una de las estructuras vistas en la serie de 
programación orientada a objetos!

Realicemos las siguientes acciones:
- Agregar
- Quitar
- Buscar
"""

import pygame
from random import randint
from estructuras import Lista, Pila, BTree

# Constants
SCREEN_RESOLUTION = (1280, 720)
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Init
pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
clock = pygame.time.Clock()  ## Syncing the FPS
font_name = pygame.font.match_font("arial")
screen_running = True


# Kill the game
def end_game():
    pygame.quit()
    quit()


listita = Lista(30, SCREEN_RESOLUTION[0] * 0.25)
listita.agregar(5)
listita.draw(screen)
pygame.display.update()

# Game loop
while screen_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end_game()

            if event.key == pygame.K_t:
                screen.fill(BLACK)
                listita.agregar(randint(1, 100))
                listita.draw(screen)
                pygame.display.update()

            if event.key == pygame.K_p:
                screen.fill(BLACK)
                valor = listita.pop()
                print(valor)
                listita.draw(screen)
                pygame.display.update()

