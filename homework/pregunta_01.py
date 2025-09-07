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

data = cargar_data()
print(data[:5]) #imprime las primeras 5 filas


def pregunta_01():
   data = cargar_data()
   suma = sum(int(row[1]) for row in data)
   return suma

print(pregunta_01())