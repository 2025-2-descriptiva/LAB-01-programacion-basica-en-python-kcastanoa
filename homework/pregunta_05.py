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

def pregunta_05():
    data = cargar_data()
    letras = sorted({fila[0] for fila in data})
    return [(letra, 
             max(int(f[1]) for f in data if f[0] == letra), 
             min(int(j[1]) for j in data if j[0] == letra),
    )
            for letra in letras]
    
print(pregunta_05())    

    #Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    #por cada letra de la columa 1.

    #Rta/
    #[('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
