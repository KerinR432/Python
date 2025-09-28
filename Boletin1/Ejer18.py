import random
#Inicializamos la varible
numApocalisis = 0
numAleo = 0
while(numAleo != 666): #-->Generamos numeros Aleatorios hasta que sea 666
    numAleo = random.randint(1,1000)
    numApocalisis +=1

print(f"AJAJAJAJAJ EL APOCALISIS TE ESTA CERCA! LE QUEDAN {numApocalisis}")