"""
22. Escribir un programa que genere un número primo aleatorio entre el 10.000.000 y el
50.000.000
"""

import random
contador_divisible = 0
numero_primo = 0

while True:
    numero_primo = random.randint(10000000,50000000)
    contador_divisible = 0

    for n in range(1,numero_primo+1):
        if numero_primo % n == 0:
            contador_divisible += 1
    if contador_divisible <= 2:
        print("El numero {} es primo".format(numero_primo))
        break
