"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from collections import Counter
def cargar_data():
    with open("files/input/data.csv", "r",encoding="utf-8") as f: #utf-8 para que identifique tildes y otros caracteres
        data = [line.strip().split("\t") for line in f.readlines()] #.strip para eliminar \n y .split para separar las comlumnas \t
    return data

def pregunta_09():
    data = cargar_data()
    claves = [
        par.split(':')[0]
        for fila in data
        for par in fila[4].split(',')
    ]
    conteo = Counter(claves)
    return dict(sorted(conteo.items()))
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
print(pregunta_09())