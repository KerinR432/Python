import random
#EJERCICIO 14
print("****************************************")
#* ------------------ FUNCIONES --------------------------
def numeroAletorio(num1, num2):
    """
    Objetivo: generar numeros aelatorio, entre 2 numeros.
    1. Pasamos 2 numeros por parametro.
    2. hacemos un random entre esos dos numeros (ej. 12 a 15) sacara un numero aleatorio
    entre ellos.
    3. Devolvemos lo que es un resultado.
    :param num1:
    :param num2:
    :return:
    """
    resultado = random.randint(numero_1, numero_2)
    return resultado

#* ------------------- VARIABLES --------------------------
# Esta variable es importante, es la que controla si un bucle sigue funcionando o no
salir = False

#* ---------------------- LOGICA ---------------------------
#Este bucle while, aloja toda la logica de codigo, tenemos tambien un try-except
# donde manejaremos errores.
while not salir:
    # el try llevara toda la logica y los condiconales para impedir fallos
    try:
        # pedimos 2 numeros por teclado
        numero_1 = int(input("Introduce un numero: "))
        numero_2 = int(input("Introduce un segundo numero: "))

        # Condición para impedir que los numeros sean, menores a 0.
        if numero_1 < 0 or numero_2 <= 0:
            raise Exception("No es un numero positivo")
        # Llamos la función para que haga su magia.
        resultadoAleatorio = numeroAletorio(numero_1, numero_2)
    # Una exeepción que saltara cuando el usuario mete mal un dato (ej. A en vez de un numero)
    except ValueError as e:
        print(f"Error {e} debe ser un numero entero")
    # Para errores genericos.
    except:
        print("error!!!")

    # Este else, soltara todo lo que tenga, cuando no falle el try
    else:
        # Por ultimo, generamos un texto de información donde almacenaremos
        # los numeros que mete el usuario y el aleatorio que salga.
        informe = f"""
        los numeros alaterios que elgistes es:
        {numero_1} y {numero_2}.
        el numero aleatorio que salio de ahi es:
        {resultadoAleatorio}
        """
        # Mostramos ese infome.
        print(informe)
        print("saliedo....")
        # Cambiamos la variable de salida.
        salir = True