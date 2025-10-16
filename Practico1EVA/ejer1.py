import random

print("======================================")
cantidadDados =  int(input("Introduce el numero de dados que quieres que se juegue\n"))

dados = []
igual = False
texto = " "
num = " "
cont = 0
while not igual:
    dados.clear()
    for i in range(0, cantidadDados):
        dados.append(random.randint(1, 6))
        texto = str(dados)
    num = texto[1:2]
    print(" - ".join(str(dados)))
    if texto.count(num)==cantidadDados:
        igual = True
    cont += 1


print(f"las veces que re repitio {cont}")