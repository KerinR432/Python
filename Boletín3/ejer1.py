"""Escribir un programa que pida una contraseña por teclado (dos veces) y si no
coinciden nos lo vuelva a pedir hasta que lo hagan"""

correcto = False
password = input("Introduce una contraseña:\n")
passSave = password


while not correcto:
    password = input("Vuelve introducir la contraseña:\n")
    if password.__eq__(passSave):
        print("Bien estas dentro🎊")
        correcto=True
    else:
        print("Error, vuelve introducir la contraseña 😔")

