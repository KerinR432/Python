"""
5. Escribir un programa que pida por teclado un número al usuario y diga si es par o impar
"""

numero = int(input("Introduce un numero: "))

if numero % 2 == 0:
    print("el ",numero,"es par")
else:
    print("el ",numero,"es impar")