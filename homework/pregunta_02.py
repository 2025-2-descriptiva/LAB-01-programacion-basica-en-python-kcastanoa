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
from operator import itemgetter
from collections import Counter

def pregunta_02():
    data = cargar_data()
    primera_columna = [row[0] for row in data]  # saco la primera columna
    conteo = Counter(primera_columna)
    return sorted(conteo.items(), key=itemgetter(0), reverse=False) #conteo solo si solo son las letras, .tem cuando sol por parejas
    
print(pregunta_02())

# Retorne la cantidad de registros por cada letra de la primera columna como la lista de tuplas (letra, cantidad), ordendas alfabéticamente.
#Rta/[('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]