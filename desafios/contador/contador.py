"""
Contador para mis directos

1 - Tener una logica me de la hora actual HH-MM-SS
2 - Definir una fecha de finalización
"""


from datetime import datetime
from time import sleep

PATH = "cuenta.txt"


def cero_adelante(numero):
    if numero < 10:
        return f"0{numero}"
    elif numero >= 10:
        return f"{numero}"


f_act = datetime.now()
f_fin = datetime.strptime("20:00:00", "%H:%M:%S")

while f_fin <= f_act:
    dif = f_fin - f_act

    hour = dif.seconds // 3600
    min = (dif.seconds // 60) % 60
    seg = dif.seconds % 60

    diff_string = f"{cero_adelante(hour)}:{cero_adelante(min)}:{cero_adelante(seg)}"
    print(diff_string)

    with open(PATH, "w") as f:
        f.write(diff_string)

    sleep(1)
    f_act = datetime.now()

