import random

#EJERCICIO 12
print("======================================")



def dadosAletorios(cantidadDados,cantidadCara,dados):
    for i in range(0, cantidadDados):  # --> el tamaño del bucle es la cantidad de dados

        dados.append(
            random.randint(1, cantidadCaras))  # --> rellenamos el array depediendo de los dados y caras que pidamos
    informe = f"""
    se han lanzado: {cantidadDados} dados
    con {cantidadCara} caras
    el resultado de las tirasdas es:  {dados}
"""
    print(informe)
#Creamos un try cath para validaciones
salir = False
while not salir:
    try:
        cantidadDados =  int(input("Introduce el numero de dados que quieres que se juegue: "))
        dados = [] #--> creamos lo que es un Array para almacenar los dados
        cantidadCaras = int(input("Introduce el numero de caras de los dados: "))
        if cantidadDados <= 0:
            raise Exception("No es un numero positivo")
        if cantidadCaras <= 0:
            raise Exception("No es un numero positivo")
        dadosAletorios(cantidadDados,cantidadCaras,dados)



    except ValueError:
        print("Error debe ser un numero entero")

    except:
        print("Error debe ser un numero entero")
    else:
      print("Saliendo...")
      salir = True

