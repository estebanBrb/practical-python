# report.py
#
# Exercise 2.4

import csv
from fileinput import filename
from os import read

def read_portfolio(filename):
    '''Lee un portfolio (csv) y guarda los datos de filas y columnas en una lista de tuplas o diccionarios. '''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            name = row[0]
            nshares = int(row[1])
            price = float(row[2])
            #holding = (name, nshares, price)
            holding = {
                'name': name,
                'shares': nshares,
                'price': price
            }
            
            portfolio.append(holding)
    
    return portfolio


#
#
# Exercise 2.6

def read_prices(filename):
    prices = {}

    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name = row[0]
                price = float(row[1])
                prices[name] = price
            except: 
                print(f"La fila {row} tiene un formato incorrecto.")
            
    return prices


#
#
# Exercise 2.9

def make_report(portfolio, prices):
    '''
     Takes a list of stocks and dictionary of prices 
     as input and returns a list of tuples containing 
     the rows of a table.
    '''
    report = []
    for stock in portfolio:
        stock_detail = (stock['name'], stock['shares'], prices[stock['name']], prices[stock['name']] - stock['price'])
        report.append(stock_detail)

    return report

#
#
#

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

# Calculamos el valor total del portfolio
costo_total = 0.0
for f in portfolio:
    costo_total += f['shares'] * f['price']

valor_actual = 0.0
for f in portfolio:
    valor_actual += f['shares'] * prices[f['name']]

print(f'Valor actual del portfolio: {valor_actual}')
print(f'Costo total del portfolio: {costo_total}')
print(f'Ganancia: {valor_actual - costo_total}')

#
#
# Exercise 2.10
# print del reporte formateado
reporte = make_report(portfolio, prices)
for fila in reporte:
    print('%10s %10d %10.2f %10.2f' % fila)

# print usando f-strings
print('\nf-strings')
for name, shares, price, change in reporte:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

#
#
# Exercise 2.11
# print del reporte formateado con encabezados
print('\nReporte Formateado')
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))  # tomado de /solutions/2.11
for name, shares, price, change in reporte:
    print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
