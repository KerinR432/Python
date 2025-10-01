# El case
numero = 0
while(numero!=5):
    numero = int(input("Introduce un nuemro del 1 al 4"))
    match numero: #Se utiliza el match
        case 2: #Llamos el case
            print("El numero es el 2")
        case 3 | 4: #entra entre 2
            print("El numero es el 3 y el 4")
        case 5:
            print("Salir")
        case _: #seria el default
            print("No es ni el 2 ni el 3")
print("FIN")
