"""
16. Escribir un programa que genere seis números aleatorios entre el 1 y el 49 (simulando una
lotería primitiva). Por el momento no te preocupes de que algunos números puedan salir
repetidos. Ya resolveremos eso más adelante.
"""

import random

loteria = []

for n in range(1, 6):
    loteria.append(random.randint(1, 49))

print(loteria)