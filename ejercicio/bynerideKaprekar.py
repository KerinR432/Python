numeroKa = input("Introduce un nuemero: ")

def ordenarMenorAMayor(num):
    cadenaNumero = list()
    for i in num:
        cadenaNumero.append(int(i))
    cadenaNumero.sort()
    return cadenaNumero


def ordenarMayorAMenor(num):
    cadenaNumero = list()
    for i in num:
        cadenaNumero.append(int(i))
    cadenaNumero.sort(reverse=True)
    return cadenaNumero

numMayor = ordenarMayorAMenor(numeroKa)
numMenor = ordenarMenorAMayor(numeroKa)

numMenor = str(numMenor)
numMayor = str(numMayor)

numMenor = numMenor.replace("[", "")
numMenor = numMenor.replace("]", "")
numMenor = numMenor.replace(",", "")
numMenor = numMenor.replace(" ", "")

numMayor = numMayor.replace("[", " ")
numMayor = numMayor.replace("]", " ")
numMayor = numMayor.replace(",", "")
numMayor = numMayor.replace(" ", "")

numMenor = int(numMenor)
numMayor = int(numMayor)

rsdo = numMayor - numMenor

print(f"La Resta de {numMayor} - {numMenor} = {rsdo}")