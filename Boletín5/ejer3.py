"""3. Escribir un programa que cuenta las palabras que tiene una frase introducida
previamente por teclado. Las palabras pueden estar separadas por más de un espacio
pero siempre debe de haber al menos uno. No tenemos en cuenta los signos de
puntuación como separadores."""

texto =input("Introduce texto:\n")
cont = 0
for i in range(0,len(texto)):
    if texto[i] == " ":
        cont += 2

print(cont)