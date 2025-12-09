import random

#EJERCICIO 11
#Inicializamos variables
dado1 = 0
dado2 = 1
varibaleDeSalida = 0
turnos = 0


#Realizamos el bucle While, que mientras y no sea 1 siga generando dados


while varibaleDeSalida != 1:
    dado1 = random.randint(1, 6)
    dado2 =  random.randint(1,6)

    if dado1 == dado2: #hacemos la comparación
        varibaleDeSalida=1
    turnos +=1
#Imprimimos por pantalla

informe = f"""
JUEGO DE LOS DADOS IGUALES
EL PRIMER DADO ES:{dado1}
EL SEGUNDO DADO ES {dado2}
HAS TARDADO {turnos} PARA QUE
SEAN IGUALES
"""

print(informe)


