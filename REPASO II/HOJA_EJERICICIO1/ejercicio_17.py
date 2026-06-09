"""
17. Escribir un programa que nos permita generar una quiniela. Para ello nos debe generar
quince números aleatorios entre el 1 y el 3. Recuerda que los resultados válidos son 1 X o 2,
así que si te sale un 3 lo que tienes que imprimir en pantalla es una X
"""

import random
quiniela = []

for n in range(15):
    numero = random.randint(1,3)

    if numero == 3:
        quiniela.append("X")
    else:
        quiniela.append(str(numero))

print("La quiniela es: ",quiniela)