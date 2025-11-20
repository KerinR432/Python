#*IMPORTACIONES
import re
from logging import exception

#*EJERCICIOS
"""
4. Validar un número de teléfono con prefijo internacional (empieza por el signo + seguido 
de dos dígitos, luego un espacio y a continuación un número de teléfono. 
Ejemplo +34 912233444
"""
#*DECLARAR VARIABLES
correcto = f"""
===========================
Genial, has introducido el 
numero bien. Ahora procede
la llamada,📲📲📲
===========================
"""
incorrecto =f"""
===========================
Mal, has introducido el 
numero mal, vuelve a inte-
tarlo, gracias.
===========================
"""
salir = False
patron = r'[+]{1}[34]{2}[\s]{1}[0-9]{9}'
#?DECLARAR FUNCIONES
#aqui comprobamos el numero telefonico, es realmente de españa o no
def comprobarNumeroTelefonicoInt(p,n):
    if re.search(p,n):
        return True
    return False
#*MAIN
while not salir:
    try:
        numeroTelefonicoIn = input("Introduce un numero telefonico de España: ")
    except ValueError:
        print(f'Has introducido algo que no es un nuemero... vuelve a intentar')
    else:
        if comprobarNumeroTelefonicoInt(patron,numeroTelefonicoIn):
            print(correcto)
            salir = True
        else:
            print(incorrecto)
