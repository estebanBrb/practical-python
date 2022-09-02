# bounce.py
#
# Exercise 1.5

altura_inicial = 100 # Metros
reduccion_de_altura = 3 / 5

for i in range(10):
    altura_inicial = altura_inicial * reduccion_de_altura
    print(round(altura_inicial, 4))



