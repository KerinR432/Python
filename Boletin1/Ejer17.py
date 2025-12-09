import random

#? declarar variables
def generarQuiniela():
    quiniela = []  # --> creamos lo que es un array

    for i in range(15):
        quiniela.append(random.randint(1, 3))  # en un bucle de 15 van genrando numero aleatorio del 1 al 3

    for i in range(15):
        if quiniela[
            i] == 3:  # --> hacemos una condición  donde comparamos existe 3 en todo el array y lo sustituimos por "x"
            quiniela[i] = 'x'
    return quiniela

quinielaTexto = str(generarQuiniela())

quinielaTexto = quinielaTexto.replace("["," ")
quinielaTexto = quinielaTexto.replace("]"," ")
quinielaTexto = quinielaTexto.replace(",","||")

formato = f"""
==========================
BIENVENIDO A LA QUINIELA
==========================
LAS VECES QUE HAS GANADO
{quinielaTexto}
"""

print(formato)

