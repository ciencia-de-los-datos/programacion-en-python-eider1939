import csv
 
lista_columna12=[]
with open('data.csv') as File:
    reader = csv.reader(File, delimiter=',', quotechar='\t',
                        quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        valor_1=row[0].split('\t')
        lista_columna12.append((valor_1[0],valor_1[1]))
def reducer(sequence):
    
    counter = {}
    for key, value in sequence:
        if key in counter:
            counter[key] += int(value)
        else:
            counter[key] = int(value)

    return sorted([(key, counter[key]) for key in counter])

print(reducer(sequence=lista_columna12))