"""
Programa para jugar penales contra la computadora.
Elegis donde disparar se calcula un poco de suerte junto
con habilidad para ver si es o no gol
"""

import random
from time import sleep

WAITING_TIME = 3  # Pequeño generador de suspenso (?)


def where(direct):
    """
    Función que retorna en palabras para donde elegiste disparar
    """

    pos = [
        "izq angulo abajo",
        "centro abajo",
        "der angulo abajo",
        "izq centro",
        "centro",
        "der centro",
        "izq angulo arriba",
        "centro up",
        "der angulo arriba",
    ]
    return pos[direct - 1]


def how_look(lck):
    """
    Función que retorna en palabras la suerte que tuviste
    """

    pos = [
        "Falla por completo!",
        "Eso se vio horrible!",
        "No es su dia!",
        "Podria ser mejor!",
        "tiro normal",
        "Buen tiro!",
        "Lindo tiro!",
        "Excelente tiro!",
        "Tiro perfecto!",
        "GRACIAS DIOS POR HACERME ARGENTINO Y CONTEMPORANEO!",
    ]
    return pos[lck - 1]


def suspense_adder():
    # Agrego suspenso
    wait = 0
    while wait < WAITING_TIME:
        print(".")
        sleep(1)
        wait += 1


# Elegis donde disparar
p_shoot = int(input("Donde disparar: "))
print("p1 patea para " + where(p_shoot))

# Calculo la suerte del jugador
p_luck = random.randint(1, 10)
print("y ")

suspense_adder()
print(how_look(p_luck))

# El arquero salta
gk_jump = random.randint(1, 9)
# Suerte del arquero
gk_luck = random.randint(1, 10)
print("EL ARQUERO SALTA!")
suspense_adder()

# Si la diferencia entre el tiro del jugador y el salto del arquero está por debajo de
# 6, el tiro puede ser gol!

jump = gk_jump - p_shoot

# Si la suerte del arquero es mayor que la del jugador puede ganar el arquero!
luck = p_luck - gk_luck
res = jump + luck


p1_festejo = "GOOOOOOOOOL"
gk_festejo = "EEEEEEL UUUUUUUUUUNOOOOOO"
gk_jump_win = "El arquero saltó de forma perfecta"
p1_jump_win = "Perfecto tiro del jugador"

if res > 0:
    print(p1_festejo)
else:
    print(gk_festejo)

if gk_jump > p_shoot:
    print(gk_jump_win)
else:
    print(p1_jump_win)

