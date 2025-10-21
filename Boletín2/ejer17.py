"""17. Escribir un programa que reciba por teclado una temperatura en cualquiera de las
tres unidades básicas (Celcius, Farenheit o Kelvin) y la devuelva en las otras dos"""

op = 0
while op != 4:
    print("1. Grados celcius\n2.Grados Farenheit\n3.Grados Kelvin\n4.salir")
    op = int(input("Ingresa un opción:\n"))
    match op:
        case 1:
            grados = float(input("Introduce tu temperatura:\n"))
            gradosF = (grados *1.8)+32
            gradosK = grados + 273.15
            print(f"tu temperatura es de {round(grados,2)}C en Farenheit es: {round(gradosF,2)}F y el Kelvin son : {round(gradosK,2)}K")
        case 2:
            gradosF = float(input("Introduce tu temperatura:\n"))
            gradosC = (gradosF - 32)/1.8
            gradosK = gradosC + 273.15
            print(f"tu temperatura es de {round(gradosF,2)}F en Celcius es: {round(gradosC,2)}C y el Kelvin son : {round(gradosK,2)}K")
        case 3:
            gradosK = float(input("Introduce tu temperatura:\n"))
            gradosC = gradosK - 273.15
            gradosF = (gradosC *1.8)+32
            print(f"tu temperatura es de {round(gradosK,2)}K en Celcius es: {round(gradosC,2)}C y el Farenheit son : {round(gradosF,2)}F")
        case 4:
            print("Salir del Programa")
        case _:
            print("Introduce un error")