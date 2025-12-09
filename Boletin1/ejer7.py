# * ----------------- Definición de Funciones (Recetas) -------------------------------
def calcularPrecioConIva(precioSinIva, IVA):
    """
    Objetivo: Recibir un precio base y un factor IVA (como 1.21) para calcular el precio final con el impuesto incluido.

    1. Toma el precio original (por ejemplo, 100€).
    2. Lo multiplica por el factor IVA (por ejemplo, 1.21).
    3. Devuelve el nuevo precio que ya incluye el 21% de impuesto.
    """
    # Devolvemos el resultado. La multiplicación por 1.21 asegura que obtenemos
    # el precio original MÁS el 21% de ese precio.
    return precioSinIva * IVA


# * ------------------ Variables Importantes -----------------------------------------------

# Esta variable es el 21% del IVA, pero expresado como factor decimal (1 + 0.21).
# Multiplicar por 1.21 equivale a: Precio_Original + (Precio_Original * 0.21).
IVA = 1.21

# * ------------------ Lógica Principal del Programa ---------------------------

# Pedimos el precio al usuario por teclado.
# 'float(input(...))' significa que esperamos un número decimal (para centavos/céntimos).
precioSinIva = float(input("Ingresa el precio del artículo sin IVA: "))

# Llamamos a nuestra la función 'calcularPrecioConIva' para que haga su trabajo.
precioConIva = calcularPrecioConIva(precioSinIva, IVA)

# Creamos la "factura" usando f-strings para darle formato.
# Usamos ':.2f' para asegurar que el precio siempre muestre 2 decimales (el formato de moneda).
factura = f"""
--- TICKET DE COMPRA ---
PRECIO DEL ARTÍCULO: {precioSinIva:.2f}€
EL IVA APLICADO:     21%
PRECIO FINAL:        {precioConIva:.2f}€
"""
# Mostramos el resultado.
print(factura)