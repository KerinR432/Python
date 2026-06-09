"""
21. Escribir un programa que pida por teclado un número al usuario y calcule si es primo o no
"""
numero = 0
numero = int(input("Introduce un numero: "))
contador_divisible = 0

for n in range(1,numero+1):
    if numero % n == 0:
        contador_divisible += 1

if contador_divisible <= 2:
    print("El numero {} es primo".format(numero))
else:
    print("El numero {} no es primo".format(numero)," sus divisibles son mayores a dos ",contador_divisible)