"""7. Escribir un programa que pida por teclado una cadena de texto y la escriba con el
alfabeto típico de los hackers sustituyendo las letras a por el número 4, las letras e por
el número 3, las letras i por el número 1 y las letras o por el número 0. Considera que
las vocales pueden estar escritas en mayúsculas o minúsculas, pero no hace falta que
tengas en cuenta que además podrían ir acentuadas
"""
texto = input("Ingresa una cadena de texto:\n ")

texto = texto.lower()
texto = texto.replace("a","4")
texto = texto.replace("e","3")
texto = texto.replace("i","1")
texto = texto.replace("o","0")

print(texto)