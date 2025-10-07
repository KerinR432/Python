"""15. Modifica el programa anterior para que al iniciar el juego te pida dos parámetros con
objeto de cambiar la dificultad del juego: el número máximo (antes era siempre 50) o
el número de intentos posibles (antes era siempre 5). """

import random
opcion = 0
cont = 5
numAle = random.randint(1, 50)
while(opcion!= 3):
    print("1. jugar \n 2. Elegir dificultad\n 3. salir\n")
    opcion = int(input("introduce un numero:\n"))
    match opcion:
        case 1:
            contFallos = 0
            while cont != 0:
                numPersonaje = int(input("Introduce un numero\n"))
                if numAle < numPersonaje:
                    print("El numero es menor")
                    cont = cont - 1
                if (numAle > numPersonaje):
                    print("El numero es mayor")
                    cont = cont - 1
                if numAle == numPersonaje:
                    print("Ganaste!!!!")
                    print(f"tardaste unos :{contFallos} hasta que acertastes")
                    cont = 0
                contFallos = contFallos + 1
            print("acaba el juego")
        case 2:
            print("Aqui escoges la dificultad introduciendo cuantas oportunidades tienes y cuanto de rango quieres el numero Aletorio")
            cont = int(input("Introduce cuantos intentos quieres:\n"))
            n = int(input("Intorduce el numero aletorio maximo\n"))
            numAle = random.randint(1, n)

        case 3:
            print("Salir del jeugo")
        case _:
            print("Introcuciste mal el numero")

print("Fin el jeugo")