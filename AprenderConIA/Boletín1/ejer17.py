import random

# Creamos una lista para almacenar los resultados de la quiniela
quiniela = []

# Generamos 15 números aleatorios del 1 al 3 y los añadimos a la lista
for i in range(15):
    quiniela.append(random.randint(1, 3))

# Reemplazamos los 3 por 'X' para representar empates
for i in range(15):
    if quiniela[i] == 3:
        quiniela[i] = 'X'

# Imprimimos los resultados de forma bonita para el usuario
print("Resultados de la quiniela (15 partidos):")
for i in range(15):
    print(f"Partido {i+1}: {quiniela[i]}", end="  ")  # Mostramos cada partido con índice, en una línea
print()  # Salto de línea al final

# Opcional: Resumen de tipos de resultados
num_1 = quiniela.count(1)
num_X = quiniela.count('X')
num_2 = quiniela.count(2)
print(f"\nResumen: {num_1} victorias locales (1), {num_X} empates (X), {num_2} victorias visitantes (2).")
print("¡Buena suerte con tus apuestas!")  # Mensaje amigable extra
