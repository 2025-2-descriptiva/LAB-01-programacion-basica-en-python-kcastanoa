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
from collections import Counter

def pregunta_04():
    data = cargar_data()
    meses = Counter(row[2][5:7] for row in data) #para extraer los 2 digitos del mes / row[2].split('-')[1] como alternativa
    return sorted(meses.items())

print(pregunta_04())

    #La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    
    #cantidad de registros por cada mes, tal como se muestra a continuación.

    #Rta/
    #[('01', 3),
     #('02', 4),
     #('03', 2),
     #('04', 4),
     #('05', 3),
     #('06', 3),
     #('07', 5),
     #('08', 6),
     #('09', 3),
     #('10', 2),
     #('11', 2),
     #('12', 3)]