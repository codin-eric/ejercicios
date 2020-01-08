"""
TODO: 
    - Parda la mejor

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

    - Logica del envido
        px canta envido                     2 no querido 1
        py acepta - rechaza - envido        4 no querido 3
        px acepta - rechaza - real envido   6 no querido 5
        asi hasta falta envido              Los puntos que le faltan al otro hasta 15 o hasta 30 no querido 7
    
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

    - logica del truco:
        px no canta nada pero gana la mano 1 punto
        px canta truco                     2 no querido 1
        py quiero no quiero retruco        3 no querido 2
        px quiero no quiero vale cuatro    4 no querido 3

"""

from truco_clases import Mazo, Player, Core


def render_display(p1, p2, turno):
    print(f"Turno: {turno}")
    p1.mostrar_mano()
    print("")
    p2.mostrar_mano()

    print("1- Tirar carta | 2- Cantar envido | 3- Cantar truco")
    # [TODO] 08 January 2020 validar entrada
    op = input("Ingresa opción: ")


# Init juego
mazo = Mazo()
p1 = Player("Edic")
p2 = Player("CPU")

for i in range(3):
    p1.agarrar(mazo.agarrar())
    p2.agarrar(mazo.agarrar())


# Game Loop
while True:
    render_display(p1, p2, 1)

    print("Primer turno")
    cmd = input("Que quere hace' ? ")
