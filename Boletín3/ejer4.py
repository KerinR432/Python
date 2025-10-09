"""4. Escribir un programa que pida por teclado una cadena de texto y la escriba en sin
espacios en blanco (si los hubiera). Además, nos debe de decir el número de espacios
que ha encontrado y suprimido"""
texto = input("Introduce un texto\n")
cont = 0
for i in range(len(texto)):
    if texto.__eq__(" "):
        cont = cont + 1

texto = texto.replace(" ", "")
print(texto)
print(f"el numero de espacios es: {cont}")