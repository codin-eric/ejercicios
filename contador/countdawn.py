"""
Programa que recibe una hora y guarda en un directorio un archivo con
el tiempo que falta para esa hora

TODO:
    - Agregar argparse
    - Usar la logica de sleep(1)
    - Implementar to_file
"""

from datetime import datetime


def to_file(dir, time):
    with open(dir, "w") as f:
        f.write(time)


now = datetime.now()
end_date = datetime.strptime("21:00:00", "%H:%M:%S")

faltan = end_date - now

hours = faltan.seconds // 3600
minutes = (faltan.seconds // 60) % 60
secs = (faltan.seconds) % 60

if hours >= 1:
    print(f"faltan {hours}:{minutes}:{secs}")
else:
    print(f"faltan {minutes}:{secs}")
