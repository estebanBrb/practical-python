# Exercise 3.1
# Modificacion de report.py para estructurarlo en funciones
#
# 

import csv

def read_portfolio(filename: str) -> dict:
    '''Lee un portfolio (csv) y guarda los datos de filas y columnas en una lista de diccionarios. '''

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        indices = [ headers.index(colname) for colname in headers ]
        
        # Creacion de la lista de diccionarios por comprension
        portfolio = [ { colname: row[index] for colname, index in zip(headers, indices) } for row in rows ]
    
    return portfolio

def read_prices(filename: str):
    '''Lee una lista (csv) de dos columnas y retorna una lista de diccionarios. '''
    
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


def make_report(portfolio: dict, prices: dict) -> list:
    '''
     Takes a dict of stocks and dictionary of prices 
     as input and returns a list of tuples containing 
     the rows of a table.
    '''
    report = [ (stock['name'], int(stock['shares']), float(prices[stock['name']]), float(prices[stock['name']]) - float(stock['price'])) for stock in portfolio ]

    return report

def print_report(report: dict):
    print('\nReporte Formateado')
    print('\n')
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))  # tomado de /solutions/2.11
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')


def portfolio_report(portfolio_filename, prices_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio, prices)
    print_report(report)

    # Calculamos el valor total del portfolio
    costo_total = 0.0
    for f in portfolio:
        costo_total += int(f['shares']) * float(f['price'])

    # Calculamos el valor actual del portfolio
    valor_actual = 0.0
    for f in portfolio:
        valor_actual += int(f['shares']) * float(prices[f['name']])
    
    # Mostramos los resultados 
    print(f'Valor actual del portfolio: {valor_actual}')
    print(f'Costo total del portfolio: {costo_total}')
    print(f'Ganancia: {valor_actual - costo_total}')
