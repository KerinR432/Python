import random
#EJERCICIO 15
print("****************************************")

#? funciones:

def generarNumeroAletorio(num1,num2):
    if num1 > num2:  # --> una coondición que si un numeroo es mayor es el que estara al final del random.
        resultado = random.randint(num2, num1)
    else:  # --> y si no se cumple entrara aqui y el que solo queda invertir el resultado.
        resultado = random.randint(num1, num2)

    return resultado

#* Declarar variables
salir = False

#* El try y eccept
while not salir:
    try:
        numero_1 = int(input("Introduce un numero: ")) #--> pedimos un numeroo por patalla.
        numero_2 = int(input("Introduce un segundo numero: "))

        if numero_1 < 0 or numero_2 < 0:
            raise Exception("No es un numero positivo")

        resultado = generarNumeroAletorio(numero_1, numero_2)
    except ValueError as e:
        print(f"No es un numero positivo: {e}")
    except:
        print("Error")

    else:
        informe = f"""
        los numeros que has introducido:
        {numero_1} y {numero_2} 
        el resultado es {resultado}
"""

        print(informe)
        print("saliendo....")
        salir = True