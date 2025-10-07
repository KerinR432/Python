"""Modifica el programa anterior para que el programa te de todos los intentos que
necesites pero que cuando aciertes te informe de cuantas veces has fallado antes de
lograrlo"""

import random

numAle = random.randint(1,50)
cont =  int(input("Introduce cuantos intentos quieres:\n"))
contFallos = 0
while cont !=0:
    numPersonaje = int(input("Introduce un numero\n"))
    if numAle < numPersonaje:
        print("El numero es menor")
    if(numAle > numPersonaje):
        print("El numero es mayor")
    if numAle == numPersonaje:
        print("Ganaste!!!!")
        print(f"tardaste unos :{contFallos} hasta que acertastes")
        cont=0
    cont = cont - 1
    contFallos = contFallos + 1
print("acaba el juego")