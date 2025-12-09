import random
#generamos un array
#? definir funciones
def generarNumerosLoteria():
    NumerosDeLaLoteria = []
    # genera 6 numeros aleatorios y lo muestra
    for i in range(6):
        NumerosDeLaLoteria.append(random.randint(1, 49))
    return NumerosDeLaLoteria

loteria = str(generarNumerosLoteria())

loteria = loteria.replace("[", "")
loteria = loteria.replace("]", "")
loteria = loteria.replace(",", "||")
informe = \
    f"""
    ============================
        EL BONO DE LA LOTERIA
    ============================
    SON LOS SIGUEINTES:
    {loteria}
    ¡ESPEREMOS QUE GANES!
    """

print(informe)

