import random

# EJERCICIO 12
print("======================================")

# Pedimos y validamos el número de dados
cantidadDados = int(input("Introduce el número de dados que quieres lanzar: "))
if cantidadDados <= 0:
    print("Error: Debes introducir un número positivo de dados.")
    exit()  # Salimos si es inválido

# Pedimos y validamos el número de caras
cantidadCaras = int(input("Introduce el número de caras de los dados: "))
if cantidadCaras <= 0:
    print("Error: Debes introducir un número positivo de caras.")
    exit()  # Salimos si es inválido

# Creamos una lista para almacenar los resultados de los dados
dados = []

# Bucle que itera por cada dado, generando un lanzamiento aleatorio
for i in range(cantidadDados):
    lanzamiento = random.randint(1, cantidadCaras)  # Generamos un número aleatorio entre 1 y cantidadCaras
    dados.append(lanzamiento)

# Imprimimos los resultados de forma bonita para el usuario
print(f"\nResultados de los {cantidadDados} dados (cada uno con {cantidadCaras} caras):")
print(", ".join(map(str, dados)))  # Mostramos todos los resultados en una línea separados por comas
print(f"Suma total: {sum(dados)}")  # Opcional: mostramos la suma para más info
print("¡Buena suerte con tus lanzamientos!")  # Mensaje amigable extra
