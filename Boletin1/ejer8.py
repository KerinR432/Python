"""
 8. Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros
(puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un
número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos
intereses de ningún tipo y redondeamos a dos decimales.
"""
#* --------------------- Definición de Funciones --------------------------------
def calcularPagoAlMes(pagar,meses):
    """
    Objectivo: Recibimos lo que tienes que pagar y el mes.
    1. Pasa un mes y precio por parametro (Ejemplo: 100€ y 2 meses).
    2. hacemos una peración, dividiendo lo de pagar y los meses, a su ves los redondeamos a 2 (resultado = 100/2).
    3. Devolvemos el resultado de la pagar y el mes.
    """
    # Realizamos un opoeración de division (100 / 2) y devolvemos un resultado.
    return round(pagar / meses, 2)

#* ------------------- Variable de Control ---------------------------------------
# Esta variable actúa como un interruptor si es 'False' el programa sigue sigue pididiendo datos.
# Cuando es 'True', el programa sabe que tiene los datos correctos y debe terminar.
salir = False

#* ------------------- Lógica Principal del Programa -----------------------------
# Iniciamos un blucle repetivo ('while') que se ejecuta *mientras* 'salir' sea 'False'.
# Esto nos permite forzar al usuario a introducir los datos correctos.
while salir !=True:
    try:
        # El bloque 'try' es un intento de ejecutar código que podría fallar (manejo de error).
        # 'int(input(...))' y 'float(input(...))' significa que esperamos un numero entero para los meses y decimal para pagar.
        pagar = float(input("Introduce el importe a pagar en euros: "))
        meses = int(input("Introduce el número de meses: "))

        # Validación: si pagar o meses son números negativos, generademos un error.
        # Para que el programa salte al bloque 'except' y pida los datos nuevo.
        if pagar <= 0:
            # Forzamos un error de tipo ValueError.
            raise ValueError("El importe debe ser mayor que 0.")
        if meses <= 0:
            raise ValueError("El número de meses debe ser un entero positivo.")
        # Llamamos a nuestras función 'calcularPagoAlMes'  que haga su trabajo.
        apagarCadaMes = calcularPagoAlMes(pagar,meses)

        # preparamos el mensaje final con los datos de pagar y mes y el pago por el mes
        factura = f"""
        -- FACTURA --
        DEBES PAGAR {pagar:.2f}€
        DURANTE {meses} MESES
        EN TOTAL PAGAS AL MES
        -- {apagarCadaMes:.2f}€ --
        """
    except ValueError as e:
        print("Error:", e)
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    # El bloque 'else' solo se ejecuta si el 'try' tuvo exito SIN NINGÚN ERROR.
    else:
        # Mostrar resultado.
        print(factura)
        # Cambiar el interruptor a 'True' para detener el bucle 'while'.
        salir = True

