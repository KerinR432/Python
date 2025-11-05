texto = "33"
if texto.isdigit(): # este comprueba si existe un numero entero o solo tiene texto
    print("Puedo convertirlo a entero")
else:
    print("No puedo convertirlo a entero")

texto = "33"
if texto.isalpha(): # aquí si existe caracteres o numero o '-','*' etc
    print("No tiene numero")
else:
    print("Si es numero")