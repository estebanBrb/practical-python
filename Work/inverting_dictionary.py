# Ejercicio 2.17
# Invertir un diccionario para mostrar los pares de tuplas (key, value) como (value, key)

# Definimos un diccionario
precios = {
    'GOOG': 490.1,
    'AA': 23.45,
    'IBM': 91.1,
    'MSFT': 34.23
}

# Mostramos pares (clave, valor) con items()
precios_clave_valor = precios.items()
print(precios_clave_valor)

# Mostramos pares (valor, clave) con zip(), values(), keys(), esto puede ser util si deseamos
# ordenar la lista con sort() o bien si se desea hacer una operacion matematica particular
# como buscar un maximo o un minimo en la lista.
lista_de_precios = list(zip(precios.values(), precios.keys()))
print(lista_de_precios)

# Ejemplos de uso de zip(): no se limita solo a pares
a = [1, 2, 3, 4]
b = ['w', 'x', 'y', 'z']
c = [0.1, 0.2, 0.3, 0.4]

lista_con_zip = list(zip(a, b, c))
print(lista_con_zip)

# Si las listas a unir no tienen la misma dimension, la lista final tiene la longitud de la mas corta
# y los elementos restantes se descartan
d = [1, 2, 3, 4, 5, 6]
e = ['a', 'b', 'c']
print(list(zip(d, e)))