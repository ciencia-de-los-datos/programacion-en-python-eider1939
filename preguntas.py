"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
##funcion lee el archivo data.csv y lo gruada en un lista por lines separadas por '\t'
def read_texto():
    lineas_texto=[]
    with open("data.csv", "r") as file:
        data = file.readlines()
    for line in data:
        line = line.replace('\n','')
        row = line.split(sep='\t')
        lineas_texto.append(row)
    return lineas_texto
##funcion cuenta las ocurrencias 
def reducer(sequence):
    counter = {}
    for key, value in sequence:
        if key in counter:
            counter[key] += int(value)
        else:
            counter[key] = int(value)
    return sorted([(key, counter[key]) for key in counter])


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data=read_texto()
    valores_columna2=[int(data[i][1]) for i in range(0,len(data))]
    return sum(valores_columna2)

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data=read_texto()
    lista_columna1=[(data[i][0],1) for i in range(0,len(data))]
    map_1_unicos=reducer(sequence=lista_columna1)
    return map_1_unicos


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data=read_texto()
    lista_columna1_2=[(data[i][0],int(data[i][1])) for i in range(0,len(data))]
    map_1_2_unicos=reducer(sequence=lista_columna1_2)
    return map_1_2_unicos

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data=read_texto()
    lista_mes=[]
    for i in range(0,len(data)):
        lista_fecha=data[i][2].split('-')
        mes=lista_fecha[1]
        lista_mes.append((mes,1))
    map_mes=reducer(sequence=lista_mes)
    return map_mes


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data=read_texto()
    lista_columna1_2=[(data[i][0],int(data[i][1])) for i in range(0,len(data))]
    counter = {}
    for key, value in lista_columna1_2:
        if key in counter:
            if counter[key][0] < value:
                counter[key][0] = value
            elif counter[key][1] >value:
                counter[key][1] = value
        else:
            counter[key] = [int(value),int(value)]
    return sorted([(key, counter[key][0],counter[key][1]) for key in counter])


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data=read_texto()
    data_texto=""
    for i in range(0,len(data)):
        data_texto+=data[i][4]+','
    lista_de_clave = list(subString.split(":") for subString in data_texto.split(","))
    #elimar la ultima posiciond el lista lista_de_claves ya que esta vacia
    lista_de_clave.pop()
    lista_de_tulas=[(lista_de_clave[i][0],lista_de_clave[i][1]) for i in range(0,len(lista_de_clave))]
    counter = {}
    for key, value in lista_de_tulas:
        value=int(value)
        if key in counter:
            if counter[key][0] > value:
                counter[key][0] = value
            elif counter[key][1] < value:
                counter[key][1] = value
        else:
            counter[key] = [int(value),int(value)]
    return sorted([(key, counter[key][0],counter[key][1]) for key in counter])


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data=read_texto()
    counter={}
    for line in data:
        letter=line[0]
        value=int(line[1])
        if value in counter:
            counter[value].append(letter)
        else:
            counter[value]=[letter]
    return sorted([(key, value) for key, value in counter.items()])


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
