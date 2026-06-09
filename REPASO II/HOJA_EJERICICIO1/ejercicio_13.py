"""
13. Modifica el programa anterior para que no admita dados con un número de caras impares
(¡no existen!). En el caso de meter un número impar de caras el programa debería de
informarnos de que es erróneo y volver a preguntarnos por este dato.

"""

import random
dados = []
numeroDeCaras = 0
numeroDeDados = 0

numeroDeDados = int(input("Introduce el numero de dados que quieras: "))

while True:
    numeroDeCaras = int(input("Introduce el numero de caras que quieras: "))

    if numeroDeCaras % 2 == 0:
        for n in range(numeroDeDados):
            dados.append(random.randint(1,numeroDeCaras))
        break

print("Los dados ha salido", dados)