"""
20. Escribir un programa que nos pida tres números por teclado en cualquier orden y nos los
muestre en pantalla ordenados de menor a mayor
"""

numero_uno = 0
numero_dos = 0
numero_tres = 0

numero_uno = int(input("Introduce el primero numero: "))
numero_dos = int(input("Introduce el segundo numero: "))
numero_tres = int(input("Introduce el tercer numero: "))

numeros = [numero_uno, numero_dos, numero_tres]
numeros.sort()

print(numeros[0]," -> ",numeros[1]," -> ",numeros[2])