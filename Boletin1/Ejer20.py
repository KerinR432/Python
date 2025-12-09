#* ------------------ Definición de Funciones ------------------
def ordenarNuemeros(num1, num2,num3):
    """
    Obejtivo: Recibir 3 Numeros y devolverlos de menor a mayor.
    1. pasan 3 numeros por parametro.
    2. Los metemos en una caja donde con tiene los 3 numeros.
    3. Ordenamos el contenido de la caja.
    4. Devolvemos la caja.
    :param num1:
    :param num2:
    :param num3:
    :return:
    """
    # creamos una lista (caja) vacia para guardar lso numeros.
    listaOrdenada = []
    # agregamos los 3 numeros en la lista
    listaOrdenada.append(num1)
    listaOrdenada.append(num2)
    listaOrdenada.append(num3)
    #Usamos el metodo 'sort()' para ordenar los numeros de menos y mayor.
    listaOrdenada.sort()
    #devolvemos la lista ordenada.
    return listaOrdenada

#* ------------------ Variables de Control ------------------

# Esta variable actúa como un interrucptor: si es 'False' el programa sigue pidiendo datos.
# Cuando es 'True' , el programa sabe que tiene los datos correctos y debe terminar.
salir = False

#* ------------------ Lógica Principal del Programa ------------------

# Iniciamos un bucle repetivo ('while') que se ejecuta *mientras* 'salir' sea 'False'.
# Esto nos permite forzar al usaurio a introducir los datos correctamente.
while not salir:
    #el bloque 'try' es un intento de ejecutar código que podría fallar (manejo de error).
    try:
        # Pedimos los tres números al usuario por teclado.
        # 'int(input(...))' significa que esperamos un numero entero.
        numero_1 = int(input("Introduce un numero: "))
        numero_2 = int(input("Introduce un numero: "))
        numero_3 = int(input("Introduce un numero: "))

        # Validación: Si cualquiera de los números es negativo, generamos un error
        # Para que el programa salte al bloque 'except' y pida los datos de nuevo.
        if numero_1 < 0  or numero_2 < 0 or numero_3 < 0:
            # Forzamos un error error de tipo 'Exception'
            raise Exception("Error, debe ser numeros enteros y positivos")
        # Llamamos a nuestra funcion 'OrdenarNumero' para que haga su trabajo
        # y convetir el resultado a texto para poder mostrarlo facilmente.
        ordenadoTexto = str(ordenarNuemeros(numero_1, numero_2, numero_3))
    # El bloque 'except' captura cualquier error que haya ocurrido en el 'try'
    # Este 'except' maneja nuestros error personalizado (números negativos).
    except Exception as ex:
        print("Error, debe ser un numero enteros y positivos")
    # Este 'except' maneja el error de 'ValueError' (Por ejemplo si el usuario escribe 'hola' en lugar de un número)
    except ValueError:
        print("Error, debe ser un numero enteros y positivos")
    # El bloque 'else' solo se ejecuta si el 'try' tuvo exito SIN NINGÚN ERROR.
    else:
        # Preparamos el mensaje final con los números originales y los ordenados
        formato=f"""
        LOS NUMEROS ORIGINALES ES:
        {numero_1},{numero_2},{numero_3}
        ORDENADAS SON:
        {ordenadoTexto}
"""
        # Mostrar los resultado.
        print(formato)
        print("Saliendo...")
        # Cambiar el interruptor a 'True' para detener el bucle 'while'
        salir = True