"""
- Justificar el texto de forma tal que queden todas las lineas del mismo
tamaño agregando espacios proporcionalmente. 
Si la linea no supera el 80% de la linea mas larga, no se debe justificar. 
- Contar la cantidad de caracteres del texto
- Buscar la palabra mas larga dentro del texto, hacer una lista con las
palabras del texto y mostrarla ordenadas por el tamaño de cada palabra,
en caso de repetirse dos palabras del mismo tamaño (ejemplo: una y uno)
mostrarlas pero ordenadas por orden alfabético.
"""

# Leer el archivo

in_file_name = "texto.txt"
out_file_name = "salida.txt"


def justify_line(line, spaces):
    """
    Funcion para justificar las lineas mas complejas
    """
    res = [line[0] + " " * spaces]
    if len(line) > 2:
        res = res + [
            " " * int(extra_spaces_per_word / 2)
            + l
            + " " * int(extra_spaces_per_word / 2)
            for l in line[1:-1]
        ]

    res = res + [" " * extra_spaces_per_word + line[-1]]
    return res


if __name__ == "__main__":
    # Abro el archivo y armo una lista con el tamaño de cada linea
    # y una lista con las palabras de esa linea
    # Ej: [32,["ya", "no", "te", "amo", "Raula"]]
    with open(in_file_name) as f:
        line = f.readline()
        meta_line = []
        max_line = [0, 0]
        while line:
            line_len = len(line)
            line_splitted = line.split(" ")
            if max_line[0] < line_len:
                max_line = [line_len, line_splitted]
            meta_line.append([line_len, line_splitted])

            line = f.readline()

        # Calculo el porcentaje permitido del 80% contra la linea mas grande
        allowed_percent = max_line[0] * 0.8
        # Limpio el archivo, creo que hay una forma de hacerlo de una pero paja
        with open(out_file_name, "w") as f:
            f.write("")

        # Calculo la suma de todos los caracteres
        sum = 0
        for n in meta_line:
            sum += n[0]
        print(f"Numero de caracteres {sum}")

        # Justifico cada linea y la guardo en el out_file_name
        for line in meta_line:
            normalized_lines = ""
            if line[0] < allowed_percent:
                extra_spaces = (
                    allowed_percent - line[0]
                )  # Calculates the needed extra spaces
                if extra_spaces > len(line[1]):
                    extra_spaces_per_word = int(
                        extra_spaces / len(line[1]) + 1
                    )  # Calculates how much spaces should be for each word
                    normalized_lines = justify_line(line[1], extra_spaces_per_word)
                else:
                    line[1][-1] = " " * int(extra_spaces + 1) + line[1][-1]
                    normalized_lines = line[1]

            else:
                normalized_lines = line[1]

            with open(out_file_name, "a") as f:
                f.write(" ".join(normalized_lines))

        print("Done")
