"""
11. Modificar el programa anterior para que tu programa tire dos dados de forma continuada
hasta que el número que salga en ambos sea el mismo. En ese momento debería de parar la
ejecución e informarnos de cuantas tiradas ha tenido que hacer para llegar a ese resultado

"""

import random
dado_uno = 0
dado_dos = 0
contador = 0
while True:
    dado_uno = random.randint(1,6)
    dado_dos = random.randint(1,6)

    if dado_uno == dado_dos:
        break

    contador+=1

print("El intentos que tuiveron que pasar para que los dados sean iguales",contador)