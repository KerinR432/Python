"""14. Modifica el programa anterior para que al final del programa te pida si quieres volver
a jugar y en caso afirmativo comience una nueva partida
"""
import random
opcion = 0
numAle = random.randint(1, 50)
while(opcion!= 2):
    print("Si quieres jugar introduce 1º\n si quieres salir introduce 2º\n ")
    opcion = int(input("introduce un numero:\n"))
    match opcion:
        case 1:
            cont = int(input("Introduce cuantos intentos quieres:\n"))
            contFallos = 0
            while cont != 0:
                numPersonaje = int(input("Introduce un numero\n"))
                if numAle < numPersonaje:
                    print("El numero es menor")
                if (numAle > numPersonaje):
                    print("El numero es mayor")
                if numAle == numPersonaje:
                    print("Ganaste!!!!")
                    print(f"tardaste unos :{contFallos} hasta que acertastes")
                    cont = 0
                cont = cont - 1
                contFallos = contFallos + 1
            print("acaba el juego")

        case 2:
            print("Salir del jeugo")
        case _:
            print("Introcuciste mal el numero")

print("Fin el jeugo")

