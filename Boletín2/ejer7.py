"""7. Escribir un programa que pida un número por teclado y nos imprima la tabla de
multiplicar de dicho número del 1 al 10. Por ejemplo, si introducimos el 74 el resultado"""
#pedimos por teclado un numero ⌨️
num = int(input("Introduce un numero: \n"))

#con un bucle mostramos la sumas
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")