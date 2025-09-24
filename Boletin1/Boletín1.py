import random

#EJERCICIO 11
dado1 = 0
dado2 = 1
print('Soy el dado 1: ',dado1,'Soy el dado 2: ',dado2)

i = 0
cont = 0
while i != 1:
    dado1 = random.randint(1, 6)
    dado2 =  random.randint(1,6)

    if  (dado1 == dado2):
        i=1
    cont +=1
print('VAMOOOOS!!! SALIERON DOS QUE SUERTE, los dados son: ',dado1,dado2)
print(f'fueron {cont} veces')

#EJERCICIO 12
print("======================================")
cantidadDados =  int(input("Introduce el numero de dados que quieres que se juegue"))

dados = [] #--> creamos lo que es un Array para almacenar los dados
cantidadCaras = int(input("Introduce el numero de caras de los dados"))

for i in range(0,cantidadDados): #--> el tamaño del bucle es la cantidad de dados

    dados.append(random.randint(1,cantidadCaras)) #--> rellenamos el array depediendo de los dados y caras que pidamos
    print(f"Tu resultado de los dados que tienes {dados[i]}")


#EJERCICIO 14
print("****************************************")

num1 = int(input("Introduce un numero"))
num2 = int(input("Introduce un segundo numero"))

rsdo = random.randint(num1,num2)

print(rsdo)