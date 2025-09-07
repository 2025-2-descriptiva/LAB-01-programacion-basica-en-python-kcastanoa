"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
def cargar_data():
    with open("files/input/data.csv", "r",encoding="utf-8") as f: #utf-8 para que identifique tildes y otros caracteres
        data = [line.strip().split("\t") for line in f.readlines()] #.strip para eliminar \n y .split para separar las comlumnas \t
    return data


def pregunta_12():
    data = cargar_data()
    letras = sorted({row[0] for row in data})
    return {
        letra: sum(
            int(v)
            for fila in data if fila[0] == letra
            for _, v in (par.split(':') for par in fila[4].split(','))
        )
        for letra in letras
    }
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
print(pregunta_12())