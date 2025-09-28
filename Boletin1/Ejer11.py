import random

#EJERCICIO 11
#Inicializamos variables
dado1 = 0
dado2 = 1
i = 0
cont = 0
print('Soy el dado 1: ',dado1,'Soy el dado 2: ',dado2)  #pedimos por teclado

#Realizamos el bucle While, que meientras i no sea 1 siga generando dados
while i != 1:
    dado1 = random.randint(1, 6)
    dado2 =  random.randint(1,6)

    if  (dado1 == dado2): #hacemos la comparación
        i=1
    cont +=1
#Imprimimos por patalla
print('VAMOOOOS!!! SALIERON DOS QUE SUERTE, los dados son: ',dado1,dado2)
print(f'fueron {cont} veces')

