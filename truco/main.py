"""
Reglas del juego:
    Init:
        - Se crea el mazo
        - Los jugadores agarran 3 cartas
    primer turno:
        - p1 puede cantar envido
        - p1 puede cantar truco
        - p1 juega una carta
        - p2 puede cantar envido
        - p2 puede cantar truco
        - p2 juega una carta

    segundo turno:
        - El ganador del primer turno tira una carta
        - p1 puede cantar truco
        - p1 juega una carta
        - p2 puede cantar truco
        - p2 juega una carta

        si px gano los 2 turnos gana la mano
    
    Tercer turno:
        - El ganador del segundo turno tira una carta
        - p1 puede cantar truco
        - p1 juega una carta
        - p2 puede cantar truco
        - p2 juega una carta

    - Logica del envido
        Solo en la primer mano!
        px canta envido                     2 no querido 1
        py acepta - rechaza - envido        4 no querido 3
        px acepta - rechaza - real envido   6 no querido 5
        asi hasta falta envido              Los puntos que le faltan al otro hasta 15 o hasta 30 no querido 7

    - logica del truco:
        px no canta nada pero gana la mano 1 punto
        px canta truco                     2 no querido 1
        py quiero no quiero retruco        3 no querido 2
        px quiero no quiero vale cuatro    4 no querido 3

"""

# [TODO] 26 January 2020 Los eventos se encolan cuando se spamea una tecla y estaria bueno que se 
#   limpie la queue cuando empieza a apretar una tecla 

import os
import time
from truco_clases import Mazo, Player
import pygame

# Consts
GAME_DELTA_TIME = 3  # Tiempo de espera en segundos e ntre momentos claves
SCREEN_RESOLUTION = (1280, 720)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Init
pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
clock = pygame.time.Clock()
font_name = pygame.font.match_font("arial")

mazo = Mazo()

p1 = Player("Lenny")
p2 = Player("Karl")

# Titulo
pygame.display.set_caption("Truquito")

def draw_text(surf, msg, size, color,x_text, y_text):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(
        msg, True,color
    )
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x_text, y_text)
    surf.blit(text_surface, text_rect)


def end_game():
    # Matar a Tony
    pygame.quit()
    quit()

def draw_ganador(msg, carta_p1, carta_p2):
    # Limpiar pantalla
    screen.fill(BLACK)

    draw_text(
            screen,
            msg,
            25,
            WHITE,
            SCREEN_RESOLUTION[0]/2,
            SCREEN_RESOLUTION[1]/2 + 100

        )
    
    img_carta = pygame.image.load(carta_p1.imagen)
    x_carta = SCREEN_RESOLUTION[0] / 2 - 200
    y_carta = SCREEN_RESOLUTION[1] / 2 - 50
    screen.blit(img_carta, (x_carta, y_carta))

    img_carta = pygame.image.load(carta_p2.imagen)
    x_carta = SCREEN_RESOLUTION[0] / 2 + 100
    y_carta = SCREEN_RESOLUTION[1] / 2 - 50
    screen.blit(img_carta, (x_carta, y_carta))

    pygame.display.update()

def cantar_truco(player, other, truco=0):
    cantando = True
    
    cantos = ["Truco", "Retruco", "Vale4"]

    if truco > 0:
        menu = ["aceptar"]
        menu.append(cantos[truco])
        menu.append("Rechazar")
    else:
        menu = [cantos[truco]]
        menu.append("Salir")

    opt=0
    while cantando:
        # Limpiar pantalla
        # [TODO] 26 January 2020 dibujar un rectangulo y no ocultar todo el juego
        screen.fill(BLACK)

        for event in pygame.event.get():
        # [TODO] 25 January 2020 Solve this quit logic in the future
            if event.type == pygame.QUIT:
                end_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    end_game()

                if event.key == pygame.K_RIGHT:
                    opt += 1
                    if opt > len(menu)-1:
                        opt = 0

                if event.key == pygame.K_LEFT:
                    opt -= 1
                    if opt < 0:
                        opt = len(menu)-1

                if event.key == pygame.K_SPACE:
                    if opt == 0 and truco > 0:
                        truco +=1
                        player.modificador_truco = truco
                        other.modificador_truco = truco
                        print(f"truco {truco}")
                        cantando = False

                    elif opt == len(menu)-1:
                        if truco > 0:
                            other.modificador_truco = truco
                            cantando = False
                            raise Exception("Not implemented")
                        else:
                            cantando = False
                    else:
                        draw_text(
                            screen,
                            f"{player.nombre} canta {menu[opt]}!",
                            25,
                            WHITE,
                            SCREEN_RESOLUTION[0]/2,
                            10
                        )
                        cantar_truco(other, player, truco+1)
                        cantando = False

                    

                    

                    

        for i, palabra in enumerate(menu):
            x_palabra = SCREEN_RESOLUTION[0]/2 - 20 + i * 75
            if opt == i:
                y_palabra = SCREEN_RESOLUTION[1] -75
            else:
                y_palabra = SCREEN_RESOLUTION[1] -30
        
            draw_text(
                screen,
                f"{palabra}",
                25,
                WHITE,
                x_palabra,
                y_palabra
            )

        pygame.display.update()

