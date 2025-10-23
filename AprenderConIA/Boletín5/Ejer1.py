"""Programa que simula una lotería primitiva: genera seis números aleatorios
únicos entre 1 y 49 (sin repeticiones)."""

import random

# Generamos directamente 6 números aleatorios únicos entre 1 y 49
numeros_ganadores = random.sample(range(1, 50), 6)

# Mostramos los números ganadores ordenados
print(f"Los números ganadores son: {sorted(numeros_ganadores)}")
