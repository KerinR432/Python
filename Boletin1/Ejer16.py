import random

loteria = []

for i in range(6):
    loteria.append(random.randint(1,49))
    print(f"Los numeros de tu loteria son: {loteria[i]}")