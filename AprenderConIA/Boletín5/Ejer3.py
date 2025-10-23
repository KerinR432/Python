"""Programa que cuenta cuántas palabras hay en una frase introducida por el usuario,
ignorando signos de puntuación y espacios extra."""

import string  # para eliminar signos de puntuación

# Pedimos la frase
texto = input("Introduce un texto:\n")

# Eliminamos signos de puntuación comunes (, . ! ? etc.)
for signo in string.punctuation:
    texto = texto.replace(signo, "")

# Dividimos el texto en palabras, sin importar si hay varios espacios
palabras = texto.split()

# Contamos cuántas palabras hay
cantidad = len(palabras)

# Mostramos el resultado
print(f"Tu frase tiene {cantidad} palabra(s).")
