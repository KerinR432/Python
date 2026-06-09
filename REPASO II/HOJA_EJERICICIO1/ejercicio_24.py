"""
24. Modifica el programa anterior para que sea el usuario quién introduzca dos números y se nos
muestre los primos que hay entre ambos
"""

numeros_primos = []
contador_divisible = 0
numero_uno = 0
numero_dos = 0

numero_uno = int(input("introduce el primer numero: "))
numero_dos = int(input("introduce el segundo numero: "))

if numero_uno > numero_dos:
    for n in range (numero_dos,numero_uno+1):
        contador_divisible = 0
        for d in range (numero_dos,numero_uno+1):
            if n % d == 0:
                contador_divisible += 1
        if contador_divisible <= 2:
            numeros_primos.append(n)
else:
    for n in range (numero_uno,numero_dos+1):
        contador_divisible = 0
        for d in range (numero_uno,numero_dos+1):
            if n % d == 0:
                contador_divisible += 1
        if contador_divisible <= 2:
            numeros_primos.append(n)

print("Los numeros primos son {}".format(numeros_primos))