"""
23. Escribir un programa que te escriba todos los números primos que hay entre el 1 y el 100
"""

numeros_primos = []
contador_primo = 0

for n in range (1,100):
    contador_primo = 0
    for d in range (1,100):
        if n % d == 0:
            contador_primo += 1
    if contador_primo <= 2:
        numeros_primos.append(n)
print("Los numeros primos son {}".format(numeros_primos))