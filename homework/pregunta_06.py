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

def pregunta_06():
    data = cargar_data()
    pares = [
        (clave, int(valor))
        for fila in data
        for clave, valor in (par.split(':') for par in fila[4].split(','))
    ]
    claves = sorted({ clave for clave, _ in pares})
    return [
        (clave,
         min(valor for kk, valor in pares if kk == clave),
         max(valor for kk, valor in pares if kk == clave))
        for clave in claves
    ]

print(pregunta_06())
    
    #La columna 5 codifica un diccionario donde cada cadena de tres letras
    #corresponde a una clave y el valor despues del caracter `:` corresponde al
    #valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    #pequeño y el valor asociado mas grande computados sobre todo el archivo.
    #Rta/
    #[('aaa', 1, 9),
     #('bbb', 1, 9),
     #('ccc', 1, 10),
     #('ddd', 0, 9),
     #('eee', 1, 7),
     #('fff', 0, 9),
     #('ggg', 3, 10),
     #('hhh', 0, 9),
     #('iii', 0, 9),
    # ('jjj', 5, 17)]