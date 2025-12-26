"""
10. Escribir un programa que nos pida una cadena por teclado y luego nos imprima sólo
las cifras que aparecen en ella.
Por ejemplo, si introducimos la cadena “Beverly Hills, 5. CP: 28934” Debería
devolvernos: 528934
"""

texto = "beverly Hills, 5. CP: 28934"

for letra in texto:
    if texto.isdigit():
        print("tiene numeros")