"""
7. Escribir un programa que pida un número por teclado al usuario que simule ser el precio de
un artículo y escriba el resultado de aplicarle el IVA del 21%
"""

dinero = int(input("Introduce el dinero: "))
IVA = 1.21
dineroConIVA = dinero * IVA

print("El producto con el precio ",dinero,"$","Incluyendo el IVA 21% el resultado es: ",dineroConIVA,"$")