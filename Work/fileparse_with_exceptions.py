# fileparse.py
#
# Exercise 3.3

# Se trabaja sobre definicion inicial de fileparse.py dada por el instructor en 3.3
import csv

def parse_csv(filename, select = None, types = None, has_headers = False, delimiter=','):     # Exercise 3.4 se agrega opcional select, Exercise 3.5 agrega types
    '''                                                   
    Parse a CSV file into a list of records
    '''
    if select and has_headers == False: # Exercise 3.8
        raise RuntimeError("select argument requires column headers")
    
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        records = []
        if has_headers:     # Exercise 3.6 agrega has_headers
            headers = next(rows)
        else:
            headers = []

        for rownum, row in enumerate(rows): # Exercise 3.9 enumeramos las filas
            if not row:    # Skip rows with no data
                continue

            if types:
                try:
                    row = [func(val) for func, val in zip(types, row) ]
                except ValueError as e: # Exercise 3.9 Capturamos los ValueError por fila 
                    print(f'Row {rownum}: Couldn\'t convert {row}')
                    print(f'Reason {e}')


            if select:
                row = [row[headers.index(colname)] for colname in select]
                record = dict(zip(select, row))
            
            if not select and types:
                record = dict(zip(headers, row))
            
            if not has_headers:
                record = tuple(row)
                
            records.append(record)

    return records