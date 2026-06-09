"""
19. Escribir un programa que pida un número por teclado y nos muestre sus divisores
"""

numero = 0

numero = int(input("Introduce un numero: "))

for n in range(1,numero+1):
    if numero % n == 0:
        print(numero," / ",n," = ",0)