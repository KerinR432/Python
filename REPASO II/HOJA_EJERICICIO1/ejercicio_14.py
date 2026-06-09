"""
14. Escribir un programa que nos pida dos números por teclado y genere un número aleatorio
comprendido entre ambos. Por el momento no te preocupes de que el primer número
siempre debería de ser menor que el segundo, simplemente no los metas en un orden
incorrecto
"""

import random

numero_uno = 0
numero_dos = 0

numero_uno = int(input("Introduce un numero: "))
numero_dos = int(input("Introduce un numero: "))

numero_aleatorio = random.randint(numero_uno, numero_dos)
print(numero_aleatorio)