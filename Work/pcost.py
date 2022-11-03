# pcost.py
#
# Exercise 1.27
import sys      # exercise 1.33 

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        headers = next(f)
        total_cost = 0
        for line in f:
            try:
                row = line.split(',')
                total_cost += int(row[1]) * float(row[2])
            except:
                print(f'La fila {row} no tiene el formato adecuado.')
    
    return total_cost

# Agregando lectura de parametro desde la commandline,
# sys.argv es una lista que contiene los parametros pasados desde la linea de comandos
# si hubiera alguno para pasar.
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

# llamado desde la cl: python3 pcost.py Data/portfolio.csv
cost = portfolio_cost(filename)
print(f'Total cost {cost}')

#
#
# Exercise 2.15

def portfolio_cost_alt(filename):
    with open(filename, 'rt') as f:
        headers = next(f)
        total_cost = 0
        for lineno, line in enumerate(f, start = 1):
            try:
                row = line.split(',')
                total_cost += int(row[1]) * float(row[2])
            except ValueError:
                print(f'La fila {lineno}: No tiene el formato adecuado: {row}')
    
    return total_cost

#
#
# Exercise 2.16
import csv

def portfolio_cost_zip(filename):
    with open(filename, 'rt') as f:
        filas = csv.reader(f)
        headers = next(filas)
        total_cost = 0
        for lineno, line in enumerate(filas, start = 1):
            record = dict(zip(headers, line))
            #print(record)
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'La fila {lineno}: No tiene el formato adecuado: {line}')
    
    return total_cost

