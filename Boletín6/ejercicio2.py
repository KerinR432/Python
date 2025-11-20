#*IMPORTACIONES
import re
#*INFORMACIÓN
"""
 2. Validar un número de teléfono
 Ejemplo: 91345566
"""

#*DECLARAR VARIABLES
correcto = f"""
===========================
¡Genial el numero que has  
introducido es correcto!.
😁😁😁😁😁😁😁😁😁😁
===========================
"""

incorrecto = f"""
===========================
¡Muy mal has introducido un
numero no valido!.
😢😢😢😢😢😢😢😢😢😢
===========================
"""
salir = False
patron = "[6-8]{1}[0-9]{8}"

#? DECLARAR FUNCIONES
#* función de comprobar si es un numero
def comprobarNumeroTelefonico(p,n):
    if re.match(p,n):
        return True
    return False

while not salir:
    try:
        numeroT = int(input("Introduce un  numero de teléfono: "))
    except ValueError:
        print("Error no has introducido un numero")
    else:
        if comprobarNumeroTelefonico(patron,str(numeroT)):
            print(correcto)
            salir = True
        else:
            print(incorrecto)


