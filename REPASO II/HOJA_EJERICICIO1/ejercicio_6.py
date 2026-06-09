"""
6. Escribir un programa que pida por teclado un número al usuario y diga si es divisible por 3 o
no.
"""
numero = int(input("ingrese un numero: "))
"""
1. str(n)
Convierte el número n en una cadena de texto (string).

2. for d in str(n)
Itera sobre cada carácter de esa cadena.

3. int(d)
Convierte cada carácter de vuelta a número entero.

4. sum(...)
Suma todos esos enteros.
"""
suma = sum(int(d) for d in str(numero))

if suma % 3 == 0 :
    print("el", numero," Es divisible entre 3")
else:
    print("el", numero," No divisible entre 3")