"""
 11. Modificar el programa anterior para que, además, nos diga al final cual han sido el
número mayor y el menor que has introducido
"""

salir = False
contador = 0
resultadoFinal = 0
numeroMayor = 0
numeroMenor = 99
while True:
    dato = input("Introduce un número o la palabra FIN... ")

    if dato == "FIN":
        break  # salimos del bucle

    if dato.isdigit():   # comprobar si es número
        numero = int(dato)

        if 1 <= numero <= 100:
            resultadoFinal = numero + resultadoFinal
            contador += 1
            if numeroMayor < numero:
                numeroMayor = numero
            if numeroMenor > numero:
                numeroMenor = numero
        else:
            print("Error: número fuera de rango (1-100)")
    else:
        print("Error: entrada no válida")

print("Entradas válidas:", contador)
print(f"Resultado final: {resultadoFinal}\nel numero menor es: {numeroMenor} y el mayor es: {numeroMayor}")
