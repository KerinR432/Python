import random

# EJERCICIO 11
# Inicializamos variables: contador de intentos
cont = 0

# Bucle que genera lanzamientos hasta que los dados sean iguales
while True:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    cont += 1

    # Opcional: Imprimimos cada lanzamiento para ver el proceso (puedes quitarlo si no lo quieres)
    print(f"Lanzamiento {cont}: Dado 1 = {dado1}, Dado 2 = {dado2}")

    # Comparamos si los dados son iguales
    if dado1 == dado2:
        break

# Imprimimos el resultado final de forma bonita
print(f"\n¡VAMOS! Salieron dos iguales. Los dados son: {dado1} y {dado2}")
print(f"Fueron necesarios {cont} intentos.")
print("¡Qué suerte!")  # Mensaje amigable extra
