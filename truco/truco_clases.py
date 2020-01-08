"""
Clase core game, mazo y cartas para el truco amigo
"""

import random

N_CARTAS = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
N_PALOS = [0, 1, 2, 3]


class Core:
    def __init__(self, p1, p2, mazo):
        self.turno = 1
        self.p1 = p1
        self.p2 = p2
        self.mazo = mazo


class Player:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []

    def agarrar(self, carta):
        self.mano.append(carta)

    def mostrar_mano(self):
        if len(self.mano) <= 0:
            print("No tengo nada")
        else:
            print(f"mano de {self.nombre}")
            for carta in self.mano:
                print(carta.mostrar())


class Carta:
    def __init__(self, numero, palo):
        palos = ["espadas", "bastos", "oros", "copas"]
        self.numero = numero
        self.n_palo = palo
        self.palo = palos[palo]

    def mostrar(self):
        return f"{self.numero} de {self.palo}"


class Mazo:
    # self.cartas = Carta[]
    def __init__(self):
        self.cartas = []
        for palo in N_PALOS:
            for numero in N_CARTAS:
                self.cartas.append(Carta(numero, palo))

        # Mezclar mazo
        random.shuffle(self.cartas)

    def agarrar(self):
        return self.cartas.pop()


if __name__ == "__main__":
    mazo = Mazo()

    print(len(mazo.cartas))

    carta = mazo.agarrar()
    print(carta.mostrar())

    carta = mazo.agarrar()
    print(carta.mostrar())

    print(len(mazo.cartas))
