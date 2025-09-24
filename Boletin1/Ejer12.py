import random

#EJERCICIO 12
print("======================================")
cantidadDados =  int(input("Introduce el numero de dados que quieres que se juegue"))

dados = [] #--> creamos lo que es un Array para almacenar los dados
cantidadCaras = int(input("Introduce el numero de caras de los dados"))

for i in range(0,cantidadDados): #--> el tamaño del bucle es la cantidad de dados

    dados.append(random.randint(1,cantidadCaras)) #--> rellenamos el array depediendo de los dados y caras que pidamos
    print(f"Tu resultado de los dados que tienes {dados[i]}")

