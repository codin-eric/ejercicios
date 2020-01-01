"""Juego del Ahorcado.

1 - Ingresar una palabra
2 - Se tiene 7 vidas
3 - Se ingresa letra por letra hasta que se descubre la palabra
o se terminan las vidas
4 - Profit
"""

vida = 7
ganaste = False

palabra = input("Ingresa la palabra del ahorcado ").lower()
secreta = " ".join(["_" for letra in palabra])
letras = []

while ganaste:
    letra = input("Decime una letra: ").lower()

    if letra in palabra:
        letras.append(letra)

        secreta = " ".join([letra if letra in letras else "_" for letra in palabra])
        print(secreta)

        if len(letras) == len(secreta):
            print("GANASTE!!!")
            ganaste = True

    else:
        vida = vida - 1
        print(f"{letra} no está en la palabra")
        print(f"Te quedan {vida} vidas")
        if vida <= 0:
            print("perdiste")
            break
