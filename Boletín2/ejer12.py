"""12. Realiza un juego en el que debes de acertar un número entre el 1 y el 50 que el
ordenador ha elegido de forma aleatoria. El programa te indicará si has acertado, si te
has pasado o si te has quedado corto. El programa finaliza cuando se acierta o cuando
se superan el número máximo de intentos establecidos en 5. """
import random

numAle = random.randint(1,50)
cont = 5
while cont !=0:
    numPersonaje = int(input("Introduce un numero\n"))
    if numAle < numPersonaje:
        print("El numero es menor")
    if(numAle > numPersonaje):
        print("El numero es mayor")
        cont=cont-1
    if numAle == numPersonaje:
        print("Ganaste!!!!")
        cont=0
print("acaba el juego")
