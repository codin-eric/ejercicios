"""
Programa que recibe una hora y guarda en un directorio un archivo con
el tiempo que falta para esa hora

TODO:
    - Agregar argparse
    - Usar la logica de sleep(1)
    - Implementar to_file
"""

from datetime import datetime
from time import sleep


def to_file(dir, time):
    with open(dir, "w") as f:
        f.write(time)


dir = "timer.txt"
end_date = datetime.strptime("21:00:00", "%H:%M:%S")
now = datetime.now()

while end_date <= now:
    faltan = end_date - now

    hours = faltan.seconds // 3600
    minutes = (faltan.seconds // 60) % 60
    secs = (faltan.seconds) % 60

    if hours >= 1:
        msg = f"{hours}:{minutes}:{secs}"
    else:
        msg = f"{minutes}:{secs}"

    to_file(dir, msg)
    sleep(1)
    now = datetime.now()
