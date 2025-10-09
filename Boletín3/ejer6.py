"""6. Escribir un programa que pida por teclado una cadena de texto y la separe en dos
distintas. En la primera de ellas estarían las letras que ocupan una posición par y en la
segunda las que ocupan una posición impar. Por ejemplo, si el usuario escribe Hola
Mundo la primera cadena sería Hl ud y la segunda oaMno"""

texto = input("Introduce un texto...\n")

textoPar = texto[::2]
print(textoPar)
