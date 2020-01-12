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

import os
import time
from truco_clases import Mazo, Player

#Consts
GAME_DELTA_TIME = 1 # Tiempo de espera en segundos e ntre momentos claves

# Init
mazo = Mazo()

p1 = Player("Lenny")
p2 = Player("Karl")


#Game loop
while True:
    os.system("clear")
    # Llevar conteo de puntos
    print(f"{p1.nombre} tiene {p1.puntos} puntos")
    print(f"{p2.nombre} tiene {p2.puntos} puntos")
    print("")

    # Se reparten las 3 cartas
    p1.mano = []
    p2.mano = []

    for i in range(3):
        p1.agarrar_carta(mazo.agarrar())
        p2.agarrar_carta(mazo.agarrar())

    ganador = False
    ronda = 1
    
    p1.primera = False
    p2.primera = False

    while ronda <= 3 and ganador == False:
        print(f"Ronda {ronda}")
        p1.jugar_carta()
        print(f"{p1.nombre} - juega {p1.carta_jugada.mostrar()}")
        time.sleep(GAME_DELTA_TIME)
        print("")

        p2.jugar_carta()
        print(f"{p2.nombre} - juega {p2.carta_jugada.mostrar()}")
        time.sleep(GAME_DELTA_TIME)
        print("")
        print("")
        
        # comparar
        if p1.carta_jugada.valor == p2.carta_jugada.valor:
            # Parda la mejor
            #Con esta logica el que gane segunda gana!
            p1.primera = True
            p2.primera = True
        else:
            # Si gana p2 pasa a ser el primero en la proxima ronda
            if p1.carta_jugada.valor < p2.carta_jugada.valor:
                paux = p2
                p2 = p1
                p1 = paux

            if p1.primera:
                print(f"gano {p1.nombre}!")
                ganador = True
                # Dar puntos
                p1.puntos += 1
            else:
                print(f"{p1.nombre} gana el turno")
                p1.primera = True

        time.sleep(GAME_DELTA_TIME)
        ronda += 1
