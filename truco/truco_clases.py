"""
Clases para definir en el juego del truco!
"""

import random

N_CARTAS = [1,2,3,4,5,6,7,10,11,12]
N_PALOS = [0, 1, 2, 3]


class Player():
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos = 0
        self.mano = []
        self.primera = False
    
    def agarrar_carta(self, carta):
        self.mano.append(carta)

    def _mostrar_mano(self):
        if len(self.mano) <= 0:
            res = "No tengo na'a ami'o"
        else:
            res = f"Mano de {self.nombre}"
            for i, carta in enumerate(self.mano, 1):
                res = f"{res} \n {i} - {carta.mostrar()}"
        
        return res
    
    def jugar_carta(self):
        print(self._mostrar_mano())
        opt = int(input("Cual carta queres jugar? "))

        while opt < 1 or opt > len(self.mano):
            print("No kapo ese numero no es correcto")
            opt = int(input("Elegi bien turbina? "))

        self.carta_jugada = self.mano.pop(opt -1)


class Mazo():
    #40 Cartas 
    def __init__(self):
        self.cartas = []
        for palo in N_PALOS:
            for numero in N_CARTAS:
                carta = Carta(numero,palo)
                self.cartas.append(carta)

        random.shuffle(self.cartas)

    def agarrar(self):
        return self.cartas.pop()


class Carta():
    def __init__(self, numero, palo):
        palos = ["espadas", "bastos", "oros", "copas"]
        self.numero = numero
        self.npalo = palo
        self.palo = palos[palo]
        self.valor = self._rankear()

    def mostrar(self):
        return f"{self.numero} de {self.palo}"

    #Rankear
        """
        valor | carta
        14       1 espada
        13       1 basto
        12       7 espada
        11       7 oro
        10       3
        9        2
        8        1 oro - 1 copa
        7        12
        6        11
        5        10
        4        7 basto 7 copa
        3        6
        2        5
        1        4
        """
    def _rankear(self):
        if self.numero != 1 and self.numero != 7:
            basicas = {
                2: 9,
                3: 10,
                4: 1,
                5: 2,
                6: 3,
                10: 5,
                11: 6,
                12: 7,
            }
        
            return basicas[self.numero]

        if self.numero ==1:
            if self.npalo == 1: # Ancho de basto
                return 13
            elif self.npalo == 0: # Ancho de espada
                return 14
            else:
                return 8
        
        if self.numero == 7:
            if self.npalo == 0: # Espada
                return 12
            elif self.npalo == 2: # Oro
                return 11
            else:
                return 4
