#* ------------------ Definición de Funciones (Recetas) ------------------
def ordenarNuemeros(num1, num2,num3):
    listaOrdenada = []
    listaOrdenada.append(num1)
    listaOrdenada.append(num2)
    listaOrdenada.append(num3)
    listaOrdenada.sort()
    return listaOrdenada

#* delcarar Variables

salir = False

#* hacemos un bucle para evitar que el usuario meta datos incorrectos
while not salir:
    try:
        # pedimos por teclado
        numero_1 = int(input("Introduce un numero: "))
        numero_2 = int(input("Introduce un numero: "))
        numero_3 = int(input("Introduce un numero: "))

        #! si el numero es menor a 0 ejecutar un error
        if numero_1 < 0  or numero_2 < 0 or numero_3 < 0:
            raise Exception("Error, debe ser numeros enteros y positivos")

        ordenadoTexto = str(ordenarNuemeros(numero_1, numero_2, numero_3))
    except Exception as ex:
        print("Error, debe ser un numero enteros y positivos")
    except ValueError:
        print("Error, debe ser un numero enteros y positivos")

    else:
        formato=f"""
        LOS NUMEROS ORIGINALES ES:
        {numero_1},{numero_2},{numero_3}
        ORDENADAS SON:
        {ordenadoTexto}
"""
        print(formato)
        print("Saliendo...")
        salir = True