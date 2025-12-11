import random

#EJERCICIO 11
#* ----------------------- VARIABLES --------------------------
# hacemos 2 variables, una de dados donde los datos se almacenaran
dado1: int = 0
dado2: int = 1
# Variable importante; es la que nos ayudara a salir de un bucle.
varibaleDeSalida = 0
# Lo usaremos como un contador, que nos dara
# los turnos de cada tirada
turnos: int = 0

#* ------------------------ LA LOGICA ------------------------
# Este bucle lo que hace es hacer tirada, hasta que una condición rompa ese bucle.
while varibaleDeSalida != 1:
    # Aquí es donde la magia surge; haremos que 2 dados tengas nuevos aleatorios hasta que
    # el bucle acabe.
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    # Aquí está la condición que rompe ese bucle, aquí lo haremos es comparar si los 2 dados
    # son iguales; haremos que la variable de salida, pase a 1.
    if dado1 == dado2:  #hacemos la comparación
        varibaleDeSalida = 1
    # Incrementamos el contador.
    turnos += 1

# Creamos "información" donde almacenaremos los datos el último dato del dado que salió de manera
# aleatoria, así como también mostraremos cuantos turnos ha tardado hasta llegar a coincidir.
informe = f"""
JUEGO DE LOS DADOS IGUALES
EL PRIMER DADO ES:{dado1}
EL SEGUNDO DADO ES {dado2}
HAS TARDADO {turnos} PARA QUE
SEAN IGUALES
"""

print(informe)
