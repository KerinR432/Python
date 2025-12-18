"""
8. Escribe un programa que sume por un lado las cifras pares y por otro las impares de
un número y nos muestre ambos resultados. Por ejemplo, si el número en cuestión es
el 128 nos debería e decir que la suma de las cifras pares es 9 y la de las impares 2
"""
numero = 128
numeroPar = 0
numeroImpar = 0
salir = False
while salir == False:

    if numero % 2 == 0:
        numeroPar=numeroPar+1
        numero = float(numero // 2)
    else:
        numeroImpar=numeroImpar+1
        numero = float(numero // 2)

    if numero == 0:
        salir = True

print(f"El numero es: {numero}\n los numeros pares: {numeroPar} y pares: {numeroImpar}")