"""
25. Escribir un programa que reciba por teclado un número y muestre sucesivamente el
resultado de ir dividiéndolo por dos sucesivamente hasta llegar a un número igual o menor a
1. Caso de ser necesario los resultados se mostrarán con dos decimales. Un ejemplo de una
ejecución correcta después de introducir el número 34 ser´ía esta:
Haz introducido el número 34
17
8.5
4.25
2.12
1.06
0.53
"""

numero = 0
numero = int(input("introduce un numero: "))
numero_divisible = 0

while True:
    numero_divisible = numero / 2

    if numero_divisible <= 1:
        break
    print(numero_divisible)
    numero = numero_divisible

print(numero_divisible)