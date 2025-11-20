#*IMPORTACIONES
import re

#*TEORÍA
"""
Validar un código postal de Madrid. Cinco números, los dos primeros siempre son el 28
Ejemplo: 28032
"""

#* DECLARAR VARIABLES
correcto = f"""
================================
Bien, has introducido bien el 
el codigo postal, tu paquete 
ha sido enviando.
😁😁😁😁😁😁😁😁😁😁😁😁😁😁
"""

incorrecto = f"""
================================
Mal, has introducido un codigo postal
que no era. Vuelve intentarlo.
😢😢😢😢😢😢😢😢😢😢😢😢😢😢
"""
salir = False

patron =r"[2 8]{2}?[0-9]{3}"

#TODO METODOS
#Metodo donde comprobamos si el codigo postal es verdadero
def comprarCodigoPostal(c, p):
    if re.match(p, c):
        return True

    return False

#*MAIN
while not salir:
    try:
        codigo = input("Introduce un código postal: ")

    except ValueError:
        print(incorrecto)

    else:
        if comprarCodigoPostal(codigo,patron):
            print(correcto)
            salir = True
        else:
            print(incorrecto)
            salir = False

    finally:
        print(f"Seguiremos mas adelante, gracias")