def jugar_carta_scene(ronda, player, other):
    eligiendo = True
    opt = 0

    while eligiendo:
        # Limpiar pantalla
        screen.fill(BLACK)

        marcador = f"Ronda {ronda} - {player.nombre} {player.puntos} | {other.nombre} {other.puntos}"
        if player.modificador_truco > 1:
            marcador = f"{marcador} | Estamos en Truco!"

        draw_text(
            screen,
            marcador,
            20,
            WHITE,
            SCREEN_RESOLUTION[0]/4,
            0
        )

        draw_text(
            screen,
            f"{player.nombre}",
            20,
            WHITE,
            SCREEN_RESOLUTION[0]/2,
            SCREEN_RESOLUTION[1]-25

        )
        for event in pygame.event.get():
        # [TODO] 25 January 2020 Solve this quit logic in the future
            if event.type == pygame.QUIT:
                end_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    end_game()

                if event.key == pygame.K_RIGHT:
                    opt += 1
                    if opt > len(player.mano)-1:
                        opt = 0

                if event.key == pygame.K_LEFT:
                    opt -= 1
                    if opt < 0:
                        opt = len(player.mano)-1

                if event.key == pygame.K_SPACE:
                    player.cartas_jugadas.append(player.mano.pop(opt))
                    eligiendo = False
                
                if event.key == pygame.K_t:
                    # Como retrucar
                    if player.modificador_truco == 1:
                        cantar_truco(player, other)
                    else:
                        print("Ya se cantó el truco")

        if other.cartas_jugadas:
            for i, carta in enumerate(other.cartas_jugadas):
                img_carta = pygame.image.load(carta.imagen)
                x_carta = SCREEN_RESOLUTION[0] / 2 - 100 + i * 50
                y_carta = SCREEN_RESOLUTION[1] / 4 - 160
                screen.blit(img_carta, (x_carta, y_carta))

        if player.cartas_jugadas:
            for i, carta in enumerate(player.cartas_jugadas):
                img_carta = pygame.image.load(carta.imagen)
                x_carta = SCREEN_RESOLUTION[0] / 2 - 100 + i * 50
                y_carta = SCREEN_RESOLUTION[1] / 4 + 50
                screen.blit(img_carta, (x_carta, y_carta))
        
        for i, carta in enumerate(player.mano):
            img_carta = pygame.image.load(carta.imagen)
            x_carta = SCREEN_RESOLUTION[0] / 2 - 100 + i * 50
            if i == opt:
                y_carta = SCREEN_RESOLUTION[1] - 300
            else:
                y_carta = SCREEN_RESOLUTION[1] - 160
            screen.blit(img_carta, (x_carta, y_carta))

        pygame.display.update()
    

# Game loop
while True:
    for event in pygame.event.get():
        # [TODO] 25 January 2020 Solve this quit logic in the future
        if event.type == pygame.QUIT:
            end_game()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end_game()
    
    # Se reparten las 3 cartas
    p1.mano = []
    p2.mano = []
    
    p1.modificador_truco = 1
    p2.modificador_truco = 1

    p1.cartas_jugadas = []
    p2.cartas_jugadas = []

    for i in range(3):
        p1.agarrar_carta(mazo.agarrar())
        p2.agarrar_carta(mazo.agarrar())

    ganador = False
    ronda = 1

    p1.primera = False
    p2.primera = False

    while ronda <= 3 and ganador == False:
        
        jugar_carta_scene(ronda, p1, p2)
        jugar_carta_scene(ronda, p2, p1)

        # comparar
        if p1.cartas_jugadas[ronda-1].valor == p2.cartas_jugadas[ronda-1].valor:
            # Parda la mejor
            # Con esta logica el que gane segunda gana!
            if p1.primera:
                msg = f"{p1.nombre} gana la ronda"
                draw_ganador(msg, p1.cartas_jugadas[ronda-1], p2.cartas_jugadas[ronda-1])
                p1.puntos += 1 * p1.modificador_truco
                ganador = True
            elif p2.primera:
                paux = p2
                p2 = p1
                p1 = paux

                p1.primera = True
                msg = f"{p1.nombre} gana la ronda"
                draw_ganador(msg, p1.cartas_jugadas[ronda-1], p2.cartas_jugadas[ronda-1])
                p1.puntos += 1 * p1.modificador_truco
                ganador = True
            else:
                p1.primera = True
                p2.primera = True

                msg = "Empate! Parda la mejor"
                draw_ganador(msg, p1.cartas_jugadas[ronda-1], p2.cartas_jugadas[ronda-1])
        else:
            # Si gana p2 pasa a ser el primero en la proxima ronda
            if p1.cartas_jugadas[ronda-1].valor < p2.cartas_jugadas[ronda-1].valor:
                paux = p2
                p2 = p1
                p1 = paux

            if p1.primera:
                msg = f"{p1.nombre} gana la ronda"
                draw_ganador(msg, p1.cartas_jugadas[ronda-1], p2.cartas_jugadas[ronda-1])
                ganador = True
                # Dar puntos
                p1.puntos += 1 * p1.modificador_truco
            else:
                p1.primera = True
                msg = f"La carta de {p1.nombre} gana"
                draw_ganador(msg, p1.cartas_jugadas[ronda-1], p2.cartas_jugadas[ronda-1])

        time.sleep(GAME_DELTA_TIME)
        ronda += 1
