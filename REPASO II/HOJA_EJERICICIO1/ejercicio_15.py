"""
15. Modificar el programa del punto anterior para que si el primer número que metemos es
mayor que el segundo funcione correctamente. Es decir, si metemos en primer lugar el 50 y
en segundo el 10 nos debería de generar un número aleatorio entre el 10 y el 50 (y no entre el
50 y el 10 que no tiene mucha lógica…)

"""

import random
numero_uno = 0
numero_dos = 0

numero_uno = int(input("Introduce el primero numero: "))
numero_dos = int(input("Introduce el segundo numero: "))

numero_aleatorio = 0

if numero_uno > numero_dos:
    numero_aleatorio = random.randint(numero_dos, numero_uno)
else :
    numero_aleatorio = random.randint(numero_uno, numero_dos)

print(numero_aleatorio)