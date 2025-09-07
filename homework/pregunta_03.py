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


def pregunta_03():
    data = cargar_data()
    letras = sorted({fila[0] for fila in data}) # Las llaves hacen un conjunto con letras que no se repitan
    return [(letra, sum(int(f[1]) for f in data if f[0] == letra)) for letra in letras]

print(pregunta_03())

    #Retorne la suma de la columna 2 por cada letra de la primera columna como
    #una lista de tuplas (letra, suma) ordendas alfabeticamente.
    #Rta/[('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
