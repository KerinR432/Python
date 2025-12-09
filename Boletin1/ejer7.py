"""
7. Escribir un programa que pida un número por teclado al usuario que simule ser el precio de
un artículo y escriba el resultado de aplicarle el IVA del 21%
"""


def calcularPrecioConIva(precioSinIva, IVA):
    return precioSinIva * IVA

# Pedimos el dato (usamos float para permitir decimales)
precioSinIva = float(input("Ingresa un monto: "))
IVA = 1.21
precioConIva = calcularPrecioConIva(precioSinIva, IVA)

# Creamos la factura usando f-strings correctamente
# Usamos :.2f para que siempre muestre 2 decimales
factura = f"""
--- TICKET DE COMPRA ---
PRECIO DEL ARTÍCULO: {precioSinIva:.2f}€
EL IVA APLICADO:     21%
PRECIO FINAL:        {precioConIva:.2f}€
"""

print(factura)