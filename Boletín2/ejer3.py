"""3. Escribir un programa que pida un número por teclado al usuario que simule ser el precio
de un artículo y escriba el resultado de aplicarle el IVA del 21%. El resultado debe de
estar redondeado a dos decimales"""

precio = float(input("Introduce el precio...\n"))
IVA = 1.21
precioFinal = round((precio*IVA),2)

print(f"El precio Final de {precio} es :{precioFinal}")