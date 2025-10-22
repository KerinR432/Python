import random

lista = [20,45,55,29,20,24,14,45,20]
numero = []
cantidad = list()
num = " "
for n in lista:
    if lista.count(n) > 1:
        numero.append(n)
        cantidad.append(lista.count(n))

print(random.sample(numero,2), random.sample(cantidad,2))
