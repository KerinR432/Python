"""
5. Escribir un programa que nos diga si un número es capicúa.
"""
# ----------------- FUNCIONES --------------------------
def EncontrarCapicua(numero):
    numeroAlReves = numero[::-1]

    numero = int(numero)
    numeroAlReves = int(numeroAlReves)
    if (numero == numeroAlReves):
       return True
    return False
#----------------------- DECLARAAR VAIRIABLES -------------------
salir = False

#----------------- LOGICA ------------------------
while salir == False:
    try:
        print(f"BEINVENIDO AL ADIVINADOR DE CAPIUAS")
        numero = input("Introduce un nuemero para saber si es capicua... ")
        if EncontrarCapicua(numero):
            print(f"""
                   TU NUMERO ES CAPICUA
                   {numero} y {numero[::-1]}
                   son lo mismo felicidades
                               """)
        else:
            print(f"""
            Vaya liada tu numero {numero} no 
            es para nada capicua porque sale:
            {numero[::-1]}    
            """)


    except ValueError:
        print("Error, debes introducir un numero...")


    else:
        print("Fin del programa")
        salir = True