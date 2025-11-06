import random

#EJERCICIO 12

dados = [] #--> creamos lo que es un Array para almacenar los dados
salir = False
def numeroDados():
    for i in range(0,cantidadDados): #--> el tamaño del bucle es la cantidad de dados

        dados.append(random.randint(1,cantidadCaras)) #--> rellenamos el array depediendo de los dados y caras que pidamos
        print(f"Tu resultado de los dados que tienes {dados[i]}")
while salir == False:
    try:
        print("======================================")
        cantidadDados =  int(input("Introduce el numero de dados que quieres que se juegue: "))

        cantidadCaras = int(input("Introduce el numero de caras de los dados: "))

    except ValueError:
        print(f"⚠️Error tiene que ser un  numero entero⚠️")
    except ZeroDivisionError:
        print(f"⚠️Tu numero no tiene que contener el '0'⚠️")

    else:
        numeroDados()
        salir = True