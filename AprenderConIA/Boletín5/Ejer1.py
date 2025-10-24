"""1. Escribir un programa que genere seis números aleatorios entre el 1 y el 49 sin que
ninguno de ellos esté repetido (simulando una lotería primitiva)."""

import random

# Generamos 6 números únicos aleatorios entre 1 y 49 usando sample para evitar repeticiones
loteria = random.sample(range(1, 50), 6)  # range(1,50) incluye del 1 al 49

# Ordenamos los números para una presentación más bonita (opcional, pero mejora la legibilidad)
loteria.sort()

# Imprimimos los números de forma atractiva para el usuario
print("¡Los números ganadores de la lotería son:")
print(", ".join(map(str, loteria)))  # Une los números con comas
print("¡Buena suerte!")  # Mensaje amigable extra
