"""
12. Escribir un programa que sirva como asistente para un juego de rol. Tu programa debería de
pedir por teclado el número de dados que se van a tirar y el número de caras de estos (4, 6,
8, 12, etc.) A continuación debería de hacer la tirada y mostrarla.
"""
import random
dados = []
numeroDeCaras = 0
numeroDeDados = 0

numeroDeDados = int(input("Introduce la cantidad de dados: "))
numeroDeCaras = int(input("introduce la catidad de caras: "))

for d in range(numeroDeDados):
    dados.append(random.randint(1,numeroDeCaras))

print(dados)