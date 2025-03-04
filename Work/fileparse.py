# fileparse.py
#
# Exercise 3.3

# Se trabaja sobre definicion inicial de fileparse.py dada por el instructor en 3.3
import csv

def parse_csv(filename, select = None, types = None, has_headers = False, delimiter=','):     # Exercise 3.4 se agrega opcional select, Exercise 3.5 agrega types
    '''                                                   
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)
        records = []
        if has_headers:     # Exercise 3.6 agrega has_headers
            headers = next(rows)
        else:
            headers = []

        for row in rows:
            if not row:    # Skip rows with no data
                continue

            if types:
                row = [func(val) for func, val in zip(types, row) ]

            if select:
                row = [row[headers.index(colname)] for colname in select]
                record = dict(zip(select, row))
            
            if not select and types:
                record = dict(zip(headers, row))
            
            if not has_headers:
                record = tuple(row)
                
            records.append(record)

    return records