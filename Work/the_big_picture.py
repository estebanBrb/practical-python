# Ejercicio 2.26
# Ejemplo de construccion de diccionarios a partir de
# un archivo csv con datos ordenado por columnas

# Forma basica
import csv
import pprint

f = open('Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
print(f'Encabezados: {headers} \nFila: {row}')

# Utilizando zip() y list comprehension
types = [str, float, str, str, float, float, float, float, int]
converted = [ func(val) for func, val in zip(types, row) ]
record = dict(zip(headers, converted))
record['date'] = tuple( [ int(value) for value in record['date'].split('/') ] )
print('Record')
pprint.pprint(record)
