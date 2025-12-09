import random

# EJERCICIO 11
# Escribir un programa que simule el lanzamiento de dos dados hasta que sus valores coincidan.

# Inicialización de variables
# Inicializamos los dados a valores diferentes para garantizar que el bucle 'while' se ejecute al menos una vez.
dado1 = 0
dado2 = 1
contador_lanzamientos = 0

# Realizamos el bucle While. El bucle se ejecuta mientras los valores de los dados sean diferentes.
while dado1 != dado2:
    # Generar un número aleatorio entre 1 y 6 para cada dado
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    # Incrementar el contador de lanzamientos en cada iteración
    contador_lanzamientos += 1

    # Opcional: Imprimir el resultado de cada lanzamiento para ver la simulación
    # print(f"Lanzamiento #{contador_lanzamientos}: Dado 1 = {dado1}, Dado 2 = {dado2}")

# Una vez que el bucle termina, sabemos que dado1 == dado2.
# Imprimimos los resultados finales.
print('\n--- Resultados de la Simulación ---')
print(f'¡VAMOOOOS! SALIERON DOS IGUALES, los dados son: {dado1} y {dado2}')
print(f'Fueron necesarios {contador_lanzamientos} lanzamientos para que coincidieran.')
