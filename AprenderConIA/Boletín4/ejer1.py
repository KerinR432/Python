# Programa que calcula el factorial de un número ingresado por el usuario

# Pedimos el número al usuario
numero = int(input("Introduce un número para calcular su factorial: "))

# Inicializamos el resultado en 1 (porque multiplicar por 1 no altera el resultado)
factorial = 1

# Recorremos todos los números desde 1 hasta el número dado
for i in range(1, numero + 1):
    factorial *= i  # Multiplicamos el resultado por el número actual

# Mostramos el resultado final
print(f"El factorial de {numero}! es {factorial}")
