import random
#EJERCICIO 14
print("****************************************")


def numeroAletorio(num1, num2):
    resultado = random.randint(numero_1, numero_2)
    return resultado

salir = False

while not salir:
    try:
        numero_1 = int(input("Introduce un numero: "))
        numero_2 = int(input("Introduce un segundo numero: "))

        if numero_1 < 0 or numero_2 <= 0:
            raise Exception("No es un numero positivo")

        resultadoAleatorio = numeroAletorio(numero_1, numero_2)
    except ValueError as e:
        print(f"Error {e} debe ser un numero entero")

    except:
        print("error!!!")


    else:

        informe = f"""
        los numeros alaterios que elgistes es:
        {numero_1} y {numero_2}.
        el numero aleatorio que salio de ahi es:
        {resultadoAleatorio}
        """
        print(informe)
        print("saliedo....")
        salir = True