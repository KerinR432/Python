"""
 25. Escribir un programa que reciba por teclado un número y muestre sucesivamente el
resultado de ir dividiéndolo por dos sucesivamente hasta llegar a un número igual o menor a
1. Caso de ser necesario los resultados se mostrarán con dos decimales. Un ejemplo de una
ejecución correcta después de introducir el número 34 ser´ía esta:
 Haz introducido el número 34
 17
 8.5
 4.25
 2.12
 1.06
 0.53
"""

#*-----------------------
#*funciones
def numeroDivesiblesADos(numero,salir):
    while salir:
        numero = numero / 2
        if numero <= 1:
            salir = False
        print(numero)


#*-----------------------
#*declar varibles
numero = int(input("introduce un numero... "))
salir = True

#*------------------------
#*main
numeroDivesiblesADos(numero,salir)






