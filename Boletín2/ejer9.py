"""
 9. Escribir un programa que pida números entre el 1 y el 100 por teclado hasta que
escribamos la palabra FIN (con mayúsculas). Si el usuario introduce una entrada
inválida (números superiores a 100, otras cadenas de caracteres que no sean FIN, etc.)
no se tendrá en cuenta pero se mostrará un mensaje de error y el programa seguirá
su curso. Cuando terminamos (al introducir la palabra FIN, recuerda) mostraremos
José María Morales Vázquez
 Página 1
Ejercicios genéricos de programación 2
 por pantalla el numero de entradas válidas que hemos hecho (sin contar esta última
que sólo sirve para finalizar el programa)
"""
from operator import truediv

salir = False
contador = 0

while True:
    dato = input("Introduce un número o la palabra FIN... ")

    if dato == "FIN":
        break  # salimos del bucle

    if dato.isdigit():   # comprobar si es número
        numero = int(dato)

        if 1 <= numero <= 100:
            contador += 1
        else:
            print("Error: número fuera de rango (1-100)")
    else:
        print("Error: entrada no válida")

print("Entradas válidas:", contador)




