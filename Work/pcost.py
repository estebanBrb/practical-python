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