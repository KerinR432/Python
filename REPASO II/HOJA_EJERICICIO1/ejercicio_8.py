"""
8. Escribir un programa que reciba por teclado el importe de una cantidad a pagar en euros
(puede tener decimales) y el número de meses que contamos para pagarla (tiene que ser un
número entero) y nos devuelva el dinero que tendríamos que pagar cada mes. No aplicamos
intereses de ningún tipo y redondeamos a dos decimales.
"""
dinero = int(input("Ingrese el numero de dinero: "))
meses = int(input("Ingrese el numero de meses: "))


dineroPorMes = dinero / meses

print("Debes pagar ",dinero,"$ ","El tiempo en meses",meses,"Debes pagar cada mes ",dineroPorMes,"$")