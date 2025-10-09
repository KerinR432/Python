"""1. Escribir un programa que genere seis números aleatorios entre el 1 y el 49 sin que
ninguno de ellos esté repetido (simulando una lotería primitiva)."""
import random

numeros = list()
for i in range(0,10):
    numeros.append(random.randint(1,49))
loteria = random.sample(numeros,6)
print(f"Los numeros ganadores son: {loteria}")