"""
 10. Modificar el programa anterior para que nos muestre al final la media aritmética de
las entradas válidas
"""
salir = False
contador = 0
resultadoFinal = 0
while True:
    dato = input("Introduce un número o la palabra FIN... ")

    if dato == "FIN":
        break  # salimos del bucle

    if dato.isdigit():   # comprobar si es número
        numero = int(dato)

        if 1 <= numero <= 100:
            resultadoFinal = numero + resultadoFinal
            contador += 1
        else:
            print("Error: número fuera de rango (1-100)")
    else:
        print("Error: entrada no válida")

print("Entradas válidas:", contador)
print(f"Resultado final: {resultadoFinal}")
