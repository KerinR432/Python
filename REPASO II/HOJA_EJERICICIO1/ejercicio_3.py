"""
3. Escribir un programa donde se muestren los 5 primeros números múltiplos de uno dado por
el usuario (se introducirá por teclado)
"""

numero = int(input("Ingrese un numero: "))

for n in range(1,6):
    print(numero*n)