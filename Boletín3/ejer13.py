"""
3. Modifica el programa anterior contemplando que entre los números y las letras
podría haber un espacio en blanco (uno solo) o un guión. En ambos casos se
considerará también que la matrícula es válida (si cumple todo lo demás, claro)
"""
import re

#* ----------------------- DECLARAMOS VARIBLES ---------------------
# Esta variable, es el patrón por el cual, se regira todas las matriculas.
patron = r"[0-9]{4}(\s|-)?[BCDFGHJKLMNPRSTVWXYZ]{3}"
# Una variable de las importante; es el controlador, para detener un bucle while.
salir = False

#* ------------------------- LUGAR LOGICO ----------------------------
# Este bucle while, lo que hace es tener la logica del programa
# mientras que la condición no funcione y se cambie su variable, sera ejecutandose
while not salir:
    # El try maneja lo que es la logica, al mismo tiempo, comprobamos si el patron funciona
    try:
        matricula = input("Introduce una matricula(ej.4325SFG): ")
        # Aqui es donde veremos si el patron es igual a la matricula.
        if re.fullmatch(patron, matricula):
            print("Funciona")
        # Por si acaso, tenemos un raise que salte un error, sin no encuentra coincidencias
        else:
            raise  Exception ("La matricula no ha sido encontrada, has introducido bien la matricula.")
    except:
        print("Error, has introducido algo que no es una matricula.")

    # Aqui cambiaremos la variable de salida, asi como mostrar mas datos.
    else:
        # Creamos un informe, donde metemos la matricula y mostramos un mensaje
        print("Saliendo...")
        informacion = f"""
        tu matricula es {matricula}
        ha sido encontrada, tu coche
        ha sido registrado
"""
        # Mostramos el informe.
        print(informacion)
        # Cambiamos la variable de salida.
        salir = True