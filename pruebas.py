

def read_texto():
    lineas_texto=[]
    with open("data.csv", "r") as file:
        data = file.readlines()
    for line in data:
        line = line.replace('\n','')
        row = line.split(sep='\t')
        lineas_texto.append(row)
    return lineas_texto

def reducer(sequence):
    counter = {}
    for key, value in sequence:
        if key in counter:
            counter[key] += int(value)
        else:
            counter[key] = int(value)
    return sorted([(key, counter[key]) for key in counter])

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
        value=line[1]
        if value in counter:
            counter[value].append(letter)
        else:
            counter[value]=[letter]
    return sorted([(key, value) for key, value in counter.items()])
print(pregunta_07())