"""
 8. Escribir un programa que reciba una cadena de texto por teclado y la muestre sin
vocales. Por ejemplo, si recibe la cadena “Hola Mundo” debería de devolver “Hl Mnd”.
"""
import re

patron = r"[aeiuo]"

texto = input("Introduce un texto.... ")

if re.search(patron,texto):
    textoNuedvo = re.sub(patron,"",texto)
    print(textoNuedvo)