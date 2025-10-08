"""2. Modifica el programa anterior para que cuando coincidan ambas contraseñas nos
informe del número de intentos inválidos"""

correcto = False
password = input("Introduce una contraseña:\n")
passSave = password
contFallos = 0


while not correcto:
    password = input("Vuelve introducir la contraseña:\n")
    if password.__eq__(passSave):
        print("Bien estas dentro🎊")
        print(f"has hecho {contFallos} intentos")
        correcto=True
    else:
        print("Error, vuelve introducir la contraseña 😔")
        contFallos=contFallos+1